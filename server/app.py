
import sys
sys.path.append('../semantic_search')
import Load_docs

from flask import Flask, request
from semantic_search  import Load_docs

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
def querry():
    if request.method== 'POST':
        pass
    else:
        return "<p> Paste your querry </p>"