from modules.pinecone_manager import PineconeManager
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Pinecone as LangchainPinecone
import os


def load_documents():
    loader = DirectoryLoader("data", glob="**/*.pdf")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    return splitter.split_documents(documents)

def ingest_data():
    pm = PineconeManager()
    docs = load_documents()
    
    LangchainPinecone.from_documents(
        documents=docs,
        embedding=pm.embeddings,
        index_name=pm.index_name
    )
    print(f"✅ Se cargaron {len(docs)} chunks al índice {pm.index_name}")

if __name__ == "__main__":
    ingest_data()