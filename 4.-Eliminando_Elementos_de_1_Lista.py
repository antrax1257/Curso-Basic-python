#Removiendo Elementos de una lista

#Creando una lista
List=[1,2,3,4,5,6,
      7,8,9,10,11,12]
print("Lista Inicial")
print(List)

#Removiendo elementos de List
#Hacemos uso del Metodo Remove()
#Remove() elimina elementos de la lista
List.remove(5)
List.remove(6)
print("\nLista depues de eliminar elementos 5 y 6 de la lista inicial: ")
print(List)

#Removiendo elementos de la lista
#Usando un Metodo interador
for i in range(1, 5):
    List.remove(i)
print("\nLista despues de saltar los elementos 1-5: ")
print(List)

#Removiendo un elemento
#Especificando su  localizacion de el
#Utilizamos el metodo pop()
List.pop(2)
print("\nLista despues de resaltar un elemento especifico: ")
print(List)
