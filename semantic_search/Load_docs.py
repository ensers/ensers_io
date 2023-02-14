from dataclasses import dataclass,field
from semantic_gpu import processor
from semantic_gpu import retriever
from semantic_gpu import document_store
from haystack.utils import convert_files_to_docs

@dataclass
class Process_Docs:
   processor:  processor
   doc_dir: str
   all_docs: list = field(default_factory=list)
   data_json: list = field(default_factory=list)
   docs: list = field(default_factory=list)

   def get_docs(self):
        self.all_docs = convert_files_to_docs(dir_path=self.doc_dir)
        return self.all_docs
   
   def process_docs(self):
        self.data_json=[
            {
                'content':doc.content.replace('\n',' ').replace('\x0c',''),
                'meta':{'name':doc.meta}
        } for doc in self.all_docs
        ]
        self.docs=processor.process(self.data_json)
        return self.docs
   
   def write_docs(self):
    document_store.write_documents(self.docs) 
    document_store.update_embeddings(
    retriever,
    batch_size=256
    )
   
def main():
    document=Process_Docs(processor=processor, doc_dir='../content')
    document.get_docs()
    print(str(document.process_docs()))

if __name__=='__main__':
    main()