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