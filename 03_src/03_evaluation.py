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
X_test = df_academico_test.drop(columns=['Target'])
y_test = df_academico_test['Target']



# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------

# CARGA DEL MODELO ENTRENADO

with open('final_model.pkl', 'rb') as f:
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