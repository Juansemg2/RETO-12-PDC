# RETO 12 PDC

Juan Sebastian Martinez Garcia

1.Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.

    def imprimir_valores_ascendentes(diccionario):
        # Convertir los valores a una lista
        valores = list(diccionario.values())
        
        # Ordenar la lista con el método de burbuja (básico)
        n = len(valores)
        for i in range(n):
            for j in range(0, n-i-1):
                if valores[j] > valores[j+1]:
                    # Intercambiar elementos
                    valores[j], valores[j+1] = valores[j+1], valores[j]
        
        # Imprimir los valores ordenados
        print("Valores ordenados de manera ascendente:")
        for valor in valores:
            print(valor)
    
    # Ejemplo
    mi_diccionario = {'a': 4, 'b': 2, 'c': 3, 'd': 1}
    imprimir_valores_ascendentes(mi_diccionario)

2.Desarrollar una función que reciba dos diccionarios como parámetros y los mezcle, es decir, que se construya un nuevo diccionario con las llaves de los dos diccionarios; si hay una clave repetida en ambos diccionarios, se debe asignar el valor que tenga la clave en el primer diccionario.

    def mezclar_diccionarios(dic1, dic2):
        diccionario_mezclado = {}
        
        # Primero agregamos las claves del segundo diccionario
        for clave in dic2:
            diccionario_mezclado[clave] = dic2[clave]
        
        # Luego agregamos las claves del primer diccionario
        # Si hay repetidas, se sobreescriben con los valores del primero
        for clave in dic1:
            diccionario_mezclado[clave] = dic1[clave]
        
        return diccionario_mezclado
    
    # Ejemplo
    diccionario1 = {'a': 1, 'b': 2, 'c': 3}
    diccionario2 = {'c': 4, 'd': 5, 'e': 6}
    resultado = mezclar_diccionarios(diccionario1, diccionario2)
    print("Diccionario mezclado:", resultado)

3.Dado el JSON:

    {
    	"jadiazcoronado":{
    		"nombres": "Juan Antonio",
    		"apellidos": "Diaz Coronado",
    		"edad":19,
    		"colombiano":true,
    		"deportes":["Futbol","Ajedrez","Gimnasia"]
    	},
    	"dmlunasol":{
    		"nombres": "Dorotea Maritza",
    		"apellidos": "Luna Sol",
    		"edad":25,
    		"colombiano":false,
    		"deportes":["Baloncesto","Ajedrez","Gimnasia"]
    	}
    }

Cree un programa que lea de un archivo con dicho JSON y:

Imprima los nombres completos (nombre y apellidos) de las personas que practican el deporte ingresado por el usuario.
Imprima los nombres completos (nombre y apellidos) de las personas que estén en un rango de edades dado por el usuario.

    import json
    
    def cargar_datos_desde_archivo(nombre_archivo):
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
        return datos
    
    def buscar_por_deporte(datos, deporte):
        print(f"\nPersonas que practican {deporte}:")
        for usuario, info in datos.items():
            if deporte in info['deportes']:
                nombre_completo = f"{info['nombres']} {info['apellidos']}"
                print(nombre_completo)
    
    def buscar_por_rango_edades(datos, edad_min, edad_max):
        print(f"\nPersonas con edades entre {edad_min} y {edad_max} años:")
        for usuario, info in datos.items():
            if edad_min <= info['edad'] <= edad_max:
                nombre_completo = f"{info['nombres']} {info['apellidos']}"
                print(nombre_completo)
    
    def main():
        # Suponiendo que el archivo se llama 'datos.json'
        datos = cargar_datos_desde_archivo('datos.json')
        
        # Opción 1: Buscar por deporte
        deporte = input("Ingrese el deporte a buscar: ")
        buscar_por_deporte(datos, deporte)
        
        # Opción 2: Buscar por rango de edades
        print("\nIngrese un rango de edades:")
        edad_min = int(input("Edad mínima: "))
        edad_max = int(input("Edad máxima: "))
        buscar_por_rango_edades(datos, edad_min, edad_max)
    
    if __name__ == "__main__":
        main()

4.A través de un programa conectese a al menos 3 API's , obtenga el JSON, imprimalo y extraiga los pares de llave : valor.

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
