#Diccionario Inicial
Dict={5: 'Bienvenido', 6: 'pagina', 7: 'Geeks',
      'A' : {1: 'Geeks', 2: 'For', 3: 'Geeks'},
      'B' : {1: 'Geeks', 2: 'Vida'},
      'C' : {1: 'Python', 2: 'Hacking'}}
print("Diccionario Inicial: ")
print(Dict)

#Eliminando un valor de clave
del Dict[6] 
print("\nEliminando un Clave especifica: ")
print(Dict)

#Eliminar la clave
#De un Diccionario anidado
del Dict['A'][2]
print("\nEliminar una clave del Diccionario anidado: ")
print(Dict)

#Borrando una clave
#Usanco pop()
Dict.pop(5)
print("\nPopping elemento especifico: ")
print(Dict)

#Borrando una clave
#Usando popitem()
Dict.popitem()
print("\nPops primer elemento: ")
print(Dict)

#Haciendo copia de el DICCIONARIO
Dict.copy()
print("\nCopiando todo el Diccionario: ")
print(Dict)

#Eliminar todo el Diccionario
Dict.clear()
print("\nElimianando todo el Diccionario: ")
print(Dict)

