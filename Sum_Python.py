import pandas as pd

# Leer los datos históricos de los partidos de Boca Juniors en la Primera División
boca_juniors = pd.read_csv("boca_juniors.csv")

# Calcular el total de partidos jugados
total_partidos = len(boca_juniors)

# Calcular el total de victorias, empates y derrotas
victorias = len(boca_juniors[boca_juniors['Resultado'] == 'V'])
empates = len(boca_juniors[boca_juniors['Resultado'] == 'E'])
derrotas = len(boca_juniors[boca_juniors['Resultado'] == 'D'])

# Calcular el porcentaje de victorias, empates y derrotas
porcentaje_victorias = (victorias / total_partidos) * 100
porcentaje_empates = (empates / total_partidos) * 100
porcentaje_derrotas = (derrotas / total_partidos) * 100

# Imprimir los resultados
print("Total de partidos: ", total_partidos)
print("Victorias: ", victorias, "(", porcentaje_victorias, "%)")
print("Empates: ", empates, "(", porcentaje_empates, "%)")
print("Derrotas: ", derrotas, "(", porcentaje_derrotas, "%)")
