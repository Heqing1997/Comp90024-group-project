import json
import ijson
import gensim.downloader as api
from nltk.sentiment import SentimentIntensityAnalyzer

# Load pre-trained Word2Vec model
w2v_model = api.load('fasttext-wiki-news-subwords-300')

# Define keywords
keywords = ["marriage"]

# Get similar words to each keyword and concatenate them
similar_words = []
for keyword in keywords:
    similar_words += [word[0] for word in w2v_model.most_similar(keyword, topn=100) if word[1] > 0.7]

# Remove duplicates
similar_words = list(set(similar_words))
print(similar_words)

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    compound_score = sentiment_scores['compound']
    return compound_score

marital_data = []
results = []
processed_tweets = set()
count = 0
positive_count = 0
negative_count = 0
neutral_count = 0

with open('twitter-huge.json', 'r', encoding='utf-8') as f:
    parser = ijson.parse(f)
    is_matching_tweet = False
    for prefix, event, value in parser:
        if prefix.endswith('.tokens') and event == 'string':
            tokens = value.split()  # Split the tokens into individual words
            if any(any(synonym in token.lower() for token in tokens) for synonym in similar_words):
                is_matching_tweet = True
                sentence = value.replace('|', ' ')
                if sentence not in processed_tweets:
                    sentiment_score = analyze_sentiment(sentence)
                    marital_data.append({
                        'tokens': tokens,  # Record the entire token list
                        'sentiment_score': sentiment_score
                    })
                    processed_tweets.add(sentence)
                    count += 1
                    if count > 100:
                        break
                    if sentiment_score > 0:
                        sentiment_category = "Positive"
                        positive_count += 1
                    elif sentiment_score < 0:
                        sentiment_category = "Negative"
                        negative_count += 1
                    else:
                        sentiment_category = "Neutral"
                        neutral_count += 1

                    tweet_data = {
                        "Tweet": sentence,  # Use the entire sentence instead of value
                        "Sentiment_Score": sentiment_score,
                        "Sentiment_Category": sentiment_category
                    }
                    print(tweet_data)
                    results.append(tweet_data)
                    
            else:
                is_matching_tweet = False
        elif is_matching_tweet and prefix.endswith('.tweet.id_str') and event == 'string':
            processed_tweets.add(value)

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
