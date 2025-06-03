# Ejemplo de acceso a filas y columnas en data frames de Pandas

import pandas as pd

datos = { 'Nombre': ['Nacho', 'Juan', 'Ana'],
    'Email': ['nacho@gmail.com', 'jperez@gmail.com', 'anaib@gmail.com'],
    'Edad': [44, 70, 40],
    'Telefono': ['611223344', '699887766', '619283746']}
dataFrame = pd.DataFrame(datos)

# Acceso a casillas sueltas
# Error -> print(dataFrame.loc[0, 1])
print(dataFrame.loc[0, 'Email'])
print(dataFrame.iat[0, 1])

# Acceso a rangos
print(dataFrame.loc[0:2, 'Nombre':'Edad'])
print(dataFrame.iloc[[0, 2], 0:2])
print(dataFrame[0:2])
print(dataFrame['Nombre'])
print(dataFrame[['Nombre', 'Edad']])
print(dataFrame[['Nombre']])

# Cambiar índices
dataFrame = dataFrame.set_index('Email')
print("Edad de Nacho:", dataFrame.loc['nacho@gmail.com', 'Edad'])
dataFrame.reset_index(inplace=True)
print(dataFrame)

# Recorrido
print("Recorrido con índice y columna:")
for index, row in dataFrame.iterrows():
    for columna in dataFrame.columns:
        print(dataFrame.loc[index, columna])

print("Recorrido con posiciones numéricas:")
for i in range(len(dataFrame)):
    for j in range(len(dataFrame.columns)):
        print(dataFrame.iloc[i, j])

# Tipos de datos
print("Tipos de datos del data frame:")
print(dataFrame.dtypes)
dataFrame = dataFrame.astype({'Edad': 'int32'})
print("Tipos de datos del data frame tras cambio:")
print(dataFrame.dtypes)
