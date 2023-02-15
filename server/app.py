
import sys
sys.path.append('../semantic_search')
import Load_docs

from flask import Flask, request,json
from semantic_search  import Load_docs , semantic_gpu


app=Flask(__name__)

@app.route("/")
def home():
    return "<p> Hello</p>"

@app.route("/process_docs")
def process_docs():
    try:
        document=Load_docs.Process_Docs(doc_dir='../content')
        document.get_docs()
        document.process_docs()
        document.write_docs()
        res="Write successfull"
        response = app.response_class(
            response=json.dumps(res),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        response = app.response_class(
            response=json.dumps(e),
            status=200,
            mimetype='application/json'
            )
    return response

@app.route("/ensers", methods=['GET','POST'])

def querry():
    if request.method== 'POST':
        query=request.data
        response=semantic_gpu.reader_pipeline.run(
            query=query,
            params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 3}})
        return response
    else:
        response={"res":"Enter your query.."}
        return response