# Programa que usa Matplotlib para crear un array de múltiples gráficos
# sobre un dataset determinado

import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("parques_eolicos.csv", sep=";")

# Cálculos previos para cada gráfico

# Conteo de parques por provincia
parques_provincia = datos['provincia'].groupby(datos['provincia']).count()
# Potencia media por provincia
potencia_provincia = datos['potencia'].groupby(datos['provincia']).mean()
# Número de generadores en Valladolid y Palencia
generadores_valladolid = datos[datos['provincia'] == 'VA']['aerogeneradores']
generadores_palencia = datos[datos['provincia'] == 'PA']['aerogeneradores']

# Array de gráficos

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))

# Conteo de parques por provincia
ax[0, 0].pie(parques_provincia, labels=parques_provincia.index)
ax[0, 0].set_title("Parques por provincia")

# Potencia media por provincia
ax[0, 1].bar(potencia_provincia.index, potencia_provincia)
ax[0, 1].set_title("Potencia media por provincia")

# Histograma con frecuencias de número de aerogeneradores
ax[1, 0].hist(datos['aerogeneradores'], bins=8)
ax[1, 0].set_title("Número de aerogeneradores")

# Gráfico de cajas con el número de aerogeneradores en Valladolid y Palencia
ax[1, 1].boxplot([generadores_valladolid, generadores_palencia], 
    tick_labels=["VA", "PA"])
ax[1, 1].set_title("Aerogeneradores en VA y PA")

plt.show()
