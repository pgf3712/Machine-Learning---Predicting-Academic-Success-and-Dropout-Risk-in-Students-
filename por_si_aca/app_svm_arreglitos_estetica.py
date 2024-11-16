import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import os
import base64


# Configuración del tema de la aplicación
st.set_page_config(page_title="Calcula tu Futuro Académico", layout="wide")


# LETRAS EN NEGRITA
# CSS para poner todas las letras en negrita
st.markdown("""
    <style>
    /* Aplica negrita a todos los textos */
    * {
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Función para convertir imagen a base64
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Ruta de la imagen de fondo (asegúrate de usar la ruta correcta)
background_image_path = "../01_data/05_images/6.jpg"

# Convierte la imagen a base64
background_base64 = get_base64(background_image_path)

# CSS para añadir fondo
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{background_base64}");
        background-attachment: fixed;
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ../01_data/05_images/fondo_app.jpg

# Título principal
st.title("🎓 Calcula tu Futuro Académico")

# Cargar el DataFrame de notas de corte
df_notas_corte = pd.read_csv("../01_data/02_processed/notas_corte_total.csv", sep=",")

# Cargar el modelo entrenado
with open('../04_models/final_model.pkl', 'rb') as f:
    modelo = pickle.load(f)

# Tabs para organizar la interfaz
tab1, tab2 = st.tabs(["📝 **Datos del Estudiante**", "📊 **Predicción y Resultados**"])

with tab1:
    st.header("Datos Personales y Académicos")

    # Colocación en columnas
    col1, col2 = st.columns(2)
    with col1:
        specialty_area = st.selectbox("**ESPECIALIDAD**", ["Humanidades y Artes", "Ciencias", "Biosanitario", "Tecnológico-Ingenierías", "Ciencias Sociales-Jurídicas"])
        gender = st.selectbox("**Género**", ["Hombre", "Mujer"])
        age_at_enrollment = st.number_input("**Edad**", min_value=16, max_value=100)
        admission_grade = st.number_input("**NOTA MEDIA 1º Bachillerato**", min_value=0.0, max_value=10.0)

    with col2:
        curricular_units_1st_sem_enrolled = st.number_input("**Asignaturas 1er Semestre (MATRICULADAS)**", min_value=0)
        curricular_units_1st_sem_approved = st.number_input("**Asignaturas 1er Semestre (APROBADAS)**", min_value=0)
        curricular_units_1st_sem_grade = st.number_input("**NOTA MEDIA 1er Semestre**", min_value=0.0, max_value=10.0)
        curricular_units_2nd_sem_enrolled = st.number_input("**Asignaturas 2do Semestre (MATRICULADAS)**", min_value=0)
        curricular_units_2nd_sem_approved = st.number_input("**Asignaturas 2do Semestre (APROBADAS)**", min_value=0)
        curricular_units_2nd_sem_grade = st.number_input("**NOTA MEDIA 2do Semestre**", min_value=0.0, max_value=10.0)

    st.subheader("Información Familiar")
    col3, col4 = st.columns(2)
    with col3:
        fathers_qualification = st.selectbox("**Nivel de estudios del Padre**", ["Ninguno", "Primaria", "Instituto", "Estudios Univeritarios", "Posgrado - Doctorado"])
    with col4:
        mothers_qualification = st.selectbox("**Nivel de estudios de la Madre**", ["Ninguno", "Primaria", "Instituto", "Estudios Univeritarios", "Posgrado - Doctorado"])

    st.subheader("Otros Datos")
    tuition_fees_up_to_date = st.selectbox("**Pagos de Matrícula al Día**", ["Sí", "No"])
    scholarship_holder = st.selectbox("**Becado**", ["Sí", "No"])

    # Convertir variables categóricas a valores numéricos
    mothers_qualification = {"Ninguno": 0, "Primaria": 1, "Instituto": 2, "Estudios Univeritarios": 3, "Posgrado - Doctorado": 4}[mothers_qualification]
    fathers_qualification = {"Ninguno": 0, "Primaria": 1, "Instituto": 2, "Estudios Univeritarios": 3, "Posgrado - Doctorado": 4}[fathers_qualification]
    tuition_fees_up_to_date = 1 if tuition_fees_up_to_date == "Sí" else 0
    gender = 0 if gender == "Hombre" else 1
    scholarship_holder = 1 if scholarship_holder == "Sí" else 0

    # Calcular la nota media final
    nota_media_final = (admission_grade * 0.5) + (curricular_units_1st_sem_grade * 0.25) + (curricular_units_2nd_sem_grade * 0.25)

with tab2:
    st.header("Resultados de la Predicción")

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
    if st.button("🔮 Predecir"):
        with st.spinner("Calculando resultados..."):
            # Realizar predicción usando el modelo
            prediccion = modelo.predict(data)
            probabilidad = modelo.predict_proba(data)[0]  # Obtener probabilidades

        # Mostrar resultados de la predicción
        if prediccion[0] == 1:
            st.success("✅ APTO")
        else:
            st.error("❌ NO APTO")

        st.write(f"### Nota Media Final: {nota_media_final:.2f}")

        # Gráfico de probabilidades en formato pie chart
        st.subheader("Probabilidades de Graduación")
        fig, ax = plt.subplots()
        colors = ["#ea6363", "#6eea63"]
        # Etiquetas
        labels = ["NO APTO", "APTO"]
        ax.pie(probabilidad, autopct='%1.1f%%', colors=colors, startangle=90)

        # Añadir leyenda en la parte inferior derecha
        ax.legend(
            labels, 
            loc="lower right", 
            fontsize="small"  
        )
        ax.axis('equal') 
        st.pyplot(fig)

        # Si el alumno es apto, mostrar carreras accesibles
        if prediccion[0] == 1:
            st.subheader("Carreras Disponibles")
            carreras_accesibles = df_notas_corte[(df_notas_corte['NOTA FINAL'] <= nota_media_final) & 
                                                 (df_notas_corte['Especialidad'] == specialty_area)]
            carreras_accesibles = carreras_accesibles.sort_values(by='Grupo 1 Ord.', ascending=False)
            st.dataframe(carreras_accesibles[['Código', 'TITULACIONES DE GRADO', 'Grupo 1 Ord.', 'Centro']])



# streamlit run app_svm_arreglitos_estetica.py