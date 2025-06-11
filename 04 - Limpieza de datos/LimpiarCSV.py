# Ejercicio para practicar otras tareas de limpieza de datos

import pandas as pd

datos = pd.read_csv('archivo.csv')

print("Datos iniciales:")
print(datos)

# Homogeneizar nombres
datos['nombre'] = datos['nombre'].str.title()
print("Datos con nombres homogeneizados:")
print(datos)

# Detectar y eliminar filas duplicadas
print("Filas duplicadas:")
print(datos.duplicated())
print("Datos sin filas duplicadas")
datos = datos.drop_duplicates()
print(datos)

# Espacios en provincia
datos['provincia'] = datos['provincia'].str.strip()
print("Datos con provincias sin espacios:")
print(datos)