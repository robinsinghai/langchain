import chromadb
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()


client = chromadb.Client()
collection = client.create_collection(name='my_collection')

collection.add(
    documents=['What is RAG?', 'How does retriever work?'],
    ids=['doc1', 'doc2']
)

results = collection.query(query_texts=['What is RAG?'], n_results=1)
print(results)