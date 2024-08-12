from flask import Flask, render_template, request, redirect, url_for
from es_connection import client

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')

    search_query = request.form.get('query')
    return redirect(url_for("results", sq=search_query))

@app.route('/results/<sq>')
def results(sq):
    query = {
        'query': {
            'multi_match': {
                'query': sq,
                "fields": [
                    "title^2",
                    "authors",
                    "url"
                ],
                "type": "phrase"
            }
        }
    }

        # search for documents
    result = client.search(index='academic', body=query, _source_includes=['url', 'title', 'authors'])
    #print(result['hits']['hits'][0]['_source'])
    optimised_result= [d['_source'] for d in result['hits']['hits']]
    return render_template("results.html", res_list=optimised_result)

if __name__ == "__main__":
    app.run(debug=True, port = 8000, host = "0.0.0.0")