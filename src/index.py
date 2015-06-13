import os
import json
import elasticsearch

client = elasticsearch.Elasticsearch()

extract_dir = './archive/text/'

for filename in os.listdir(extract_dir):
    with open(os.path.join(extract_dir, filename)) as text_file:
        text = text_file.read()
        doc = {
          'text': text
        }
        client.index(index='mps', doc_type='report', body=doc)
