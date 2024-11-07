<p align="center">
  <img src="./images/Captura de pantalla 2024-11-07 193801.png" alt="Descripción de la imagen">
</p>

# 🎓 Proyecto de Machine Learning: Predicción de Éxito o Fracaso Académico 📊



## 📋 Descripción

Este proyecto tiene como objetivo desarrollar un modelo de **Machine Learning** para predecir el éxito o fracaso académico de los estudiantes en función de sus características personales, académicas y socioeconómicas. Utilizando un enfoque de **clasificación**, el modelo identificará si un estudiante tiene probabilidades de **graduarse** o de **abandonar** sus estudios.

---

## 🚀 Objetivo del Proyecto

El objetivo principal es construir un modelo que sea capaz de **clasificar a los estudiantes en categorías de éxito o fracaso académico**. Esto puede ayudar a las instituciones educativas a identificar estudiantes en riesgo y a implementar estrategias de intervención.

---

## 📊 Datasets

- **Fuente**: Datos ficticios para propósitos de este proyecto.
- **Variables clave**:
  - Datos personales: Estado civil, edad, nacionalidad, género.
  - Datos académicos: Calificaciones, asistencia, unidades curriculares.
  - Datos socioeconómicos: Nivel educativo de los padres, ocupación, tasas de desempleo...

> **Nota**: Actualmente, estamos en la fase de **limpieza de datos** y **preprocesamiento** para garantizar que el conjunto de datos esté listo para el análisis y modelado.

---

## 💡 Motivación

Este proyecto busca utilizar técnicas de **Machine Learning** para abordar uno de los problemas más importantes en la educación: la **retención de estudiantes**. Al identificar patrones y factores que contribuyen al éxito o abandono, podemos ayudar a las instituciones a implementar programas de apoyo y mejorar las tasas de graduación.

---

## 📅 Estado Actual del Proyecto

- [x] Definición del proyecto y objetivos.
- [x] Recolección y exploración de datos.
- [ ] Limpieza y preprocesamiento de datos.
- [ ] Análisis exploratorio de datos (EDA).
- [ ] Selección y entrenamiento de modelos.
- [ ] Evaluación y optimización de modelos.
- [ ] Documentación final y presentación.

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

Este diseño te ayuda a entender mejor la estructura y relevancia de cada grupo de columnas en el contexto de la predicción del éxito o fracaso académico de los estudiantes. Puedes agregar o ajustar la descripción de acuerdo con el avance del análisis.



<p align="center">
  <img src="./images/Captura de pantalla 2024-11-07 211344.png" alt="Descripción de la imagen">
</p>

