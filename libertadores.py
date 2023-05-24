# Historial de enfrentamientos entre River Plate y Boca Juniors en la Copa Libertadores 2018
enfrentamientos = [
    {"rival": "Boca Juniors", "local": "River Plate", "puntos_local": 2, "puntos_rival": 2},
    {"rival": "Boca Juniors", "local": "River Plate", "puntos_local": 3, "puntos_rival": 1},
    # Agrega más enfrentamientos aquí según la historia de la Copa Libertadores 2018
]

# Variables para los puntajes totales
river_puntaje = 0
boca_puntaje = 0

# Simulación de los partidos
for enfrentamiento in enfrentamientos:
    local = enfrentamiento["local"]
    rival = enfrentamiento["rival"]
    puntos_local = enfrentamiento["puntos_local"]
    puntos_rival = enfrentamiento["puntos_rival"]
    
    # Actualización de los puntajes totales
    if local == "River Plate":
        river_puntaje += puntos_local
        boca_puntaje += puntos_rival
    else:
        river_puntaje += puntos_rival
        boca_puntaje += puntos_local

# Imprimir resultados
print("Historia de enfrentamientos en la Copa Libertadores 2018 entre River Plate y Boca Juniors:")
for enfrentamiento in enfrentamientos:
    local = enfrentamiento["local"]
    rival = enfrentamiento["rival"]
    puntos_local = enfrentamiento["puntos_local"]
    puntos_rival = enfrentamiento["puntos_rival"]
    
    print(f"{local} {puntos_local} - {puntos_rival} {rival}")

print("\nPuntaje total:")
print(f"River Plate: {river_puntaje} puntos")
print(f"Boca Juniors: {boca_puntaje} puntos")
#DANNY_URBINA
#DEPORTES
#IEM_ESCUELA_NORMAL_PASTO
#11_1
