import re

from config import OPENAI_API_KEY, PINECONE_API_KEY

from langchain_community.document_loaders import RecursiveUrlLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec

from bs4 import BeautifulSoup

def bs4_body_extractor(html: str) -> str:
    soup = BeautifulSoup(html, "lxml")
    body = soup.body
    if not body:
        return ""
    # Get all text inside the body tag
    body_text = body.get_text()
    # Clean up excessive newlines
    return re.sub(r"\n\n+", "\n\n", body_text).strip()

def index():
    # LOAD DOCUMENTS
    loader = RecursiveUrlLoader("https://nutritionsource.hsph.harvard.edu/salt-and-sodium/", max_depth=1, extractor=bs4_body_extractor)
    docs = loader.load()

    # SPLIT DOCUMENTS
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    all_splits = text_splitter.split_documents(docs) # this automatically deals with page content so no need to clean

    # STORE DOCUMENTS
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small", api_key=OPENAI_API_KEY)

    pc = Pinecone(api_key=PINECONE_API_KEY)
    index_name = "mock"

    if not pc.has_index(index_name):
        pc.create_index(
            name=index_name,
            dimension=1536,
            metric="dotproduct", # Supports sparse vector retrieval
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )

    index = pc.Index(index_name)
    vector_store = PineconeVectorStore(index=index, embedding=embeddings)
    vector_store.add_documents(documents=all_splits)

# index()