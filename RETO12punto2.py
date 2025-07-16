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