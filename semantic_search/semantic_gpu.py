# Imports

from haystack.document_stores import PineconeDocumentStore
from haystack.nodes import PreProcessor,Shaper, PromptNode, PromptTemplate
from haystack import Document
from haystack.nodes import DensePassageRetriever
from haystack.utils import print_answers
# from haystack.nodes.answer_generator import RAGenerator
# from haystack.pipelines import GenerativeQAPipeline
from haystack import Pipeline
from haystack.nodes import FARMReader
from haystack.pipelines import ExtractiveQAPipeline
# from haystack.nodes import Seq2SeqGenerator
from haystack.pipelines import Pipeline

# Initializing variables

document_store = PineconeDocumentStore(
    api_key='',
    index='semantic',
    environment='us-east1-gcp',
    similarity="dot_product",
    embedding_dim=128
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

retriever = DensePassageRetriever(
    document_store=document_store,
    query_embedding_model="vblagoje/dpr-question_encoder-single-lfqa-wiki",
    passage_embedding_model="vblagoje/dpr-ctx_encoder-single-lfqa-wiki",
)

generator = OpenAIAnswerGenerator(api_key='',
                                  model="text-davinci-003",
                                  max_tokens=100,
                                  presence_penalty=0.1,
                                  frequency_penalty=0.1,
                                  top_k=3,
                                  temperature=0.9,
                                  )

# model = "deepset/roberta-base-squad2"
# reader = FARMReader(model, use_gpu=True)

# reader_pipeline = ExtractiveQAPipeline(reader, retriever)
pipeline=GenerativeQAPipeline(generator=generator,retriever=retriever)


