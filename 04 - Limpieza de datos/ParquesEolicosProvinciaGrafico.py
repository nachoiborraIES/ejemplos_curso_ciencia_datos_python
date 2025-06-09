# Programa que carga un archivo CSV con datos faltantes y los rellena
# para calcular algunas estadísticas y gráficos

import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv('parques_eolicos2.csv', sep=';')
datos = datos[['provincia', 'potencia']]
# Reemplazamos con la moda
datos['potencia'].fillna(datos['potencia'].mode()[0], inplace=True)
# Reemplazamos con la media
#datos['potencia'].fillna(datos['potencia'].mean(), inplace=True)

datos = datos.groupby(datos['provincia']).mean()
print(datos)

# Gráfico de barras
datos.plot.bar()
plt.xlabel("Provincias")
plt.ylabel("Potencia media")
plt.show()
