from haystack.nodes import FARMReader
from haystack.pipelines import ExtractiveQAPipeline
from semantic_gpu import retriever

model = "deepset/roberta-base-squad2"
reader = FARMReader(model, use_gpu=False)

pipe = ExtractiveQAPipeline(reader, retriever)

def inference(query: str):
    prediction = pipe.run(
        query=query,
        params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 3}}
    )
    return prediction

pred=inference('querry')

print(pred)