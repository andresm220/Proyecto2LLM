import streamlit as st
from modules.qa_chain import QAChain
from modules.utils import process_uploaded_files
from dotenv import load_dotenv
import os

load_dotenv()

# Configuración de la página
st.set_page_config(page_title="Asistente Técnico", layout="wide")
st.title("📄🤖 Asistente con Carga de Documentos")


# Inicializar QAChain
@st.cache_resource
def load_qa_chain():
    return QAChain()


qa_chain = load_qa_chain()

# Sección para subir documentos
with st.expander("📤 Subir nuevos documentos", expanded=True):
    uploaded_files = st.file_uploader(
        "Arrastra aquí tus archivos (PDF, TXT, DOCX)",
        type=["pdf", "txt", "docx"],
        accept_multiple_files=True
    )

    if st.button("Procesar documentos") and uploaded_files:
        with st.spinner("Procesando documentos..."):
            docs = process_uploaded_files(uploaded_files)
            qa_chain.vectorstore.add_documents(docs)
            st.success(f"✅ {len(docs)} fragmentos cargados exitosamente!")

# Sección de preguntas
st.divider()
question = st.text_input("Escribe tu pregunta técnica:")
if st.button("Consultar") and question:
    with st.spinner("Buscando respuesta..."):
        result = qa_chain.ask(question)

        st.subheader("Respuesta")
        st.write(result["answer"])

        with st.expander("📚 Contextos utilizados"):
            for i, context in enumerate(result["contexts"], 1):
                st.markdown(f"**Fragmento {i}**")
                st.write(context)
                st.divider()