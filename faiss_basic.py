from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

documents = ["RAG is a hybrid AI architecture.", "FAISS is great for similarity search."]

embeddings = OpenAIEmbeddings()
vector_store = FAISS.from_texts(documents, embedding=embeddings)
retriever = vector_store.as_retriever()


query = "what is rag?"
retrived_docs = retriever.get_relevant_documents(query)
print(retrived_docs)