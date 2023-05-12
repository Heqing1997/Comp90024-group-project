#### emotion analysis -- pos/neg/neu
import ijson
import nltk
import json
from nltk.corpus import wordnet
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def get_synonyms(words):
    synonyms = []
    for word in words:
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())
    return synonyms

keywords = ["married", "de facto", "divorced", "separated", "widowed", "never married"]
synonyms = get_synonyms(keywords)
print(synonyms)

file_path = "E:\\Desktop\\data\\twitter-huge.json\\mnt\\ext100\\twitter-huge.json"

# 初始化情感分析器
sia = SentimentIntensityAnalyzer()

positive_count = 0
negative_count = 0
neutral_count = 0

results = []

with open(file_path, 'r', encoding='utf-8') as file:
    parser = ijson.parse(file)

    for prefix, event, value in parser:
        if prefix.endswith('.tokens') and event == 'string':
            if any(synonym in value.lower() for synonym in synonyms):
                sentence = value.replace('|', ' ')
                sentiment_score = sia.polarity_scores(sentence)

                # 根据compound得分进行分类和统计
                if sentiment_score['compound'] < -0.5:
                    sentiment_category = "Negative"
                    negative_count += 1
                elif sentiment_score['compound'] > 0.5:
                    sentiment_category = "Positive"
                    positive_count += 1
                else:
                    sentiment_category = "Neutral"
                    neutral_count += 1

                tweet_data = {
                    "Tweet": value.replace('|', ' '),
                    "Sentiment Score": sentiment_score,
                    "Sentiment Category": sentiment_category
                }

                print(tweet_data)

                results.append(tweet_data)

# 添加统计结果
results.append({
    "Positive Count": positive_count,
    "Negative Count": negative_count,
    "Neutral Count": neutral_count
})

json_data = json.dumps(results, indent=4)

# 将结果保存为JSON文件
output_file = "emotion_analysis.json"
with open(output_file, 'w') as f:
    f.write(json_data)

print("Results", output_file)
