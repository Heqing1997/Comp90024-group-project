import couchdb
import json

admin = 'admin'
password = 'password'
url = f'http://{admin}:{password}@172.26.135.144:5984/'

couch = couchdb.Server(url)

db_name = 'mastodon'

if db_name not in couch:
    db = couch.create(db_name)
else:
    db = couch[db_name]

token = 'QrElmW9xkXg-oE9gSmHGnGyZNxYcclquesUhKw7hUKE'
m = Mastodon(
    api_base_url= f'mastodon.social',
    access_token= token
)

class Listener(StreamListener):
    def on_update(self, status):
        json_str = json.dumps(status,indent=2,sort_keys=True,default=str)
        doc_id,doc_rev = db.save(json.loads(json_str))
        print(f'Document saved with ID: {doc_id} and revision: {doc_rev}')

m.stream_public(Listener())