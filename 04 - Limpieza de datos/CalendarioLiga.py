# Programa que carga el calendario de liga de la temporada 2022-23, reindexa
# el dataset por el campo de fecha y obtiene los partidos del mes de octubre

import pandas as pd

datos = pd.read_csv('liga_22_23.csv')
datos['Date'] = pd.to_datetime(datos['Date'], format='%d-%m-%Y')
datos = datos.set_index('Date').sort_index()

octubre_22 = datos.loc['2022-10']
print(octubre_22.shape[0], "partidos en octubre")
print(octubre_22)
