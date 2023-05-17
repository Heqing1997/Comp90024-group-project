import json
import couchdb

# 连接到 CouchDB 服务器
couch = couchdb.Server('http://admin:password@172.26.135.144:5984/')

# 指定数据库名称
db_name = 'mastodon_au'

# 获取数据库对象
db = couch[db_name]

# 构建查询函数
def filter_doc(doc):
    return (
        'account' in doc and
        'followers_count' in doc['account'] and
        'following_count' in doc['account'] and
        'statuses_count' in doc['account'] and
        'content' in doc and
        'favourites_count' in doc and
        'language' in doc and
        'reblogs_count' in doc and
        'replies_count' in doc and
        'sensitive' in doc
    )

# 执行查询并提取所需字段
filtered_data = []
for doc_id in db:
    doc = db.get(doc_id)
    if filter_doc(doc):
        filtered_data.append({
            'followers_count': doc['account']['followers_count'],
            'following_count': doc['account']['following_count'],
            'statuses_count': doc['account']['statuses_count'],
            'content': doc['content'],
            'favourites_count': doc['favourites_count'],
            'language': doc['language'],
            'reblogs_count': doc['reblogs_count'],
            'replies_count': doc['replies_count'],
            'sensitive': doc['sensitive']
        })

# 输出筛选后的数据
for data in filtered_data:
    print(data)

# 将数据输出为 JSON 文件
output_file = 'filtered_data.json'
with open(output_file, 'w') as f:
    for data in filtered_data:
        json.dump(data, f)
        f.write('\n')

