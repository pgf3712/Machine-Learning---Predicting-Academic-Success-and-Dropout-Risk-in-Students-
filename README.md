<p align="center">
  <img src="./01_data/05_images/Captura de pantalla 2024-11-07 193801.png" alt="Descripción de la imagen">
</p>

# 🎓 Proyecto de Machine Learning: Predicción de Éxito Académico 📊

## 📋 Descripción

Este proyecto utiliza **Machine Learning** para predecir el éxito o fracaso académico de estudiantes de bachillerato. Además, se ha desarrollado una aplicación en **Streamlit** que, basándose en las predicciones, ofrece orientación personalizada sobre carreras universitarias o grados superiores disponibles en Madrid según la especialidad del estudiante (Ciencias, Letras, Artes, etc.).

---

## 🚀 Objetivo del Proyecto

1. **Predicción Académica:**  
   Desarrollar un modelo para clasificar a los estudiantes en categorías de **graduado** o **no graduado**.
   
2. **Orientación Vocacional:**  
   Proporcionar un listado de opciones académicas en Madrid para ayudar a los estudiantes a planificar su futuro de manera exitosa.

---

## 📊 Dataset

- **Características principales:**
  - Información personal: Edad, género, estado civil, entre otros.
  - Datos académicos: Unidades curriculares aprobadas, evaluaciones, notas.
  - Información socioeconómica: Nivel educativo de los padres, ocupación, becas.
  - Factores económicos externos: Tasa de desempleo, inflación.

---

## 💡 Motivación

El proyecto busca no solo predecir el rendimiento académico, sino también aportar un valor adicional al guiar a los estudiantes hacia carreras o estudios superiores que maximicen sus posibilidades de éxito. Esto resulta particularmente útil para instituciones educativas y orientadores vocacionales.

---

## 🔬 Metodología

1. **Preparación de Datos:**
   - Limpieza, preprocesamiento y transformación de datos.
   - Uso de **Standard Scaler** para normalizar las características numéricas.

2. **Modelos Probados:**
   Se entrenaron y evaluaron varios modelos supervisados y no supervisados:
   - **Modelos Supervisados:**
     - Decision Tree Classifier
     - Gradient Boosting Classifier
     - K-Nearest Neighbors (KNN)
     - Logistic Regression
     - Random Forest Classifier
     - Support Vector Machines (SVM)
   - **Modelos No Supervisados:**
     - Clustering
     - Análisis de Componentes Principales (PCA)
   - **Modelo basado en redes neuronales:**  
     Implementación de una Red Neuronal para clasificación.

3. **Modelo Ganador:**
   - El modelo de **Support Vector Machines (SVM)** obtuvo el mejor desempeño en términos de precisión, recall y F1-score.

4. **Aplicación Web:**
   - Desarrollo de una aplicación interactiva en **Streamlit** que:
     - Predice si un estudiante se gradúa o no.
     - Ofrece un listado personalizado de carreras o grados superiores en Madrid basándose en la especialidad del estudiante (Ciencias, Letras, Artes).

---

## 🛠️ Herramientas y Tecnologías

- **Lenguaje:** Python
- **Bibliotecas:** scikit-learn, pandas, numpy, matplotlib, seaborn.
- **Aplicación Web:** Streamlit.
- **Visualización:** PCA y gráficos de distribución para analizar resultados.

---

## 🏆 Resultados

1. **Modelo SVM:**
   - **Precisión:** 0.90
   - **Recall:** 0.94
   - **F1-Score:** 0.91
  

2. **Aplicación Streamlit:**
   - Funcionalidad completa para predicciones.
   - Ofrece orientación vocacional personalizada.

---
---


---
---

# 📑 Descripción de las Columnas

En esta sección se detallan las columnas del dataset utilizado en el proyecto. Estas se agrupan en categorías para facilitar la comprensión.

---

## 🧑‍🎓 Información Personal

- **Marital status**: Estado civil del estudiante (representado numéricamente).
- **Gender**: Género del estudiante (`0` para hombre, `1` para mujer).
- **Age at enrollment**: Edad del estudiante al momento de la inscripción.
- **International**: Indica si el estudiante es internacional (`1`) o no (`0`).
- **Displaced**: Indica si el estudiante está desplazado (`1`) o no (`0`).
- **Educational special needs**: Indica si el estudiante tiene necesidades educativas especiales (`1`) o no (`0`).

---

## 🏫 Información Académica

- **Application mode**: Modo de aplicación (probablemente relacionado con el tipo de admisión o proceso de inscripción).
- **Application order**: Orden de aplicación, indicando posiblemente en qué orden el estudiante aplicó a diferentes cursos o programas.
- **Course**: Código del curso en el que el estudiante está inscrito.
- **Daytime/evening attendance**: Si el estudiante asiste durante el día o en la noche (`1`: diurno, `0`: nocturno).
- **Previous qualification**: Calificación académica anterior o nivel de estudios previo (representado numéricamente).
- **Previous qualification (grade)**: Calificación promedio o puntuación obtenida en la calificación académica anterior.
- **Admission grade**: Nota o puntuación de admisión del estudiante.

---

## 📚 Unidades Curriculares

### Primer Semestre

- **Curricular units 1st sem (credited)**: Número de unidades curriculares aprobadas en el primer semestre.
- **Curricular units 1st sem (enrolled)**: Número de unidades curriculares inscritas en el primer semestre.
- **Curricular units 1st sem (evaluations)**: Número de evaluaciones en unidades curriculares del primer semestre.
- **Curricular units 1st sem (approved)**: Número de unidades curriculares aprobadas en el primer semestre.
- **Curricular units 1st sem (grade)**: Calificación promedio en las unidades curriculares del primer semestre.
- **Curricular units 1st sem (without evaluations)**: Número de unidades curriculares en el primer semestre sin evaluaciones.

### Segundo Semestre

- **Curricular units 2nd sem (credited)**: Número de unidades curriculares aprobadas en el segundo semestre.
- **Curricular units 2nd sem (enrolled)**: Número de unidades curriculares inscritas en el segundo semestre.
- **Curricular units 2nd sem (evaluations)**: Número de evaluaciones en unidades curriculares del segundo semestre.
- **Curricular units 2nd sem (approved)**: Número de unidades curriculares aprobadas en el segundo semestre.
- **Curricular units 2nd sem (grade)**: Calificación promedio en las unidades curriculares del segundo semestre.
- **Curricular units 2nd sem (without evaluations)**: Número de unidades curriculares en el segundo semestre sin evaluaciones.

---

## 👪 Información Familiar

- **Mother's qualification**: Nivel educativo de la madre (representado numéricamente).
- **Father's qualification**: Nivel educativo del padre (representado numéricamente).
- **Mother's occupation**: Ocupación de la madre (representado numéricamente).
- **Father's occupation**: Ocupación del padre (representado numéricamente).

---

## 💵 Información Socioeconómica y Financiera

- **Nacionality**: Nacionalidad del estudiante (representado numéricamente).
- **Scholarship holder**: Indica si el estudiante es becado (`1`) o no (`0`).
- **Debtor**: Indica si el estudiante tiene deudas (`1`) o no (`0`).
- **Tuition fees up to date**: Indica si las tasas de matrícula están al día (`1`) o no (`0`).

---

## 📈 Indicadores Económicos

- **Unemployment rate**: Tasa de desempleo (posiblemente en el área o región donde vive el estudiante).
- **Inflation rate**: Tasa de inflación (posiblemente en la región o país).
- **GDP**: Producto Interno Bruto (PIB), posiblemente relacionado con la región o país del estudiante.

---

## 🎯 Variable Objetivo

- **Target**: Objetivo de predicción, que indica el estado final del estudiante (por ejemplo, "Dropout" si el estudiante abandonó, "Graduate" si se graduó).

---

## **Notas** 📝

- **Unidades Curriculares**: Varias columnas hacen referencia al desempeño del estudiante en unidades curriculares, tanto en el primer como en el segundo semestre, lo cual puede ser clave para analizar el rendimiento académico.
  
- **Factores Socioeconómicos y Familiares**: Columnas sobre el estado civil, ocupación y educación de los padres, lo cual puede ser relevante para analizar el impacto socioeconómico en el rendimiento académico.
  
- **Factores Económicos**: Las columnas sobre la tasa de desempleo, inflación y PIB pueden ayudar a relacionar factores económicos externos con el desempeño académico del estudiante.

---



<p align="center">
  <img src="./01_data/05_images/Captura de pantalla 2024-11-07 211344.png" alt="Descripción de la imagen">
</p>
