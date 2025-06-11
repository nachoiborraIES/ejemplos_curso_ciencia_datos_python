# Ejemplos de escalado de datos

import pandas as pd

datosIniciales = { 'Nombre': ['Juan', 'Ana', 'Mario', 'Laura'],
                   'Edad': [70, 40, 30, 26],
                   'Sueldo': [2800, 1200, 1750, 1420]
}
datos = pd.DataFrame(datosIniciales)

# Escalado por normalización
datos['Edad'] = (datos['Edad'] - datos['Edad'].min()) / \
    (datos['Edad'].max() - datos['Edad'].min())

# Escalado por estandarización
datos['Sueldo'] = (datos['Sueldo'] - datos['Sueldo'].mean()) / \
    datos['Sueldo'].std()

print(datos)