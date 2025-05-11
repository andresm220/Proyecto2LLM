# 📚🤖 Asistente Técnico con Búsqueda Semántica

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32%2B-FF4B4B)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT_3.5-412991)

Una aplicación web inteligente que responde preguntas técnicas usando IA, buscando en documentos cargados por el usuario. ¡Convierte tus archivos en conocimiento accionable!

<p align="center">
    <img src="https://img.icons8.com/clouds/300/000000/document.png" width="200">
</p>

---

## 🚀 Características principales

- **Carga múltiple de documentos** (PDF, TXT, DOCX)
- **Búsqueda semántica** con Pinecone 🍍
- **Respuestas contextuales** usando GPT-3.5
- **Interfaz intuitiva** con Streamlit
- **Auto-instalación** con script para Windows

---

## 📦 Requisitos previos

- Windows 10/11
- Python 3.10+
- Cuentas en [OpenAI](https://platform.openai.com/) y [Pinecone](https://www.pinecone.io/)

---

## 🛠️ Instalación en 1 clic

1. Descarga el proyecto.
2. Coloca tus documentos en la carpeta `data` (opcional).
3. **Doble click en `run.bat`**  
     *¡El script hará todo por ti!*


---

## 🖥️ Uso manual

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Cargar documentos iniciales (opcional)
python ingest.py

# 3. Iniciar aplicación
streamlit run main.py
```

---

## 📂 Estructura del proyecto

```
.
├── data/                   # Documentos base (opcional)
├── modules/
│   ├── pinecone_manager.py # Conexión con Pinecone
│   ├── qa_chain.py         # Lógica de preguntas/respuestas
│   └── utils.py            # Procesamiento de archivos
├── main.py                 # Interfaz principal
├── run.bat                 # Instalador automático
└── requirements.txt        # Dependencias
```

---

## 🛠️ Tecnologías utilizadas

- **Lenguaje:** Python 3.10
- **Framework:** Streamlit
- **IA:** OpenAI (GPT-3.5, Embeddings)
- **Base de datos:** Pinecone
- **Procesamiento:** LangChain, Unstructured

---

## 🆘 Soporte técnico

### Problema: Problemas de codificación en archivos TXT
**Solución:** Guarda tus documentos en formato UTF-8.  
[Tutorial para guardar en UTF-8](https://www.wikihow.com/Change-a-File-to-UTF-8-Encoding)

### Problema: Claves API no detectadas
**Verifica:**
- Que el archivo `.env` esté creado correctamente.
- Que incluya las siguientes variables:

```env
PINECONE_API_KEY=tu_clave_pinecone
OPENAI_API_KEY=tu_clave_openai
```

---

¡Listo! Ahora puedes transformar tus documentos en conocimiento accionable con IA. 🚀