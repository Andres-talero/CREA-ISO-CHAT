import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.azuresearch import AzureSearch
from dotenv import load_dotenv

load_dotenv()


embeddings: OpenAIEmbeddings = OpenAIEmbeddings(
    deployment="embedding", chunk_size=1
)

vector_store_address = f"https://{os.environ.get('AZURE_COGNITIVE_SEARCH_SERVICE_NAME')}.search.windows.net"

vector_store: AzureSearch = AzureSearch(
    azure_search_endpoint=vector_store_address,
    azure_search_key=os.environ.get("AZURE_COGNITIVE_SEARCH_API_KEY"),
    index_name=os.environ.get("AZURE_COGNITIVE_SEARCH_INDEX_NAME"),
    embedding_function=embeddings.embed_query,
)


def vector_search(question):
    docs = vector_store.similarity_search(
        query=question,
        k=5,
        search_type="hybrid",
    )
    return docs


def search(question):
    output = vector_search(question)
    return output
