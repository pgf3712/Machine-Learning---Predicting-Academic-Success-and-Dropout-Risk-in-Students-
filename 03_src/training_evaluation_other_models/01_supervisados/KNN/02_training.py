# IMPORTO LIBRERIAS

from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle


# Cargar el modelo entrenado
with open('../../../../04_models/other_models/01_supervisados/trained_model_knn.pkl', 'rb') as f:
    modelo = pickle.load(f)


# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------

# IMPORTO DS PROCESSED

df_academico = pd.read_csv("../../../../01_data/02_processed/ds_academico.csv", sep=",") 
df_academico.head() 

# RECORTO DS PROCESSED

train_df, test_df = train_test_split(df_academico, test_size=0.1, random_state=42)


# EXPORTO DS PROCESSED EN TRAIN Y TEST
# conjunto de entrenamiento 
train_df.to_csv('../../../../01_data/03_train/ds_academico_train.csv', index=False)
# conjunto de prueba 
test_df.to_csv('../../../../01_data/04_test/ds_academico_test.csv', index=False)

# LEO NUEVO DS TRAIN CREADO EN EL PASO ANTERIOR

df_academico_train = pd.read_csv("../../../../01_data/03_train/ds_academico_train.csv", sep=",") 
df_academico_train.head(1) 


# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------

# SEPARO TARGET PARA MI MEJOR MODELO DE PREDICCION

X = df_academico_train[["Tuition fees up to date", "Scholarship holder", "Curricular units 1st sem (enrolled)", "Curricular units 1st sem (approved)", "Curricular units 2nd sem (enrolled)", "Curricular units 2nd sem (approved)"]]  
y = df_academico_train['Target']                 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
  

# ENTRENAMIENTO DEL MODELO
modelo.fit(X_train, y_train)

# PREDICCIONES
y_pred = modelo.predict(X_test)

# METRICAS DE RENDIMIENTO
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("Classification Report:")
print(classification_report(y_test, y_pred))


# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------


# python 02_training.py