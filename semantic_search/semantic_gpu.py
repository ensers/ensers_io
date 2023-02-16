# Imports

from haystack.document_stores import PineconeDocumentStore
from haystack.nodes import PreProcessor
from haystack import Document
from haystack.nodes.retriever import EmbeddingRetriever
from haystack.utils import print_answers
from haystack.nodes.answer_generator import RAGenerator
from haystack.pipelines import GenerativeQAPipeline
from haystack import Pipeline
from haystack.nodes import FARMReader
from haystack.pipelines import ExtractiveQAPipeline
# Initializing variables

document_store = PineconeDocumentStore(
    api_key='8b1f9cc1-4214-458e-8f54-2ddacba4f5c9',
    index='semantic',
    environment='us-east1-gcp',
    similarity="cosine",
    embedding_dim=768
)

processor = PreProcessor(
    clean_empty_lines=True,
    clean_whitespace=True,
    clean_header_footer=True,
    split_by="word",
    split_length=200,
    split_respect_sentence_boundary=True,
    split_overlap=20
)

retriever=EmbeddingRetriever(
    document_store=document_store,
    embedding_model='flax-sentence-embeddings/all_datasets_v3_mpnet-base',
    model_format='sentence_transformers',
    use_gpu=False)

# generator = RAGenerator(
#     model_name_or_path="facebook/rag-sequence-nq",
#     retriever=retriever,
#     top_k=1,
#     min_length=2
# )

model = "deepset/roberta-base-squad2"
reader = FARMReader(model, use_gpu=False)

reader_pipeline = ExtractiveQAPipeline(reader, retriever)
# generator_pipeline=GenerativeQAPipeline(generator,retriever)


# def gen_inference(query):
#     result=pipeline.run(
#         query=query,
#         params={
#             'Retriever':{'top_k':10},
#             'Generator': {'top_k':1
#             }
#         }
#     )
# Clean-Up

# document_store.delete_documents(index='semantic')

# document_store.delete_index('semantic')