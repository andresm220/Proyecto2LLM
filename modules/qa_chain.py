from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI
from langchain.pydantic_v1 import BaseModel, Field
from typing import Any, Dict, List
from modules.pinecone_manager import PineconeManager

class QAChainConfig(BaseModel):
    arbitrary_types_allowed = True

class QAChain:
    def __init__(self):
        self.pm = PineconeManager()
        
        self.qa = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(
                model_name="gpt-3.5-turbo",
                temperature=0.3,
                streaming=True
            ),
            chain_type="stuff",
            retriever=self.pm.vectorstore.as_retriever(),
            return_source_documents=True,
            verbose=False
        )

    def ask(self, question: str) -> tuple:
        try:
            result = self.qa({"query": question})
            return result["result"], result["source_documents"]
        except Exception as e:
            return f"Error: {str(e)}", []