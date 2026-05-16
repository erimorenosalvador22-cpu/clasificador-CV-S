# 🧠 Clasificación Automática de Hojas de Vida (CVs) con Inteligencia Artificial

## 📌 Descripción del proyecto

Este proyecto desarrolla un sistema de Inteligencia Artificial para la **clasificación automática de hojas de vida (CVs)** en diferentes áreas profesionales utilizando técnicas de Procesamiento de Lenguaje Natural (NLP).

El objetivo es apoyar procesos de selección en instituciones educativas, reduciendo tiempos y automatizando la preclasificación de candidatos.

---

## 🎯 Problema que resuelve

Actualmente, la revisión de hojas de vida es un proceso manual, lento y sujeto a sesgos humanos.  
Este sistema permite:

- Automatizar la clasificación de CVs en categorías profesionales
- Reducir el tiempo de análisis de documentos
- Estandarizar el proceso de selección
- Facilitar la gestión de perfiles en instituciones educativas

---

## ⚙️ Pipeline del sistema

---

## 📂 Estructura del proyecto
proyecto-ia/
│
├── data/ # Datasets utilizados (Kaggle e institucional)
├── notebooks/ # Desarrollo del modelo en Colab/Jupyter
├── models/ # Modelos entrenados
├── results/ # Métricas y resultados
├── scripts/ # Código modularizado
└── README.md # Documentación del proyecto

---

## 🧹 Preprocesamiento de datos

Se aplicaron las siguientes técnicas de limpieza de texto:

- Conversión a minúsculas
- Eliminación de caracteres especiales y números
- Eliminación de stopwords
- Filtrado de palabras irrelevantes o muy cortas

---

## 🔢 Vectorización

Se utilizó **TF-IDF (Term Frequency - Inverse Document Frequency)** para transformar el texto en representaciones numéricas.

Esto permite:

- Identificar palabras más relevantes
- Reducir ruido en los datos
- Mejorar la capacidad predictiva del modelo

---

## 🤖 Modelo utilizado

Se implementó un modelo de:

- **Regresión Logística (Logistic Regression)**

Razones:

- Buen desempeño en clasificación de texto
- Modelo interpretable
- Eficiente computacionalmente

---

## 📊 Resultados del modelo

- Accuracy aproximado: **94%**
- Validación cruzada: **0.76**
- F1-score balanceado entre clases

Se observó que el modelo presenta buen desempeño general, aunque la validación cruzada muestra un rendimiento más realista frente a datos no vistos.

---

## 📈 Métricas comparativas

| Modelo / Evaluación        | Resultado |
|---------------------------|----------|
| Accuracy inicial          | ~100% (sobreajuste) |
| Modelo ajustado final     | 94% |
| Validación cruzada (5-fold) | 0.76 |

---

## 🧪 Evidencias de robustez

Se realizaron pruebas con datos no vistos para evaluar la capacidad de generalización del modelo, obteniendo resultados consistentes con el entrenamiento.

---

## 🚀 Cómo ejecutar el proyecto

1. Clonar el repositorio
2. Abrir el notebook en Google Colab o Jupyter
3. Ejecutar todas las celdas del pipeline
4. Subir un CV en formato PDF
5. Obtener la predicción automática de la categoría profesional

---

## 🧠 Tecnologías utilizadas

- Python
- Scikit-learn
- Pandas
- NumPy
- TF-IDF Vectorizer
- Google Colab

---

## 📌 Conclusión

Este proyecto demuestra la viabilidad de utilizar técnicas de Machine Learning para automatizar la clasificación de hojas de vida, logrando un sistema funcional, interpretable y aplicable en contextos educativos reales.

---

## 👤 Autor

Proyecto académico de titulación  

---

## 🧹 Preprocesamiento de datos

Se aplicaron las siguientes técnicas de limpieza de texto:

- Conversión a minúsculas
- Eliminación de caracteres especiales y números
- Eliminación de stopwords
- Filtrado de palabras irrelevantes o muy cortas

---

## 🔢 Vectorización

Se utilizó **TF-IDF (Term Frequency - Inverse Document Frequency)** para transformar el texto en representaciones numéricas.

Esto permite:

- Identificar palabras más relevantes
- Reducir ruido en los datos
- Mejorar la capacidad predictiva del modelo

---

## 🤖 Modelo utilizado

Se implementó un modelo de:

- **Regresión Logística (Logistic Regression)**

Razones:

- Buen desempeño en clasificación de texto
- Modelo interpretable
- Eficiente computacionalmente

---

## 📊 Resultados del modelo

- Accuracy aproximado: **94%**
- Validación cruzada: **0.76**
- F1-score balanceado entre clases

Se observó que el modelo presenta buen desempeño general, aunque la validación cruzada muestra un rendimiento más realista frente a datos no vistos.

---

## 📈 Métricas comparativas

| Modelo / Evaluación        | Resultado |
|---------------------------|----------|
| Accuracy inicial          | ~100% (sobreajuste) |
| Modelo ajustado final     | 94% |
| Validación cruzada (5-fold) | 0.76 |

---

## 🧪 Evidencias de robustez

Se realizaron pruebas con datos no vistos para evaluar la capacidad de generalización del modelo, obteniendo resultados consistentes con el entrenamiento.

---

## 🚀 Cómo ejecutar el proyecto

1. Clonar el repositorio
2. Abrir el notebook en Google Colab o Jupyter
3. Ejecutar todas las celdas del pipeline
4. Subir un CV en formato PDF
5. Obtener la predicción automática de la categoría profesional

---

## 🧠 Tecnologías utilizadas

- Python
- Scikit-learn
- Pandas
- NumPy
- TF-IDF Vectorizer
- Google Colab

---

## 📌 Conclusión

Este proyecto demuestra la viabilidad de utilizar técnicas de Machine Learning para automatizar la clasificación de hojas de vida, logrando un sistema funcional, interpretable y aplicable en contextos educativos reales.

---

## 👤 Erika Moreno

Proyecto académico de titulación  

El flujo del modelo es el siguiente:
