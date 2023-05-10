import ijson
import nltk
import json
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

keywords = ["marriage", "wedding", "spouse", "bride", "groom", "marital","marry"]
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
            if any(keyword in value.lower() for keyword in keywords):
                sentiment_score = sia.polarity_scores(value)
                sentiment_label = max(sentiment_score, key=sentiment_score.get)

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

                print()

                tweet_data = {
                    "Tweet": value,
                    "Sentiment": sentiment_label,
                    "Sentiment Score": sentiment_score,
                    "Sentiment Category": sentiment_category
                }

                results.append(tweet_data)

# 添加统计结果
results.append({
    "Positive Count": positive_count,
    "Negative Count": negative_count,
    "Neutral Count": neutral_count
})

# 将结果保存为JSON文件
output_file = "output.json"
with open(output_file, 'w') as json_file:
    json.dump(results, json_file, indent=4)

print("Results", output_file)