import couchdb
import json
from mastodon import Mastodon, StreamListener


def run_harvester():
    print("harvester running")
    admin = 'admin'
    password = 'password'
    url = f'http://{admin}:{password}@172.26.135.144:5984/'
    database_name = "mastodon_au"

    try:
        couch = couchdb.Server(url)

        if database_name not in couch:
            db = couch.create(database_name)
            print(f"Created database '{database_name}'")
        else:
            db = couch[database_name]
            print(f"Database '{database_name}' already exists")

    except couchdb.http.ServerError as e:
        print(f"An error occurred while harvester connecting to CouchDB: {e}")

    m = Mastodon(
        api_base_url=f'https://aus.social/',
        access_token='JsVc4APP3DMFnOPBzQU-eriGlgG00A9crz_OBpnlyhk',
    )

    print(m.api_base_url)
    print(m.access_token)

    class Listener(StreamListener):
        def on_update(self, status):
            json_str = json.dumps(status, indent=2, sort_keys=True, default=str)
            doc_id, doc_rev = db.save(json.loads(json_str))
            print(f'Document saved with ID: {doc_id} and revision: {doc_rev}')

    m.stream_public(Listener())


if __name__ == '__main__':
    run_harvester()
