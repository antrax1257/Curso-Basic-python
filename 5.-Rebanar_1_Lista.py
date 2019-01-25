#Slice sirve para imprimir un rango espefico de elementos de la Lista

#Programa en Python para la demostracion de
#Eliminacion de elementos de una lista

#Creando la lista
List=["G","E","E","K","S","F",
      "O","R","G","E","E","K","S"]
print("Lista inicial: ")
print(List)

#Imprimir elementos de una rango
#Utilizando la operacion Slice 
#Slice es operacion de rebanada de una lista
Sliced_List=List[3:8]
print("\nCortar elementos en un rango de 3-8: ")
print(Sliced_List)

#Imprimir elementos desde el principio
#A un punto pre-definido utilizando
#Slice
#Para imprimir elementos desde el final use [: -Index]
Sliced_List=List[:-6]
print("\nElementos cortados hasta el 6to elemento de la lista: ")
print(Sliced_List)

#Imprimir elementos de un
#Punto pre-definido al final
#Para imprimir elementos desde un Índice específico hasta el final use [Índice:]
Sliced_List=List[5:]
print("\nElementos cortados desde el quinto elemento hasta el final: ")
print(Sliced_List)

#Impresion de elementos desde
#El comienzo hasta el final
#La operacion de corte se realiza en listas con el uso de (:)
Sliced_List=List[:]
print("\nImprimiendo elementos utilizando la operacion de corte: ")
print(Sliced_List)

#Imprimiendo elementos al reves
#Usando la operacion Slice
#Para imprimir la Lista completa en orden inverso, use [:: - 1]
Sliced_List=List[::-1]
print("\nImprimiendo Lista a la inversa: ")
print(Sliced_List)
