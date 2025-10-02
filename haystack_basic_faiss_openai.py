from haystack.document_stores import FAISS
from haystack.nodes import OpenAIAnswerGenerator, EmbeddingRetriever
from haystack.pipelines import GenerativeQAPipeline

document_store = FAISS(document_store_name='faiss_index')
retriever = EmbeddingRetriever(document_store=document_store)
generator = OpenAIAnswerGenerator()

pipeline = GenerativeQAPipeline(generator=generator, retriever=retriever)


