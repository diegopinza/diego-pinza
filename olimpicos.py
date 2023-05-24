import requests

def obtener_medallistas_olimpicos():
    url = "https://api.com/medallistas" # Reemplaza con la URL correcta de la API de medallistas olímpicos
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("No se pudo obtener la información de los medallistas olímpicos")
            return None
    except requests.exceptions.RequestException as e:
        print("Error de conexión:", e)
        return None

def mostrar_historia_olimpica(medallistas):
    if medallistas is not None:
        for medallista in medallistas:
            nombre = medallista["nombre"]
            deporte = medallista["deporte"]
            medallas = medallista["medallas"]
            
            print(f"{nombre} ha ganado {medallas} medallas en {deporte} en los Juegos Olímpicos.")

# Obtener la lista de medallistas olímpicos
medallistas_olimpicos = obtener_medallistas_olimpicos()

# Mostrar la historia olímpica de los deportistas colombianos
mostrar_historia_olimpica(medallistas_olimpicos)
