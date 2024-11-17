import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import os
import base64
import time
from fpdf import FPDF
import base64
from datetime import datetime


# Configuración del tema de la aplicación
st.set_page_config(page_title="Calcula tu Futuro Académico", layout="wide")

st.markdown(
    """
    <style>
    /* Marco global con bordes dobles separados */
    .stApp {
        border: 25px solid #ADD8E6; /* Borde interior azul pastel */
        outline: 56px solid #FF6347; /* Borde exterior rojo */
        outline-offset: 10px; /* Espacio entre bordes */
        border-radius: 15px; /* Bordes redondeados */
        padding: 20px; /* Espaciado interno */
        background-color: #F8F8FF; /* Fondo azul claro */
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); /* Sombra suave */
    }

    /* Ajuste del contenido interno */
    .block-container {
        padding: 20px; /* Más espacio interno */
    }
    </style>
    """,
    unsafe_allow_html=True
)


class PDF(FPDF):
    def header(self):
        # Encabezado
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Listado de Carreras Disponibles", border=0, ln=1, align="C")
        self.ln(10)

    def footer(self):
        # Pie de página
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Página {self.page_no()} - Generado el {datetime.now().strftime('%d/%m/%Y')}", align="C")

def generar_pdf_listado(carreras_accesibles):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    # Generar el listado
    for index, row in carreras_accesibles.iterrows():
        pdf.set_font("Arial", style="B", size=10)
        pdf.cell(0, 10, f"{index + 1}. {row['TITULACIONES DE GRADO']}", ln=1)  # Titulación
        pdf.set_font("Arial", size=10)
        pdf.cell(0, 10, f"    Centro: {row['Centro']}", ln=1)  # Centro
        pdf.cell(0, 10, f"    Nota: {row['Grupo 1 Ord.']}", ln=1)  # Nota
        pdf.ln(5)  # Espacio entre carreras

    # Guardar el PDF
    pdf_file = "carreras_disponibles_listado.pdf"
    pdf.output(pdf_file)
    return pdf_file

# Función para convertir el archivo PDF a base64 para la descarga
def convertir_a_base64(pdf_file):
    with open(pdf_file, "rb") as file:
        pdf_bytes = file.read()
    b64 = base64.b64encode(pdf_bytes).decode()
    return b64


# LETRAS EN NEGRITA
st.markdown("""
    <style>
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

# Ruta de la imagen de fondo
background_image_path = "../01_data/05_images/6.jpg"
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

    col1, col2 = st.columns(2)
    with col1:
        specialty_area = st.selectbox("🎨 **ESPECIALIDAD**", ["Humanidades y Artes", "Ciencias", "Biosanitario", "Tecnológico-Ingenierías", "Ciencias Sociales-Jurídicas"])
        gender = st.selectbox("👤 **Género**", ["Hombre", "Mujer"])
        age_at_enrollment = st.number_input("🎂 **Edad**", min_value=16, max_value=100)
        admission_grade = st.number_input("📚 **NOTA MEDIA 1º Bachillerato**", min_value=0.0, max_value=10.0)

    with col2:
        curricular_units_1st_sem_enrolled = st.number_input("📘 **Asignaturas 1er Semestre (MATRICULADAS)**", min_value=0)
        curricular_units_1st_sem_approved = st.number_input("📗 **Asignaturas 1er Semestre (APROBADAS)**", min_value=0)
        curricular_units_1st_sem_grade = st.number_input("📊 **NOTA MEDIA 1er Semestre**", min_value=0.0, max_value=10.0)
        curricular_units_2nd_sem_enrolled = st.number_input("📘 **Asignaturas 2do Semestre (MATRICULADAS)**", min_value=0)
        curricular_units_2nd_sem_approved = st.number_input("📗 **Asignaturas 2do Semestre (APROBADAS)**", min_value=0)
        curricular_units_2nd_sem_grade = st.number_input("📊 **NOTA MEDIA 2do Semestre**", min_value=0.0, max_value=10.0)

    st.subheader("Información Familiar")
    col3, col4 = st.columns(2)
    with col3:
        fathers_qualification = st.selectbox("👨‍🎓 **Nivel de estudios del Padre**", ["Ninguno", "Primaria", "Instituto", "Estudios Univeritarios", "Posgrado - Doctorado"])
    with col4:
        mothers_qualification = st.selectbox("👩‍🎓 **Nivel de estudios de la Madre**", ["Ninguno", "Primaria", "Instituto", "Estudios Univeritarios", "Posgrado - Doctorado"])

    st.subheader("Otros Datos")
    tuition_fees_up_to_date = st.selectbox("💳 **Pagos de Matrícula al Día**", ["Sí", "No"])
    scholarship_holder = st.selectbox("🎓 **Becado**", ["Sí", "No"])

    mothers_qualification = {"Ninguno": 0, "Primaria": 1, "Instituto": 2, "Estudios Univeritarios": 3, "Posgrado - Doctorado": 4}[mothers_qualification]
    fathers_qualification = {"Ninguno": 0, "Primaria": 1, "Instituto": 2, "Estudios Univeritarios": 3, "Posgrado - Doctorado": 4}[fathers_qualification]
    tuition_fees_up_to_date = 1 if tuition_fees_up_to_date == "Sí" else 0
    gender = 0 if gender == "Hombre" else 1
    scholarship_holder = 1 if scholarship_holder == "Sí" else 0

    nota_media_final = (admission_grade * 0.5) + (curricular_units_1st_sem_grade * 0.25) + (curricular_units_2nd_sem_grade * 0.25)

with tab2:
    st.header("Resultados de la Predicción")

    data = pd.DataFrame({
        "Tuition fees up to date": [tuition_fees_up_to_date],
        "Scholarship holder": [scholarship_holder],
        "Curricular units 1st sem (enrolled)": [curricular_units_1st_sem_enrolled],
        "Curricular units 1st sem (approved)": [curricular_units_1st_sem_approved],
        "Curricular units 2nd sem (enrolled)": [curricular_units_2nd_sem_enrolled],
        "Curricular units 2nd sem (approved)": [curricular_units_2nd_sem_approved],
    })

    if st.button("🔮 Predecir"):
        with st.spinner("Calculando resultados..."):
            prediccion = modelo.predict(data)
            probabilidad = modelo.predict_proba(data)[0]

        if prediccion[0] == 1:
            st.success("## ✅ APTO")



            # Mostrar gráfico de pie dentro de un desplegable
            with st.expander("### 📊 **Ver Probabilidades de Graduación**"):
                st.subheader("Probabilidades de Graduación")
                fig, ax = plt.subplots()
                colors = ["#ff9999", "#99ff99"]
                labels = ["NO APTO", "APTO"]
                ax.pie(probabilidad, autopct='%1.1f%%', colors=colors, startangle=90)
                ax.axis("equal")
                ax.legend(labels, loc="lower right", title="Leyenda")
                st.pyplot(fig)

            # Mostrar carreras accesibles
            st.subheader("Carreras Disponibles")
            carreras_accesibles = df_notas_corte[(df_notas_corte['NOTA FINAL'] <= nota_media_final) & 
                                                 (df_notas_corte['Especialidad'] == specialty_area)]
            carreras_accesibles = carreras_accesibles.sort_values(by='TITULACIONES DE GRADO', ascending=True)
            st.dataframe(carreras_accesibles[['Código', 'TITULACIONES DE GRADO', 'Grupo 1 Ord.', 'Centro']])

            # Generar PDF con las carreras accesibles
            if not carreras_accesibles.empty:
                pdf_file = generar_pdf_listado(carreras_accesibles)
                b64_pdf = convertir_a_base64(pdf_file)

                 # Botón para descargar el PDF
                href = f'<a href="data:application/octet-stream;base64,{b64_pdf}" download="carreras_disponibles.pdf">📥 Descargar Carreras en PDF</a>'
                st.markdown(href, unsafe_allow_html=True)

            # GIF
            gif_path = "../01_data/05_images/homer.gif" 
            st.image(gif_path, use_container_width=True)
            time.sleep(5)  # Mostrar el GIF durante 5 segundos
            st.empty()  # Limpiar el espacio del GIF


        else:
            st.error("## ❌ NO APTO")

            # Mostrar gráfico de pie dentro de un desplegable
            with st.expander("### 📊 **Ver Probabilidades de Graduación**"):
                st.subheader("Probabilidades de Graduación")
                fig, ax = plt.subplots()
                colors = ["#ff9999", "#99ff99"]
                labels = ["NO APTO", "APTO"]
                ax.pie(probabilidad, autopct='%1.1f%%', colors=colors, startangle=90)
                ax.axis("equal")
                ax.legend(labels, loc="lower right", title="Leyenda")
                st.pyplot(fig)


# streamlit run app.py