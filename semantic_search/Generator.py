
from haystack.nodes.answer_generator import RAGenerator
from haystack.pipelines import GenerativeQAPipeline
from semantic_gpu import retriever

generator = RAGenerator(
    model_name_or_path="facebook/rag-sequence-nq",
    retriever=retriever,
    top_k=1,
    min_length=2
)

pipeline=GenerativeQAPipeline(generator,retriever)

result=pipeline.run(
    query=query,
    params={
        'Retriever':{'top_k':10},
        'Generator': {'top_k':1
        }
    }
)