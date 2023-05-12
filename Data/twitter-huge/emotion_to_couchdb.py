import couchdb
import json

# authentication
admin = 'admin'
password = 'password'

# CouchDB server URL
server_url = f'http://{admin}:{password}@172.26.135.144:5984/'

# Connect to CouchDB server
couch = couchdb.Server(server_url)

# indicate the db name
db_name = 'emotion_analysis'

# if not exist, create one
if db_name not in couch:
    db = couch.create(db_name)
else:
    db = couch[db_name]

# Specify the path and filename of the JSON file
json_file_path = 'E:\Desktop\emotion_analysis.json'

# Open the JSON file and load the data
with open(json_file_path, 'r') as json_file:
    content = json.load(json_file)

# Import the JSON data to CouchDB
for index, data in enumerate(content):
    doc_id, doc_rev = db.save(data)
    print(f'Document {index + 1} saved with ID: {doc_id} and revision: {doc_rev}')

# basic query all the docs
for _id in db:
    doc = db.get(_id)
    # filter and do something
    print(f"ID: {_id}, Rev: {doc['_rev']}")

