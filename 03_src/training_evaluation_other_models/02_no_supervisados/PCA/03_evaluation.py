# IMPORTO LIBRERIAS

from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import pickle


# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------

# IMPORTO DATOS DE PRUEBA

df_academico_test = pd.read_csv("../01_data/04_test/ds_academico_test.csv", sep=",")

# Separar características y target
X_test = df_academico_test[["Tuition fees up to date", "Scholarship holder", "Curricular units 1st sem (enrolled)", "Curricular units 1st sem (approved)", "Curricular units 2nd sem (enrolled)", "Curricular units 2nd sem (approved)"]]
y_test = df_academico_test['Target']


# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------

# CARGA DEL MODELO ENTRENADO

with open('../04_models/other_models/02_no_supervisados/trained_model_pca.pkl', 'rb') as f:
    modelo_importado = pickle.load(f)


# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------

# PREDICCIONES Y ACCURACY

# Generar predicciones
y_pred = modelo_importado.predict(X_test)

# Calcular métricas de evaluación
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("Classification Report:")
print(classification_report(y_test, y_pred))


# python 03_evaluation.py