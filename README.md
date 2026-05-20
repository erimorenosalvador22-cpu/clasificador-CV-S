Clasificación Automática de Hojas de Vida con NLP y Machine Learning
Descripción
Este proyecto consiste en el desarrollo de un modelo de inteligencia artificial para clasificar hojas de vida (CVs) en diferentes áreas académicas y profesionales utilizando técnicas de procesamiento de lenguaje natural (NLP).
La idea principal del proyecto es apoyar procesos de selección docente y reducir el tiempo que toma revisar perfiles manualmente.
________________________________________
Objetivo
Desarrollar un sistema capaz de identificar automáticamente el área profesional de un perfil docente a partir del texto contenido en una hoja de vida.
________________________________________
Problemática
En muchos procesos de contratación, especialmente en instituciones educativas, la revisión de hojas de vida todavía se realiza de forma manual. Esto genera:
•	Procesos lentos
•	Alta carga operativa
•	Dificultad para clasificar grandes volúmenes de perfiles
•	Posibles inconsistencias en la selección
Por ello, se propone utilizar NLP y machine learning para automatizar parte de este proceso.
________________________________________
Dataset utilizado
Para el entrenamiento del modelo se utilizaron dos fuentes de datos:
•	Dataset público de Kaggle
•	Dataset institucional con perfiles docentes
Ambos datasets fueron integrados para mejorar la representación de categorías académicas.
________________________________________
Tecnologías utilizadas
•	Python
•	Pandas
•	Scikit-learn
•	Google Colab
•	TF-IDF Vectorizer
________________________________________
Preprocesamiento
Antes de entrenar el modelo se aplicaron técnicas básicas de limpieza de texto:
•	Conversión a minúsculas
•	Eliminación de caracteres especiales
•	Eliminación de stopwords
•	Limpieza de palabras irrelevantes
________________________________________
Modelo utilizado
Se utilizó Regresión Logística como modelo principal de clasificación.
Se escogió este modelo porque:
•	Tiene buen desempeño en clasificación de texto
•	Es rápido de entrenar
•	Es interpretable
•	Funciona bien con TF-IDF
________________________________________
Resultados
Resultados obtenidos en la evaluación final:
Métrica	Resultado
Accuracy	0.95
Macro F1-score	0.91
Weighted F1-score	0.95
Validación cruzada	0.76
El modelo obtuvo buenos resultados generales, aunque la validación cruzada mostró que todavía existe cierto grado de sobreajuste y oportunidades de mejora en generalización.
También se observó que algunas categorías como ciencias sociales y salud presentan mayor dificultad debido a similitudes semánticas entre perfiles.
________________________________________
Estructura del proyecto
proyecto-ia/
│
├── data/
├── notebooks/
├── models/
├── results/
├── scripts/
└── README.md
________________________________________
Ejecución del proyecto
1.	Clonar el repositorio
2.	Abrir el notebook en Google Colab
3.	Ejecutar las celdas del pipeline
4.	Cargar un CV en formato PDF o texto
5.	Obtener la predicción automática
________________________________________
Limitaciones
•	El dataset institucional es limitado
•	Existe desbalance entre categorías
•	Algunas áreas presentan similitud de términos
•	El modelo todavía puede mejorar su capacidad de generalización
________________________________________
Trabajo futuro
Como trabajo futuro se podría:
•	Integrar el sistema con plataformas reales
•	Utilizar modelos más avanzados como BERT
•	Incorporar técnicas de explicabilidad
•	Aumentar el tamaño del dataset
________________________________________
Autor
Erika Moreno
Maestría en Inteligencia Artificial Aplicada


## 👤 Erika Moreno

Proyecto académico de titulación  

El flujo del modelo es el siguiente:
