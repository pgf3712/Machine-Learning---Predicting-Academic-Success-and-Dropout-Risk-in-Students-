# IMPORTO LIBRERIAS

from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle


# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------

# IMPORTO DS PROCESSED

df_academico = pd.read_csv("../01_data/02_processed/ds_academico.csv", sep=",") 
df_academico.head() 

# RECORTO DS PROCESSED

train_df, test_df = train_test_split(df_academico, test_size=0.1, random_state=42)


# EXPORTO DS PROCESSED EN TRAIN Y TEST
# conjunto de entrenamiento 
train_df.to_csv('../01_data/03_train/ds_academico_train.csv', index=False)
# conjunto de prueba 
test_df.to_csv('../01_data/04_test/ds_academico_test.csv', index=False)

# LEO NUEVO DS TRAIN CREADO EN EL PASO ANTERIOR

df_academico_train = pd.read_csv("../01_data/03_train/ds_academico_train.csv", sep=",") 
df_academico_train.head(1) 


# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------

# SEPARO TARGET PARA MI MEJOR MODELO DE PREDICCION
x = df_academico_train.drop(columns=['Target'])  
y = df_academico_train['Target']                 
print(x)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

mi_mejor_modelo = Pipeline([
    ('scaler', StandardScaler()),
    ('logreg', LogisticRegression(C=1, penalty='l1', solver='liblinear', random_state=42))
])

# ENTRENAMIENTO DEL MODELO
mi_mejor_modelo.fit(X_train, y_train)

# PREDICCIONES
y_pred = mi_mejor_modelo.predict(X_test)

# METRICAS DE RENDIMIENTO
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("Classification Report:")
print(classification_report(y_test, y_pred))


# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------

# EXPORTO A PICKLE

# Guardo mi modelo

with open('../04_models/final_model_f.pkl', 'wb') as f:
    print("Creado")
    pickle.dump(mi_mejor_modelo, f) 
