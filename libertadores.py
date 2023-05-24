import pandas as pd

# Cargar datos de los deportistas colombianos en los Juegos Olímpicos
data = pd.read_csv('deportistas_colombianos.csv')

# Filtrar los deportistas por medallas ganadas
medallistas = data[data['Medallas'] > 0]

# Ordenar los deportistas por año de participación
medallistas = medallistas.sort_values('Año')

# Imprimir la información de los deportistas medallistas
for index, deportista in medallistas.iterrows():
    print(f"Deportista: {deportista['Nombre']}")
    print(f"Año: {deportista['Año']}")
    print(f"Medalla: {deportista['Medallas']}")
    print("")

# Calcular el total de medallas ganadas por Colombia
total_medallas = medallistas['Medallas'].sum()
print(f"Total de medallas ganadas por Colombia: {total_medallas}"
#DANNY_URBINA
#DEPORTES
#IEM_ESCUELA_NORMAL_PASTO
#11_1
