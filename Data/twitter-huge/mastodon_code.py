import couchdb
import json
import nltk
from nltk.corpus import wordnet
from mastodon import Mastodon, StreamListener

# authentication
admin = 'admin'
password = 'password'
url = f'http://{admin}:{password}@172.26.135.144:5984/'

# get couchdb instance
couch = couchdb.Server(url)

# indicate the db name
db_name = 'mastodon_test'

# if not exist, create one
if db_name not in couch:
    db = couch.create(db_name)
else:
    db = couch[db_name]


token = 'fOKxh4ae_FNTnU1EuIVF2E_7jwXVzEsVoknCeWjE2mc'
m = Mastodon(
    api_base_url = f'https://mastodon.social/',
    access_token = token
)

def get_synonyms(words, languages):
    synonyms = []
    for word in words:
        for language in languages:
            synsets = wordnet.synsets(word, lang=language)
            for syn in synsets:
                for lemma in syn.lemmas(lang=language):
                    synonyms.append(lemma.name())
    return synonyms

# listen to the timeline
class Listener(StreamListener):
    def __init__(self):
        self.keywords = ["married", "de facto", "divorced", "separated", "widowed", "never married"]
        languages = ['eng', 'als', 'arb', 'bul', 'cmn', 'dan', 'ell', 'fin', 'fra', 'heb', 'hrv', 'isl', 'ita',
                     'ita_iwn', 'jpn', 'cat', 'eus', 'glg', 'spa', 'ind', 'zsm', 'nld', 'nno', 'nob', 'pol', 'por',
                     'ron', 'lit', 'slk', 'slv', 'swe', 'tha']
        self.synonyms = get_synonyms(self.keywords, languages)
        print(self.synonyms)

    # called when receiving new post or status update
    def on_update(self, status):
        text = status['content']  # 获取推文的内容
        # 检查文本是否包含关键词或其同义词
        if any(keyword in text.lower() for keyword in self.keywords) or any(synonym in text.lower() for synonym in self.synonyms):
            json_str = json.dumps(status, indent = 2, sort_keys = True, default = str)
            doc_id,doc_rev = db.save(json.loads(json_str))
            print(f'Document saved with ID: {doc_id} and revision: {doc_rev}')

# 创建监听器实例
listener = Listener()

# 启动实时流监听
# make it better with try-catch and error-handling
m.stream_public(listener)
