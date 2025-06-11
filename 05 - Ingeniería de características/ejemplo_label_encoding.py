# Ejemplo de uso de "label encoding"

import pandas as pd

datos = { 'Nacionalidad': ['España', 'Portugal', 'España', 'Francia',
                           'Portugal', 'España'],
          'Edad': [34, 38, 30, 40, 37, 32],
          'Peso': [88.4, 95.6, 90.2, 96.7, 99.3, 82.4],
          'Socio': ['Si', 'Si', 'No', 'No', 'Si', 'Si']}

df = pd.DataFrame(datos)

# Asignación arbitraria de valores

df['Nacionalidad'] = df['Nacionalidad'].astype('category')
df['Cod_Nacionalidad'] = df['Nacionalidad'].cat.codes
print("Datos con columna generada con cat.codes:")
print(df)

# Asignación manual de valores
df['Cod_Nacionalidad2'] = df['Nacionalidad'].map({
    'España': 0, 'Portugal': 1, 'Francia': 2
})
print("Datos con columna generada manualmente:")
print(df)