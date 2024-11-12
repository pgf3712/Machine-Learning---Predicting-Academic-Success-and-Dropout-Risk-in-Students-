import streamlit as st
import pandas as pd
import pickle

df_academico = pd.read_csv("../01_data/02_processed/ds_academico.csv", sep=",") 


# Título de la aplicación
st.title("Predicción de Éxito Académico")

# Cargar el modelo entrenado
with open('../04_models/final_model.pkl', 'rb') as f:  
    modelo = pickle.load(f)   

# Instrucciones para el usuario
st.write("Por favor, ingresa los datos del estudiante para predecir el éxito académico.")

# Crear entradas para los datos del usuario
daytime_evening_attendance = st.selectbox("Asistencia Diurna/Nocturna", ["Daytime", "Evening"])
previous_qualification = st.selectbox("Calificación Previa", ["None", "High School", "Bachelor's", "Master's", "Other"])
previous_qualification_grade = st.number_input("Nota Calificación Previa", min_value=0.0, max_value=20.0)
mothers_qualification = st.selectbox("Calificación de la Madre", ["None", "High School", "Bachelor's", "Master's", "Other"])
fathers_qualification = st.selectbox("Calificación del Padre", ["None", "High School", "Bachelor's", "Master's", "Other"])
admission_grade = st.number_input("Nota de Admisión", min_value=0.0, max_value=20.0)
educational_special_needs = st.selectbox("Necesidades Educativas Especiales", ["Yes", "No"])
debtor = st.selectbox("Deudor", ["Yes", "No"])
tuition_fees_up_to_date = st.selectbox("Pagos de Matrícula al Día", ["Yes", "No"])
gender = st.selectbox("Género", ["Male", "Female"])
scholarship_holder = st.selectbox("Becado", ["Yes", "No"])
age_at_enrollment = st.number_input("Edad en el Momento de Inscripción", min_value=18, max_value=100)
international = st.selectbox("Estudiante Internacional", ["Yes", "No"])
curricular_units_1st_sem_credited = st.number_input("Unidades Curriculares 1er Semestre (Acreditadas)", min_value=0)
curricular_units_1st_sem_enrolled = st.number_input("Unidades Curriculares 1er Semestre (Inscritas)", min_value=0)
curricular_units_1st_sem_evaluations = st.number_input("Unidades Curriculares 1er Semestre (Evaluaciones)", min_value=0)
curricular_units_1st_sem_approved = st.number_input("Unidades Curriculares 1er Semestre (Aprobadas)", min_value=0)
curricular_units_1st_sem_grade = st.number_input("Nota Unidades Curriculares 1er Semestre", min_value=0.0, max_value=20.0)
curricular_units_2nd_sem_credited = st.number_input("Unidades Curriculares 2do Semestre (Acreditadas)", min_value=0)
curricular_units_2nd_sem_enrolled = st.number_input("Unidades Curriculares 2do Semestre (Inscritas)", min_value=0)
curricular_units_2nd_sem_evaluations = st.number_input("Unidades Curriculares 2do Semestre (Evaluaciones)", min_value=0)
curricular_units_2nd_sem_approved = st.number_input("Unidades Curriculares 2do Semestre (Aprobadas)", min_value=0)
curricular_units_2nd_sem_grade = st.number_input("Nota Unidades Curriculares 2do Semestre", min_value=0.0, max_value=20.0)

# Convertir variables categóricas a valores numéricos
daytime_evening_attendance = 0 if daytime_evening_attendance == "Daytime" else 1
previous_qualification = {"None": 0, "High School": 1, "Bachelor's": 2, "Master's": 3, "Other": 4}[previous_qualification]
mothers_qualification = {"None": 0, "High School": 1, "Bachelor's": 2, "Master's": 3, "Other": 4}[mothers_qualification]
fathers_qualification = {"None": 0, "High School": 1, "Bachelor's": 2, "Master's": 3, "Other": 4}[fathers_qualification]
educational_special_needs = 1 if educational_special_needs == "Yes" else 0
debtor = 1 if debtor == "Yes" else 0
tuition_fees_up_to_date = 1 if tuition_fees_up_to_date == "Yes" else 0
gender = 0 if gender == "Male" else 1
scholarship_holder = 1 if scholarship_holder == "Yes" else 0
international = 1 if international == "Yes" else 0

# Crear un DataFrame con los datos ingresados
data = pd.DataFrame({
    "Daytime/evening attendance": [daytime_evening_attendance],
    "Previous qualification": [previous_qualification],
    "Previous qualification (grade)": [previous_qualification_grade],
    "Mother's qualification": [mothers_qualification],
    "Father's qualification": [fathers_qualification],
    "Admission grade": [admission_grade],
    "Educational special needs": [educational_special_needs],
    "Debtor": [debtor],
    "Tuition fees up to date": [tuition_fees_up_to_date],
    "Gender": [gender],
    "Scholarship holder": [scholarship_holder],
    "Age at enrollment": [age_at_enrollment],
    "International": [international],
    "Curricular units 1st sem (credited)": [curricular_units_1st_sem_credited],
    "Curricular units 1st sem (enrolled)": [curricular_units_1st_sem_enrolled],
    "Curricular units 1st sem (evaluations)": [curricular_units_1st_sem_evaluations],
    "Curricular units 1st sem (approved)": [curricular_units_1st_sem_approved],
    "Curricular units 1st sem (grade)": [curricular_units_1st_sem_grade],
    "Curricular units 2nd sem (credited)": [curricular_units_2nd_sem_credited],
    "Curricular units 2nd sem (enrolled)": [curricular_units_2nd_sem_enrolled],
    "Curricular units 2nd sem (evaluations)": [curricular_units_2nd_sem_evaluations],
    "Curricular units 2nd sem (approved)": [curricular_units_2nd_sem_approved],
    "Curricular units 2nd sem (grade)": [curricular_units_2nd_sem_grade]
})

# Botón para realizar la predicción
if st.button("Predecir"):
    # Realizar predicción
    prediccion = modelo.predict(data)
    probabilidad = modelo.predict_proba(data)

    # Mostrar resultados
    st.write("Predicción:", "Se Gradúa" if prediccion[0] == 1 else "No se Gradúa")
    st.write("Probabilidad de éxito académico:", probabilidad[0][1])
    st.write("Probabilidad de riesgo de abandono:", probabilidad[0][0])



