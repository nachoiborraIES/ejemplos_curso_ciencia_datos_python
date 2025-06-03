# Programa que crea una serie de Pandas con notas de alumnos y las procesa

import pandas as pd

notas = {'1111': 8.5, '2222': 4, '3333': 6.2, '4444': 9.8}
serie = pd.Series(notas)
serie = serie[serie >= 5].sort_values(ascending=False)
print(serie)
