import pinecone
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()


pinecone.init(api_key='api_key', environment='us-west1-gcp')
pinecone.create_index("rafg-index", dimension=1536, metric="cosine")

embeddings = OpenAIEmbeddings()
vector_store = Pinecone.from_existing_index(index_name='rag-index', embedding=embeddings)
retriever = vector_store.as_retriever()