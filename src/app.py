import os.path
import flask
import elasticsearch
import json

app = flask.Flask(__name__, static_url_path='')
es = elasticsearch.Elasticsearch()

@app.route('/')
def search():
    with open('src/templates/search.html') as fileobj:
      return fileobj.read()  # app.send_static_file('search.html')

@app.route('/api/v1/search')
def search_api():
    query = {
        "query" : {
            "query_string" : {
                "query" : flask.request.args.get('q')
            }
        },
        "aggregations" : {
            "significantWords" : {
                "significant_terms" : { "field" : "text" }
            }
        },
        "highlight" : {
            "fields" : {
                "text" : {}
            }
        }
    }
    results = es.search(
        index='mps',
        doc_type='report',
        body=query)
    return json.dumps(results)

if __name__ == '__main__':
    app.run(debug=True)
