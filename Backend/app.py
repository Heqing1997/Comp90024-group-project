from flask import Flask, Response
import couchdb
import json


app = Flask(__name__)

admin = 'admin'
password = 'password'
url = f'http://{admin}:{password}@172.26.135.144:5984/'

databases = {}
try:
    couch = couchdb.Server(url)
    print("Connected to CouchDB server successfully.")
    db_names = ["sudo_adelaide_city",
                "sudo_brisbane_inner",
                "sudo_melbourne_city",
                "sudo_perth_city",
                "sudo_sydney_inner_city"]

    for db_name in db_names:
        if db_name not in couch:
            databases[db_name] = couch.create(db_name)
            print(f"Created database '{db_name}'")
        else:
            databases[db_name] = couch[db_name]
            print(f"Database '{db_name}' already exists")

except couchdb.http.ServerError as e:
    print(f"An error occurred while connecting to CouchDB: {e}")


@app.route('/adelaide/male-registered-marriage/<sa2_code>')
def show_data(sa2_code):
    results = []

    for doc_id in databases["sudo_adelaide_city"]:
        doc = databases["sudo_adelaide_city"].get(doc_id)
        if doc['sa2_code_2021'] == sa2_code:  # 匹配sa2_code
            male_data = {key: value for key, value in doc.items() if key.startswith('m_') and 'marrd_reg_marrge' in key and not key.startswith('m_tot_')}
            sorted_male_data = dict(sorted(male_data.items(), key=lambda x: x[0]))
            results.append(sorted_male_data)
            break
    else:
        return Response(json.dumps({"error": "SA2 code not found"}), mimetype='application/json'), 404

    return Response(json.dumps(results), mimetype='application/json')



if __name__ == '__main__':
    app.run(debug=True)
