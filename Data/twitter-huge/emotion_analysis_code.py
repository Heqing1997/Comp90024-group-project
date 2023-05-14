#### emotion analysis -- pos/neg/neu
import json
import ijson
import gensim.downloader as api
import nltk
from nltk.corpus import wordnet
from nltk.sentiment import SentimentIntensityAnalyzer

# Load pre-trained Word2Vec model
w2v_model = api.load('fasttext-wiki-news-subwords-300')

# Define keywords
keywords = ["married", "defacto", "divorced", "separated", "widowed", "unmarried"]

# Get similar words to each keyword and concatenate them
similar_words = []
for keyword in keywords:
    similar_words += [word[0] for word in w2v_model.most_similar(keyword)]

# Remove duplicates and print the resulting list
similar_words = list(set(similar_words))

def get_synonyms(words, languages):
    synonyms = []
    for word in words:
        for language in languages:
            synsets = wordnet.synsets(word, lang=language)
            for syn in synsets:
                for lemma in syn.lemmas(lang=language):
                    synonyms.append(lemma.name())
    return synonyms

languages = nltk.corpus.wordnet.langs()
synonyms = get_synonyms(similar_words, languages)

# Remove duplicates and print the resulting list
synonyms = list(set(synonyms))
synonyms += list(set(similar_words) - set(synonyms))
print(synonyms)

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
            tokens = value
            if any(synonym in value.lower() for synonym in synonyms):
                is_matching_tweet = True
                sentence = value.replace('|', ' ')
                if sentence not in processed_tweets:
                    sentiment_score = analyze_sentiment(sentence)
                    marital_data.append({
                        'sentence': sentence,
                        'sentiment_score': sentiment_score
                    })
                    processed_tweets.add(sentence)
                    count += 1

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
                        "Tweet": value.replace('|', ' '),
                        "Sentiment Score": sentiment_score,
                        "Sentiment Category": sentiment_category
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
