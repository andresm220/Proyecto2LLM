from langchain_community.document_loaders import PyPDFLoader, TextLoader, UnstructuredWordDocumentLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from tempfile import NamedTemporaryFile
import os


def process_uploaded_files(uploaded_files):
    documents = []
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    for file in uploaded_files:
        with NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.name)[1]) as temp_file:
            temp_file.write(file.getbuffer())
            temp_path = temp_file.name

        try:
            if file.type == "application/pdf":
                loader = PyPDFLoader(temp_path)
            elif file.type == "text/plain":
                loader = TextLoader(temp_path)
            elif file.type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
                loader = UnstructuredWordDocumentLoader(temp_path)
            else:
                continue

            docs = loader.load()
            docs = splitter.split_documents(docs)
            documents.extend(docs)

        finally:
            os.unlink(temp_path)

    return documents