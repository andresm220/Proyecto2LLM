from langchain_community.document_loaders import PyPDFLoader, TextLoader, UnstructuredWordDocumentLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from tempfile import NamedTemporaryFile
import os
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

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
                # Detectar codificación automáticamente
                encoding = detect_encoding(temp_path)
                loader = TextLoader(temp_path, encoding=encoding)
            elif file.type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
                loader = UnstructuredWordDocumentLoader(temp_path)
            else:
                continue

            docs = loader.load()
            docs = splitter.split_documents(docs)
            documents.extend(docs)

        except UnicodeDecodeError:
            st.error(f"Error de codificación en el archivo {file.name}. Usa formato UTF-8.")
        except Exception as e:
            st.error(f"Error procesando {file.name}: {str(e)}")
        finally:
            os.unlink(temp_path)

    return documents