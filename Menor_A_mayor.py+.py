def cadena(lista):
    lista2=sorted(lista, key=len)
    return lista2

lista=["\nPython","Lenguaje","Programacion","mundo","aprendizaje","hack"]
print(cadena(lista))
