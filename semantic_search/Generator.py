



pipeline=GenerativeQAPipeline(generator,retriever)

def gen_inference(query):
    result=pipeline.run(
        query=query,
        params={
            'Retriever':{'top_k':10},
            'Generator': {'top_k':1
            }
        }
    )