# -*- coding: utf-8 -*-
import time

from nltk.sentiment import SentimentIntensityAnalyzer
import couchdb
import nltk

nltk.download('vader_lexicon')

# 创建情感分析器对象
sia = SentimentIntensityAnalyzer()

# 定义相似词列表
similar_words = ['mariage', 'berkahwin', 'menjalankan', 'marriage_ceremony', 'inter-marriage', 'conjugal', 'perkawinan',
                 'menjelang', 'remarriages', 'marriage-', 'meninggal', 'menemukan', 'mengakibatkan', 'marriage',
                 'wedding', 'casada', 'reposado', 'marriage-minded', 'homme', 'marriage-equality', 'casar', 'marrage',
                 'non-marriage', 'lanzado', 'marriages', 'marriage-related', 'post-marriage', 'pengantin', 'kesatuan',
                 'mengajar', 'gabungan', 'casados', 'interesado', 'tahan', 'spousal_relationship', 'marrige',
                 'mengajak', 'marrriage', 'mariages', 'perniagaan', 'marito', 'pensado', 'sponsali', 'patrimonio',
                 'cónyugues', 'lançado', 'noces', 'pesta_kahwin', 'pre-marriage', 'basado', 'sposalizio', 'matrimony',
                 'menjalani', 'perkahwinan', 'compañero', 'asado', 'unión', 'same-sex-marriage', 'Matrimonio',
                 'wedlock', 'berkomunikasi', 'imeneo', 'divorce', 'pasado', 'connubio', 'permasalahan', 'perjodohan',
                 'man_and_wife', 'pergabungan', 'rosado', 'époux', 'married_couple', 'marriage-based', 'demonio',
                 'bertahan', 'remarriage', 'union', 'matrimonio', 'marraige', 're-marriage', 'perubahan', 'pernikahan',
                 'marriageability', 'nikah', 'Mariage', 'matrimonii', 'pesado', 'berlebihan', 'gay-marriage',
                 'marriage-like', 'mengadakan', 'nozze', 'menikmati', 'pareja', 'noce', 'unione_matrimoniale', 'casado',
                 'marriage.', 'pesta_nikah', 'perna', 'pertumbuhan']


# 构建查询函数
def filter_doc(document):
    return (
            'account' in document and
            'followers_count' in document['account'] and
            'following_count' in document['account'] and
            'statuses_count' in document['account'] and
            'content' in document and
            'favourites_count' in document and
            'language' in document and
            'reblogs_count' in document and
            'replies_count' in document and
            'sensitive' in document
    )


def sentiment_analysis():
    # 连接到 CouchDB 服务器
    couch = couchdb.Server('http://admin:password@172.26.135.144:5984/')

    # 指定源数据库名称
    src_db_name = 'mastodon_au'

    # 获取源数据库对象
    src_db = couch[src_db_name]

    # 指定目标数据库名称
    dst_db_name = 'mastodon_au_filtered'

    # 创建或获取目标数据库对象
    if dst_db_name in couch:
        dst_db = couch[dst_db_name]
        print(f"Database '{dst_db_name}' already exists")

    else:
        dst_db = couch.create(dst_db_name)
        print(f"Created database '{dst_db_name}'")

    status_doc_id = 'last_processed_doc_time'
    # 获取状态文档，如果不存在则创建一个新的
    try:
        status_doc = dst_db[status_doc_id]
    except couchdb.http.ResourceNotFound:
        status_doc = {'_id': status_doc_id, 'last_processed_doc_time': '1970-01-01T00:00:00Z'}

    # 执行查询并提取所需字段
    while True:
        for row in src_db.iterview('_design/time/_view/time', 1000, startkey=status_doc['last_processed_doc_time']):
            doc_id = row['id']
            doc = src_db.get(doc_id)
            if filter_doc(doc):
                content = doc['content']
                tokens = content.split()  # 分割词语
                if any(any(synonym in token.lower() for token in tokens) for synonym in similar_words):  # 检查关键词
                    sentiment_scores = sia.polarity_scores(content)
                    sentiment_category = "Neutral"
                    if sentiment_scores['compound'] > 0:
                        sentiment_category = "Positive"
                    elif sentiment_scores['compound'] < 0:
                        sentiment_category = "Negative"

                    filtered_doc = {
                        '_id': doc_id,
                        'followers_count': doc['account']['followers_count'],
                        'following_count': doc['account']['following_count'],
                        'statuses_count': doc['account']['statuses_count'],
                        'content': content,
                        'favourites_count': doc['favourites_count'],
                        'language': doc['language'],
                        'reblogs_count': doc['reblogs_count'],
                        'replies_count': doc['replies_count'],
                        'sensitive': doc['sensitive'],
                        'sentiment_score': sentiment_scores['compound'],
                        'sentiment_category': sentiment_category
                    }
                    try:
                        dst_db.save(filtered_doc)
                        print(f"Filtered and analyzed data '{doc_id}' has been saved to the '{dst_db_name}' database.")
                    except couchdb.http.ResourceConflict:
                        print(f"Conflict occurred while saving doc '{doc_id}', skipping...")

            status_doc['last_processed_doc_time'] = doc['created_at']
            dst_db.save(status_doc)
            print(f"Currently processed data created at {doc['created_at']}")
        time.sleep(60)


if __name__ == '__main__':
    sentiment_analysis()
