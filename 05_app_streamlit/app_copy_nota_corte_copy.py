import streamlit as st
import pandas as pd
import pickle

# Cargar el DataFrame de notas de corte
df_notas_corte = pd.read_csv("../01_data/02_processed/notas_corte_total.csv", sep=",")  

# Cargar el modelo entrenado (incluye el escalador y el modelo de regresión logística)
with open('../04_models/final_model_basico.pkl', 'rb') as f:  
    modelo = pickle.load(f)

# Título de la aplicación
st.title("Predicción de Éxito Académico")

# Crear entradas para los datos del usuario
mothers_qualification = st.selectbox("Nivel de estudios de la Madre", ["Ninguno", "Primaria", "Instituto", "Estudios Univeritarios", "Posgrado - Doctorado"])
fathers_qualification = st.selectbox("Nivel de estudios del Padre", ["Ninguno", "Primaria", "Instituto", "Estudios Univeritarios", "Posgrado - Doctorado"])
admission_grade = st.number_input("NOTA MEDIA 1º Bachillerato", min_value=0.0, max_value=10.0)
educational_special_needs = st.selectbox("Necesidades Educativas Especiales", ["Yes", "No"])
debtor = st.selectbox("Deudor", ["Yes", "No"])
tuition_fees_up_to_date = st.selectbox("Pagos de Matrícula al Día", ["Yes", "No"])
gender = st.selectbox("Género", ["Hombre", "Mujer"])
scholarship_holder = st.selectbox("Becado", ["Yes", "No"])
age_at_enrollment = st.number_input("Edad", min_value=18, max_value=100)
international = st.selectbox("Estudiante Internacional", ["Yes", "No"])
curricular_units_1st_sem_credited = st.number_input("CREDITOS OBTENIDOS 1er Semestre", min_value=0)
curricular_units_1st_sem_enrolled = st.number_input("Asignaturas 1er Semestre (Inscritas)", min_value=0)
curricular_units_1st_sem_evaluations = st.number_input("Nº de exámenes 1er Semestre", min_value=0)
curricular_units_1st_sem_approved = st.number_input("Nº de exámenes 1er Semestre (APROBADOS)", min_value=0)
curricular_units_1st_sem_grade = st.number_input("NOTA MEDIA 1er Semestre", min_value=0.0, max_value=10.0)
curricular_units_2nd_sem_credited = st.number_input("CREDITOS OBTENIDOS 2do Semestre", min_value=0)
curricular_units_2nd_sem_enrolled = st.number_input("Asignaturas 2do Semestre (Inscritas)", min_value=0)
curricular_units_2nd_sem_evaluations = st.number_input("Nº de exámenes 2do Semestre", min_value=0)
curricular_units_2nd_sem_approved = st.number_input("Nº de exámenes 2do Semestre (APROBADOS)", min_value=0)
curricular_units_2nd_sem_grade = st.number_input("NOTA MEDIA 2do Semestre", min_value=0.0, max_value=10.0)
specialty_area = st.selectbox("ESPECIALIDAD", ["Humanidades y Artes", "Ciencias", "Biosanitario", "Tecnológico-Ingenierías", "Ciencias Sociales-Jurídicas"])


# Convertir variables categóricas a valores numéricos
# daytime_evening_attendance = 0 if daytime_evening_attendance == "Daytime" else 1
mothers_qualification = {"Ninguno": 0, "Primaria": 1, "Instituto": 2, "Estudios Univeritarios": 3, "Posgrado - Doctorado": 4}[mothers_qualification]
fathers_qualification = {"Ninguno": 0, "Primaria": 1, "Instituto": 2, "Estudios Univeritarios": 3, "Posgrado - Doctorado": 4}[fathers_qualification]
educational_special_needs = 1 if educational_special_needs == "Yes" else 0
debtor = 1 if debtor == "Yes" else 0
tuition_fees_up_to_date = 1 if tuition_fees_up_to_date == "Yes" else 0
gender = 0 if gender == "Hombre" else 1
scholarship_holder = 1 if scholarship_holder == "Yes" else 0
international = 1 if international == "Yes" else 0

# Calcular la nota media final del alumno
nota_media_final = (admission_grade * 0.5) + (curricular_units_1st_sem_grade * 0.25) + (curricular_units_2nd_sem_grade * 0.25) 

# Crear un DataFrame con los datos ingresados
data = pd.DataFrame({
    #"Daytime/evening attendance": [daytime_evening_attendance],
    #"Previous qualification (grade)": [previous_qualification_grade],
    #"Mother's qualification": [mothers_qualification],
    #"Father's qualification": [fathers_qualification],
    #"Admission grade": [admission_grade],
    #"Educational special needs": [educational_special_needs],
    #"Debtor": [debtor],
    #"Tuition fees up to date": [tuition_fees_up_to_date],
    #"Gender": [gender],
    #"Scholarship holder": [scholarship_holder],
    #"Age at enrollment": [age_at_enrollment],
    #"International": [international],
    #"Curricular units 1st sem (credited)": [curricular_units_1st_sem_credited],
    "Curricular units 1st sem (enrolled)": [curricular_units_1st_sem_enrolled],
    #"Curricular units 1st sem (evaluations)": [curricular_units_1st_sem_evaluations],
    "Curricular units 1st sem (approved)": [curricular_units_1st_sem_approved],
    #"Curricular units 1st sem (grade)": [curricular_units_1st_sem_grade],
    #"Curricular units 2nd sem (credited)": [curricular_units_2nd_sem_credited],
    "Curricular units 2nd sem (enrolled)": [curricular_units_2nd_sem_enrolled],
    #"Curricular units 2nd sem (evaluations)": [curricular_units_2nd_sem_evaluations],
    "Curricular units 2nd sem (approved)": [curricular_units_2nd_sem_approved],
    #"Curricular units 2nd sem (grade)": [curricular_units_2nd_sem_grade]
})


# Botón para realizar la predicción
if st.button("Predecir"):
    # Realizar predicción usando el modelo
    prediccion = modelo.predict(data)
    probabilidad = modelo.predict_proba(data)

    # Mostrar resultados de la predicción
    st.write("Predicción:", "Se Gradúa" if prediccion[0] == 1 else "No se Gradúa")
    #st.write("Probabilidad de éxito académico:", probabilidad[0][1])
    #st.write("Probabilidad de riesgo de abandono:", probabilidad[0][0])

    # st.write("Columnas disponibles en el DataFrame de notas de corte:", df_notas_corte.columns)
    # st.write(df_notas_corte.head())


    # Si el alumno se gradúa, mostrar las carreras a las que puede acceder
    if prediccion[0] == 1:
        st.write("### Carreras a las que el alumno puede acceder según su nota media final")
        # Filtrar carreras según la nota media
        carreras_accesibles = df_notas_corte[(df_notas_corte['NOTA FINAL'] <= nota_media_final) & 
                                             (df_notas_corte['Especialidad'] == specialty_area)]
        carreras_accesibles = carreras_accesibles.sort_values(by='Grupo 1 Ord.', ascending=False)
        
        # Mostrar las carreras en la aplicación
        st.dataframe(carreras_accesibles[['Código', 'TITULACIONES DE GRADO', 'Grupo 1 Ord.', 'Centro']])


# streamlit run app_copy_nota_corte_copy.py