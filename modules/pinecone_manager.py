import os
from pinecone import Pinecone, ServerlessSpec
from langchain_community.vectorstores import Pinecone as LangchainPinecone
from langchain_openai import OpenAIEmbeddings  # Importación corregida
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno

class PineconeManager:
    def __init__(self):
        # Configuración de Pinecone
        self.pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        self.index_name = "tranquil-redwood"
        
        # Configuración actualizada de embeddings
        self.embeddings = OpenAIEmbeddings(
            model="text-embedding-3-small",
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )

        # Crear índice si no existe
        if self.index_name not in self.pc.list_indexes().names():
            self.pc.create_index(
                name=self.index_name,
                dimension=1536,  # Dimensión compatible con el modelo
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1")
            )

    @property
    def vectorstore(self):
        """Versión compatible con LangChain"""
        index = self.pc.Index(self.index_name)
        return LangchainPinecone(
            index=index,
            embedding=self.embeddings,
            text_key="text"
        )
    
    def get_index_stats(self):
        """Obtiene estadísticas del índice"""
        return self.pc.Index(self.index_name).describe_index_stats()