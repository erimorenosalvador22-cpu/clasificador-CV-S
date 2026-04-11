import streamlit as st
import pickle
import pdfplumber
from docx import Document

# cargar modelo
model = pickle.load(open("modelo.pkl", "rb"))

st.title("Clasificador de CVs")

# subir archivo
archivo = st.file_uploader("Sube tu CV (PDF o Word)", type=["pdf", "docx"])

texto = ""

# leer PDF
if archivo is not None:
    if archivo.type == "application/pdf":
        with pdfplumber.open(archivo) as pdf:
            for page in pdf.pages:
                texto += page.extract_text()

    # leer Word
    elif archivo.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = Document(archivo)
        for para in doc.paragraphs:
            texto += para.text

# botón
if st.button("Clasificar"):
    if texto:
        pred = model.predict([texto])
        st.success(f"Categoría: {pred[0]}")
    else:
        st.warning("Sube un archivo válido")