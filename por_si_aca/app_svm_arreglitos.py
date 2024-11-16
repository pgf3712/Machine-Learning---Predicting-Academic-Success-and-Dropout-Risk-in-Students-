import streamlit as st
import pandas as pd
import pickle

# Cargar el DataFrame de notas de corte
df_notas_corte = pd.read_csv("../01_data/02_processed/notas_corte_total.csv", sep=",")  

# Cargar el modelo entrenado (incluye el escalador y el modelo de regresión logística)
with open('../04_models/final_model.pkl', 'rb') as f:  
    modelo = pickle.load(f)

# Título de la aplicación
st.title("CALCULA TU FUTURO ACADÉMICO")

# Crear entradas para los datos del usuario
specialty_area = st.selectbox("ESPECIALIDAD", ["Humanidades y Artes", "Ciencias", "Biosanitario", "Tecnológico-Ingenierías", "Ciencias Sociales-Jurídicas"])
gender = st.selectbox("Género", ["Hombre", "Mujer"])
age_at_enrollment = st.number_input("Edad", min_value=16, max_value=100)
admission_grade = st.number_input("NOTA MEDIA 1º Bachillerato", min_value=0.0, max_value=10.0)
curricular_units_1st_sem_enrolled = st.number_input("Asignaturas 1er Semestre (MATRICULADAS)", min_value=0)
curricular_units_1st_sem_approved = st.number_input("Asignaturas 1er Semestre (APROBADAS)", min_value=0)
curricular_units_1st_sem_grade = st.number_input("NOTA MEDIA 1er Semestre", min_value=0.0, max_value=10.0)
curricular_units_2nd_sem_enrolled = st.number_input("Asignaturas 2do Semestre (MATRICULADAS)", min_value=0)
curricular_units_2nd_sem_approved = st.number_input("Asignaturas 2do Semestre (APROBADAS)", min_value=0)
curricular_units_2nd_sem_grade = st.number_input("NOTA MEDIA 2do Semestre", min_value=0.0, max_value=10.0)
fathers_qualification = st.selectbox("Nivel de estudios del Padre", ["Ninguno", "Primaria", "Instituto", "Estudios Univeritarios", "Posgrado - Doctorado"])
mothers_qualification = st.selectbox("Nivel de estudios de la Madre", ["Ninguno", "Primaria", "Instituto", "Estudios Univeritarios", "Posgrado - Doctorado"])
tuition_fees_up_to_date = st.selectbox("Pagos de Matrícula al Día", ["Yes", "No"])
scholarship_holder = st.selectbox("Becado", ["Yes", "No"])



# Convertir variables categóricas a valores numéricos

mothers_qualification = {"Ninguno": 0, "Primaria": 1, "Instituto": 2, "Estudios Univeritarios": 3, "Posgrado - Doctorado": 4}[mothers_qualification]
fathers_qualification = {"Ninguno": 0, "Primaria": 1, "Instituto": 2, "Estudios Univeritarios": 3, "Posgrado - Doctorado": 4}[fathers_qualification]
tuition_fees_up_to_date = 1 if tuition_fees_up_to_date == "Yes" else 0
gender = 0 if gender == "Hombre" else 1
scholarship_holder = 1 if scholarship_holder == "Yes" else 0


# Calcular la nota media final del alumno
nota_media_final = (admission_grade * 0.5) + (curricular_units_1st_sem_grade * 0.25) + (curricular_units_2nd_sem_grade * 0.25) 

# Crear un DataFrame con los datos ingresados
data = pd.DataFrame({
    "Tuition fees up to date": [tuition_fees_up_to_date],
    "Scholarship holder": [scholarship_holder],
    "Curricular units 1st sem (enrolled)": [curricular_units_1st_sem_enrolled],
    "Curricular units 1st sem (approved)": [curricular_units_1st_sem_approved],
    "Curricular units 2nd sem (enrolled)": [curricular_units_2nd_sem_enrolled],
    "Curricular units 2nd sem (approved)": [curricular_units_2nd_sem_approved],
})


# Botón para realizar la predicción
if st.button("Predecir"):
    # Realizar predicción usando el modelo
    prediccion = modelo.predict(data)
    probabilidad = modelo.predict_proba(data)

    # Mostrar resultados de la predicción
    st.write("# APTO" if prediccion[0] == 1 else "# NO APTO")
    st.write("### NOTA MEDIA TOTAL:", nota_media_final)

    # Si el alumno se gradúa, mostrar las carreras a las que puede acceder
    if prediccion[0] == 1:
        st.write("### Acceso a estudios:")
        # Filtrar carreras según la nota media
        carreras_accesibles = df_notas_corte[(df_notas_corte['NOTA FINAL'] <= nota_media_final) & 
                                             (df_notas_corte['Especialidad'] == specialty_area)]
        carreras_accesibles = carreras_accesibles.sort_values(by='Grupo 1 Ord.', ascending=False)
        
        # Mostrar las carreras en la aplicación
        st.dataframe(carreras_accesibles[['Código', 'TITULACIONES DE GRADO', 'Grupo 1 Ord.', 'Centro']])


# streamlit run app_svm_arreglitos.py