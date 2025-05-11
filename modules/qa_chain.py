from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from .pinecone_manager import PineconeManager
from pydantic import BaseModel, Field
from typing import Any, Dict, List, Optional


# Configuración para evitar el error de validación
class QAConfig(BaseModel):
    arbitrary_types_allowed = True


class QAChain:
    def __init__(self):
        # Configura el manejador de Pinecone
        self.pm = PineconeManager()

        # Configuración segura del QA chain
        self.qa = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(
                model_name="gpt-3.5-turbo",
                temperature=0.3,
                streaming=True,
                callbacks=None  # Desactiva callbacks temporalmente
            ),
            chain_type="stuff",
            retriever=self.pm.vectorstore.as_retriever(),
            return_source_documents=True,
            verbose=False
        )

    def ask(self, question: str) -> tuple[str, List[Any]]:
        """Método seguro para realizar preguntas"""
        try:
            result = self.qa.run({"query": question})
            return result["result"], result.get("source_documents", [])
        except Exception as e:
            return f"Error: {str(e)}", []