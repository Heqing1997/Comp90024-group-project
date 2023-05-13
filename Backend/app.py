from flask import Flask, Response
from flask_cors import CORS
import couchdb
import json

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
                "sudo_sydney_city"]

    for db_name in db_names:
        if db_name not in couch:
            databases[db_name] = couch.create(db_name)
            print(f"Created database '{db_name}'")
        else:
            databases[db_name] = couch[db_name]
            print(f"Database '{db_name}' already exists")

except couchdb.http.ServerError as e:
    print(f"An error occurred while connecting to CouchDB: {e}")


@app.route('/<city>/<sa2_code>')
def show_data(city,sa2_code):
    database_name = f"sudo_{city}_city"
    for doc_id in databases[database_name]:
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


if __name__ == '__main__':
    app.run(debug=True)
