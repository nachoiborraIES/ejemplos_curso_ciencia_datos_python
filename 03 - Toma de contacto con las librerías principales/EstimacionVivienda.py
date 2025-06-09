# Programa que usa Seaborn para construir un mapa de regresión para
# estimar el precio de venta de una vivienda

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

datos = pd.read_csv("precios_inmuebles.csv")

sns.regplot(x = "MetrosBajo", y = "Precio", data = datos)
plt.show()

