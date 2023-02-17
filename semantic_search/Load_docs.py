
from dataclasses import dataclass,field
from .semantic_gpu import processor
from .semantic_gpu import retriever
from .semantic_gpu import document_store
from haystack.utils import convert_files_to_docs,clean_wiki_text

@dataclass
class Process_Docs:
   processor:  processor =processor
   doc_dir: str = field(default_factory=str)
   all_docs: list = field(default_factory=list)
   data_json: list = field(default_factory=list)
   docs: list = field(default_factory=list)

   def get_docs(self):
        self.all_docs = convert_files_to_docs(dir_path=self.doc_dir,clean_func=clean_wiki_text, split_paragraphs=True)
        return self.all_docs
   
   def process_docs(self):
        for doc in self.all_docs:
          doc.content=doc.content.replace('\n',' ').replace('\x0c','')
        self.docs=processor.process(self.all_docs)
        return self.docs
   
   def write_docs(self):
    document_store.write_documents(self.docs) 
    document_store.update_embeddings(retriever)
   
# def main():
#     document=Process_Docs(doc_dir='../content')
#     document.get_docs()
#     print(str(document.process_docs()))
    
    

# if __name__=='__main__':
#     main()