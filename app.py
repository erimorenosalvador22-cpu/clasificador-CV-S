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
# FUNCIÓN EXPLICACIÓN (XAI)
# -------------------------
def explicar_prediccion(modelo, texto):
    vectorizer = modelo.named_steps['tfidf']
    clf = modelo.named_steps['model']
    
    X = vectorizer.transform([texto])
    
    feature_names = vectorizer.get_feature_names_out()
    coefs = clf.coef_
    
    pred_class = clf.predict(X)[0]
    class_index = list(clf.classes_).index(pred_class)
    
    scores = X.toarray()[0] * coefs[class_index]
    
    top_indices = scores.argsort()[-10:]
    
    palabras = [(feature_names[i], scores[i]) for i in top_indices if scores[i] > 0]
    
    palabras = sorted(palabras, key=lambda x: x[1], reverse=True)
    
    return palabras[:5]

# -------------------------
# UI PRINCIPAL
# -------------------------
st.title("📄 Clasificador Inteligente de CVs")

st.markdown("Sube tu hoja de vida en formato PDF o Word y el sistema la clasificará automáticamente.")

st.divider()

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.title("ℹ️ Información")
st.sidebar.write("""
Modelo: TF-IDF + Logistic Regression  
Incluye balanceo de clases (oversampling)  
Clasificación de perfiles docentes
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
                if page.extract_text():
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

        # RESULTADO
        st.subheader("🎯 Resultado de clasificación")
        st.success(f"Categoría detectada: **{pred[0]}**")

        st.divider()

        # EXPLICACIÓN
        st.subheader("🧠 ¿Por qué esta clasificación?")

        palabras_clave = explicar_prediccion(model, texto)

        if palabras_clave:
            for palabra, peso in palabras_clave:
                st.write(f"🔹 {palabra}")
        else:
            st.write("No se pudieron identificar palabras clave relevantes.")

        st.divider()

        # TEXTO EXTRAÍDO
        st.subheader("📄 Texto extraído del CV")
        st.text_area("", texto, height=200)

    else:
        st.warning("Sube un archivo válido")