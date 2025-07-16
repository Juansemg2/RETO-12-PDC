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