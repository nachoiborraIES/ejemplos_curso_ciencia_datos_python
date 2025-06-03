# Programa que crea un data frame de Pandas con datos predefinidos

import pandas as pd
from tabulate import tabulate

datos = {'Mes': ['Enero', 'Abril', 'Julio', 'Octubre'],
    'Ventas': [20600, 22500, 15400, 21100],
    'Gastos': [17900, 18500, 17600, 18200]}

df = pd.DataFrame(datos)
print(tabulate(df, headers="keys", tablefmt="pretty"))
df.info()
print("Columnas:", df.shape[1])
df.to_csv('archivo2.csv', index=False)
