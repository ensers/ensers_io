# Imports

from haystack.document_stores import PineconeDocumentStore
from haystack.utils import convert_files_to_docs
from haystack.nodes import PreProcessor
from haystack import Document
from haystack.nodes.retriever import EmbeddingRetriever
from haystack.utils import print_answers

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



def preprocess_docs(processor,path='./content'):
    doc_dir=path
    all_docs = convert_files_to_docs(dir_path=doc_dir)

    # Pre-processing
    data_json=[
        {
            'content':doc.content.replace('\n',' ').replace('\x0c',''),
            'meta':{'name':doc.meta}
    } for doc in all_docs
    ]
    docs=processor.process(data_json)
    return docs

def process_docs(docs):
    document_store.write_documents(docs) 
    document_store.update_embeddings(
    retriever,
    batch_size=256
    )

# Writing documents to document store



# Embedding documents in the document store




# Clean-Up

# document_store.delete_documents(index='semantic')

# document_store.delete_index('semantic')