from flask import Flask, request


app=Flask(__name__)

@app.route("/")
def home():
    return "<p> Hello</p>"

@app.route("/querry", methods=['GET','POST'])
def querry():
    if request.method== 'POST':
        pass
    else:
        return "<p> Paste your querry </p>"