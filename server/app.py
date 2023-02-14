
import sys
sys.path.append('../semantic_search')
import Load_docs

from flask import Flask, request
from semantic_search  import Load_docs , semantic_gpu


app=Flask(__name__)

@app.route("/")
def home():
    return "<p> Hello</p>"

@app.route("/process_docs")
def process_docs():
    document=Load_docs.Process_Docs(doc_dir='../content')
    document.get_docs()
    res=document.process_docs()
    return res

@app.route("/querry", methods=['GET','POST'])
def querry(request):
    if request.method== 'POST':
        query=request.args.get('key', '')
        response=semantic_gpu.pipe.run(
            query=query,
            params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 3}})
        return query
    else:
        return "<p> Paste your querry </p>"