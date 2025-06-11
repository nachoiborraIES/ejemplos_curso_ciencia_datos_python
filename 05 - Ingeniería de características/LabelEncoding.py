# Ejercicio para codificar columnas usando "label encoding"

import pandas as pd

datos = pd.read_csv('datos_salud.csv')

# Codificaciones "label encoding" de "cholesterol" y "gluc"
datos['cholesterol'] = datos['cholesterol'].map({'Normal':0, 'Above Normal':1,
    'Well Above Normal':2})
datos['gluc'] = datos['gluc'].map({'Normal':0, 'Above Normal':1,
    'Well Above Normal':2})

# Codificaciones binarias de columnas SI/NO
datos['smoke'] = datos['smoke'].map({'No':0, 'Yes':1})
datos['alco'] = datos['alco'].map({'No':0, 'Yes':1})
datos['active'] = datos['active'].map({'No':0, 'Yes':1})
datos['cardio'] = datos['cardio'].map({'No':0, 'Yes':1})

# Vemos cómo queda el dataset
print(datos.head())