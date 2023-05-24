import random

# Creación de las variables para los puntajes
river_puntaje = 0
boca_puntaje = 0

# Historial de enfrentamientos
enfrentamientos = [
    {"rival": "Boca Juniors", "local": "River Plate", "puntos_local": 0, "puntos_rival": 0},
    {"rival": "River Plate", "local": "Boca Juniors", "puntos_local": 0, "puntos_rival": 0},
    # Agrega más enfrentamientos aquí según la historia de la Copa Libertadores
]

# Simulación de los partidos
for enfrentamiento in enfrentamientos:
    local = enfrentamiento["local"]
    rival = enfrentamiento["rival"]
   
    # Simulación de los puntajes
    puntos_local = random.randint(0, 5)
    puntos_rival = random.randint(0, 5)
   
    enfrentamiento["puntos_local"] = puntos_local
    enfrentamiento["puntos_rival"] = puntos_rival
   
    # Actualización de los puntajes totales
    if local == "River Plate":
        river_puntaje += puntos_local
        boca_puntaje += puntos_rival
    else:
        river_puntaje += puntos_rival
        boca_puntaje += puntos_local

# Imprimir resultados
print("Historia de enfrentamientos en la Copa Libertadores entre River Plate y Boca Juniors:")
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
