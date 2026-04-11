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
# explicación
st.subheader("🧠 ¿Por qué esta clasificación?")

palabras_clave = explicar_prediccion(model, texto)

for palabra, peso in palabras_clave:
    st.write(f"🔹 {palabra}")