from flask import Flask, Response
from flask_cors import CORS
import couchdb
import json
from collections import defaultdict
from flask import jsonify

app = Flask(__name__)
CORS(app)

admin = 'admin'
password = 'password'
url = f'http://{admin}:{password}@172.26.135.144:5984/'

databases = {}
try:
    couch = couchdb.Server(url)
    print("Connected to CouchDB server successfully.")
    db_names = ["sudo_adelaide_city",
                "sudo_brisbane_city",
                "sudo_melbourne_city",
                "sudo_perth_city",
                "sudo_sydney_city",
                "mastodon_au",
                "twitters_marriage_informations",
                "mastodon_au_filtered"]

    for db_name in db_names:
        if db_name not in couch:
            databases[db_name] = couch.create(db_name)
            print(f"Created database '{db_name}'")
        else:
            databases[db_name] = couch[db_name]
            print(f"Database '{db_name}' already exists")

except couchdb.http.ServerError as e:
    print(f"An error occurred while connecting to CouchDB: {e}")


# token = 'JsVc4APP3DMFnOPBzQU-eriGlgG00A9crz_OBpnlyhk'
# # token_2 = '7rflPh_nxRZBIN_ZF8Nh2j9EihC2EgJUBX6dHgornL4'
# harvester_thread = threading.Thread(target=run_harvester, args=("mastodon_au", token, f'https://aus.social/'))
# filter_thread = threading.Thread(target=sentiment_analysis)
#
# # harvester_thread_2 = threading.Thread(target=run_harvester,
# #                                       args=("mastodon_au_blower", token_2, f'https://theblower.au/'))
# # harvester_thread.start()
# # harvester_thread_2.start()
# # filter_thread.start()


# m = Mastodon(
#     api_base_url=f'https://aus.social/',
#     access_token=token
# )
#
#
# class Listener(StreamListener):
#     def on_update(self, status):
#         json_str = json.dumps(status, indent=2, sort_keys=True, default=str)
#         doc_id, doc_rev = databases["mastodon_au"].save(json.loads(json_str))
#         print(f'Document saved with ID: {doc_id} and revision: {doc_rev}')
#
#
# m.stream_public(Listener())


@app.route('/<city>/<sa2_code>')
def show_data(city, sa2_code):
    database_name = f"sudo_{city}_city"
    for doc_id in databases[database_name]:

        if doc_id.startswith('_design/'):
            continue
        doc = databases[database_name].get(doc_id)
        if doc['sa2_code_2021'] == sa2_code:
            male_data_married = {key: value for key, value in doc.items() if
                                 key.startswith('m_') and 'marrd_reg_marrge' in key and not key.startswith('m_tot_')}
            female_data_married = {key: value for key, value in doc.items() if
                                   key.startswith('f_') and 'marrd_reg_marrge' in key and not key.startswith('f_tot_')}
            male_data_de_facto = {key: value for key, value in doc.items() if
                                  key.startswith('m_') and 'married_de_facto' in key and not key.startswith('m_tot_')}
            female_data_de_facto = {key: value for key, value in doc.items() if
                                    key.startswith('f_') and 'married_de_facto' in key and not key.startswith('f_tot_')}
            male_data_not_married = {key: value for key, value in doc.items() if
                                     key.startswith('m_') and 'not_married' in key and not key.startswith('m_tot_')}
            female_data_not_married = {key: value for key, value in doc.items() if
                                       key.startswith('f_') and 'not_married' in key and not key.startswith('f_tot_')}
            people_data_married = {key: value for key, value in doc.items() if
                                   key.startswith('p_') and 'marrd_reg_marrge' in key and not key.startswith('p_tot_')}
            people_data_de_facto = {key: value for key, value in doc.items() if
                                    key.startswith('p_') and 'married_de_facto' in key and not key.startswith('p_tot_')}
            people_data_not_married = {key: value for key, value in doc.items() if
                                       key.startswith('p_') and 'not_married' in key and not key.startswith('p_tot_')}
            results = {
                "male": {
                    "married": male_data_married,
                    "de_facto": male_data_de_facto,
                    "not_married": male_data_not_married,
                },
                "female": {
                    "married": female_data_married,
                    "de_facto": female_data_de_facto,
                    "not_married": female_data_not_married,
                },
                "people": {
                    "married": people_data_married,
                    "de_facto": people_data_de_facto,
                    "not_married": people_data_not_married,
                }

            }
            break
    else:
        return Response(json.dumps({"error": "SA2 code not found"}), mimetype='application/json'), 404

    return Response(json.dumps(results), mimetype='application/json')


@app.route('/<city>/')
def show_city_data(city):
    database_name = f"sudo_{city}_city"
    db = databases[database_name]
    view_result = db.view(f'_design/people/_view/{city}')

    # print(view_result)
    merged_data = defaultdict(int)
    for row in view_result:
        key = row.key
        value = row.value
        merged_data[key] += value

    return Response(json.dumps(dict(merged_data)), mimetype='application/json')


@app.route('/twitter_analysis/')
def show_twitter_data():
    db = databases["twitters_marriage_informations"]
    view_result = db.view("_design/city/_view/city_count", group_level=2)

    cities = ['Melbourne', 'Sydney', 'Brisbane', 'Adelaide', 'Perth']
    result = {city: {'Positive': 0, 'Neutral': 0, 'Negative': 0} for city in cities}
    result['Other_places'] = {'Positive': 0, 'Neutral': 0, 'Negative': 0}

    for row in view_result:
        place = row.key[0]
        sentiment = row.key[1]
        count = row.value
        found = False
        for city in cities:
            if city in place:
                result[city][sentiment] += count
                found = True
                break
        if not found:
            result['Other_places'][sentiment] += count

    return result


@app.route('/mastodon_analysis/')
def show_mastodon_data():
    db = databases["mastodon_au_filtered"]
    view_result = db.view("_design/sentiment/_view/sentiment_category", group_level=1)
    data = {row.key: row.value for row in view_result}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
