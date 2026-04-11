import streamlit as st
import pickle
import pdfplumber
from docx import Document
import os

# -------------------------
# CARGAR MODELO
# -------------------------
model_path = os.path.join(os.path.dirname(__file__), "modelo.pkl")
model = pickle.load(open(model_path, "rb"))

# -------------------------
# TÍTULO Y DESCRIPCIÓN
# -------------------------
st.title("📄 Clasificador Inteligente de CVs")

st.markdown("Sube tu hoja de vida en PDF o Word y el sistema la clasificará automáticamente.")

st.divider()

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.title("ℹ️ Información")
st.sidebar.write("""
Modelo: TF-IDF + Logistic Regression  
Proyecto de clasificación de perfiles docentes
""")

# -------------------------
# SUBIDA DE ARCHIVO
# -------------------------
archivo = st.file_uploader("📂 Sube tu CV", type=["pdf", "docx"])

texto = ""

if archivo is None:
    st.info("Por favor sube un archivo PDF o Word para comenzar.")

# -------------------------
# EXTRACCIÓN DE TEXTO
# -------------------------
if archivo is not None:

    if archivo.type == "application/pdf":
        with pdfplumber.open(archivo) as pdf:
            for page in pdf.pages:
                texto += page.extract_text()

    elif archivo.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = Document(archivo)
        for para in doc.paragraphs:
            texto += para.text

# -------------------------
# BOTÓN Y RESULTADO
# -------------------------
if st.button("Clasificar"):

    if texto:
        with st.spinner("Analizando CV..."):
            pred = model.predict([texto])

        st.subheader("Resultado de clasificación")
        st.success(f"🎯 Categoría detectada: **{pred[0]}**")

        st.divider()

        st.subheader("Texto extraído del CV")
        st.text_area("", texto, height=200)

    else:
        st.warning("Sube un archivo válido")