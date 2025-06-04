# Programa que carga un archivo CSV y filtra datos por provincia y potencia

import pandas as pd

datos = pd.read_csv('parques_eolicos.csv', sep=';')
datos = datos[(datos['provincia'] == 'ZA') & (datos['aerogeneradores'] > 10)]
datos = datos.sort_values(by='aerogeneradores')
print(datos)
