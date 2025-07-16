import requests

def consultar_api(url):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza error si la solicitud no fue exitosa
        datos = respuesta.json()
        return datos
    except requests.exceptions.RequestException as e:
        print(f"Error al consultar la API: {e}")
        return None

def mostrar_datos_api(datos):
    if datos is None:
        print("No se pudieron obtener datos de la API.")
        return
    
    print("\nDatos obtenidos de la API:")
    if isinstance(datos, dict):
        for clave, valor in datos.items():
            print(f"{clave}: {valor}")
    elif isinstance(datos, list):
        for item in datos[:5]:  # Mostrar solo los primeros 5 elementos si es una lista
            print(item)

def main():
    # Lista de APIs públicas para probar
    apis = [
        "https://api.github.com/users/octocat",
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://api.agify.io?name=meelad"
    ]
    
    for api_url in apis:
        print(f"\nConsultando API: {api_url}")
        datos = consultar_api(api_url)
        mostrar_datos_api(datos)

if __name__ == "__main__":
    main()