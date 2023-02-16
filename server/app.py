
import sys
sys.path.append('../semantic_search')
import Load_docs

from flask import Flask, request,json,render_template
from semantic_search  import Load_docs , semantic_gpu
from flask_restful import Resource,Api,reqparse


app=Flask(__name__)
api=Api(app)
parser=reqparse.RequestParser()
parser.add_argument('query',type=string, help='Enter your query here')
parser.add_argument('doc_dir',type=string, help='Enter the document path')
class Home(Resource):
    def get(self):
        return {"response":"Home"},200

class Documents(Resource):
    def post(self):
        try:
            args=parser.parse_args()
            doc_dir=args['doc_dir']
            document=Load_docs.Process_Docs(doc_dir=doc_dir)
            document.get_docs()
            document.process_docs()
            document.write_docs()
            res="Write successfull"
            response = app.response_class(
                response=json.dumps(res),
                status=200,
                mimetype='application/json'
            )
        except Exception as err:
            response = app.response_class(
                response=json.dumps(err),
                status=200,
                mimetype='application/json'
                )
        return response

class Ensers(Resource):
    def get(self):
        return {"response":"Ensers"}
    def post(self):
        args=parser.parse_args()
        query=args['query']
        response=semantic_gpu.reader_pipeline.run(
            query=query,
            params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 3}})
        return response,200

api.add_resource(Home,'/','/home')
api.add_resource(Ensers,'/ensers')
api.add_resource(Documents,'/documents')

if __name__=='__main__':
    app.run(debug=True)