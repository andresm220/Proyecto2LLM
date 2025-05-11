import streamlit as st
from modules.qa_chain import QAChain
from modules.utils import process_uploaded_files
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="Asistente Técnico", layout="wide")
st.title("📄🤖 Asistente con Carga de Documentos")

@st.cache_resource
def load_qa_chain():
    return QAChain()

qa_chain = load_qa_chain()

with st.expander("📤 Subir nuevos documentos", expanded=True):
    uploaded_files = st.file_uploader(
        "Arrastra aquí tus archivos (PDF, TXT, DOCX)",
        type=["pdf", "txt", "docx"],
        accept_multiple_files=True
    )

    if st.button("Procesar documentos") and uploaded_files:
        with st.spinner("Procesando documentos..."):
            docs = process_uploaded_files(uploaded_files)
            
            if len(docs) < 70:
                st.warning(f"⚠️ Debes cargar al menos 70 fragmentos. Actuales: {len(docs)}")
            else:
                qa_chain.pm.vectorstore.add_documents(docs)
                st.success(f"✅ {len(docs)} fragmentos cargados exitosamente!")

st.divider()
question = st.text_input("Escribe tu pregunta técnica:")

if st.button("Consultar") and question:
    try:
        with st.spinner("Buscando respuesta..."):
            answer, contexts = qa_chain.ask(question)
            
            st.subheader("Respuesta")
            st.write(answer)

            with st.expander("📚 Contextos utilizados"):
                for i, context in enumerate(contexts, 1):
                    st.markdown(f"**Fragmento {i}**")
                    st.write(context.page_content)
                    st.divider()
                    
        st.sidebar.markdown(f"**Fragmentos cargados:** {qa_chain.pm.get_index_stats()['total_vector_count']}")
        
    except Exception as e:
        st.error(f"🚨 Error: {str(e)}")