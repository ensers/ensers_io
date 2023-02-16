
import sys
sys.path.append('../')
# # # import Load_docs

from flask import Flask, request,json,render_template,jsonify,make_response
from semantic_search import Load_docs , semantic_gpu
from flask_restful import Resource,Api,reqparse


app=Flask(__name__)
api=Api(app)
parser=reqparse.RequestParser()
parser.add_argument('query')
parser.add_argument('task',location='values')
parser.add_argument('doc_dir',type=str, help='Enter the document path')

TODOS = {
}
def getanswers(query):
    response={}
    res=semantic_gpu.reader_pipeline.run(
            query=query,
            params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 3}})
    response=res['answers'][0].answer
    return {"response":response}

def generate_answer(query):
    result=semantic_gpu.generator_pipeline.run(
        query=query,
        params={
            'Retriever':{'top_k':10},
            'Generator': {'top_k':1
            }
        }
    )
    answer=result['answers'][0].answer
    return {"answer":answer}


class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201
    
class Home(Resource):
    def get(self):
        return {"response":"Home"},200

class Documents(Resource):

    def get(self):
        return {"Response":"Docs"}
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
        req_query=args["query"]
        res=getanswers(req_query)
        return res,200

api.add_resource(Home,'/','/home')
api.add_resource(Ensers,'/ensers')
api.add_resource(Documents,'/documents')
api.add_resource(TodoList, '/todos')

if __name__=='__main__':
    app.run(debug=True)