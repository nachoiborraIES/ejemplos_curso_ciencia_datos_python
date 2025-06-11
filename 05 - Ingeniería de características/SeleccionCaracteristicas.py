# Ejemplo de selección de columnas relevantes usando correlación

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

datos = pd.read_csv('precios_inmuebles.csv')
datos = datos.drop('Barrio', axis=1)

# Mapa de calor de correlación
heatmap = sns.heatmap(datos.corr(), vmin=-1, vmax=1, annot=True)
heatmap.set_title("Correlaciones venta inmuebles")
plt.show()

# Las columnas relevantes son los metros del bajo, de la primera planta,
# número de aseos y año de construcción (junto con el objetivo, el precio)
columnas_relevantes = ['MetrosBajo', 'Metros1P', 'Aseos', 'Anyo', 'Precio']
datos = datos[columnas_relevantes]
print(datos.head())
