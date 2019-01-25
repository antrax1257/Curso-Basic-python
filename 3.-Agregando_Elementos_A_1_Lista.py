#Este codigo Agregara elementos a una lista
#Creando la lista
List=[]
print("Lista inicial en blanco: ")
print(List)

#Añadiendo los elementos
#A la Lista
#append para añadir elementos
List.append(1)
List.append(2)
List.append(3)
List.append(4)
List.append(5)
print("\nImprimiendo la Lista despues de agregar 5 elementos: ")
print(List)

#Añadiendo elementos a la lista
#Usamos un Interador(for)
#Los elementos se agregan en range 1-5
for i in range(1, 5):
    List.append(i)
print("\nImprimiendo la Lista despues de agregar elementos del 1-5: ")
print(List)

#Añadiendo Tuplas a la Lista Anterior
#Se agrega el elemento 5 y 6
List.append((5, 6))
print("\nImprimiendo la Lista despues de Añadir la tupla: ")
print(List)

#Adicion de una lista a una lista(A LA ANTERIOR)
List2=["For","Hacking","Google","python"]
List.append(List2)
print("\nLista despues de añadir una Lista A la Lista: ")
print(List)

#Adicion de Un elemento
#Especificacion de una posicion
#(Usando el Metodo Insert)
#Insert añade elementos a la posicion deseada
List.insert(3, 12)
List2.insert(0, "Geeks")
print("\nLista despues de usar el Metodo insert: ")
print(List)

#Adicion de multiples elementos
#A la Lista en la posicion final
#Usando el Metodo Extend
#Extend es un Metodo que agrega varios elementos
#Al mismo tiempo  al final de la lista
List.extend([8, "Geeks", "Inteligencia Artificial"])
print("\nLista despues de Hacer uso del Metodo Extend: ")
print(List)



