import os
from pinecone import Pinecone, ServerlessSpec
from langchain_community.vectorstores import Pinecone as LangchainPinecone
from langchain_community.embeddings import OpenAIEmbeddings


class PineconeManager:
    def __init__(self):
        # Configuración 100% compatible
        self.pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        self.index_name = "tranquil-redwood"
        self.embeddings = OpenAIEmbeddings()

        # Crea el índice si no existe
        if self.index_name not in self.pc.list_indexes().names():
            self.pc.create_index(
                name=self.index_name,
                dimension=1536,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1")
            )

    @property
    def vectorstore(self):
        """Versión QUE SÍ FUNCIONA con LangChain"""
        index = self.pc.Index(self.index_name)
        return LangchainPinecone(
            index=index,
            embedding=self.embeddings,
            text_key="text"
        )