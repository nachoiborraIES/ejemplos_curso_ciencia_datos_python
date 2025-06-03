# Programa que carga un archivo CSV y selecciona ciertas columnas

import pandas as pd

datos = pd.read_csv('casas_rurales.csv', sep=';')
datos = datos.loc[:, ['id','localidad','codigo_postal','nombre']]
datos = datos.astype({'id': 'int32', 'codigo_postal': 'int32'})
print(datos.dtypes)
datos.to_csv('casas_rurales_resumen.csv', index_label=False, sep=';')

# Comprobamos resultados
print("Datos guardados en fichero:")
datos2= pd.read_csv('casas_rurales_resumen.csv', sep=';')
print(datos2)
# Los tipos de datos cambiados no se guardan
print("Tipos de datos almacenados:")
print(datos2.dtypes)
