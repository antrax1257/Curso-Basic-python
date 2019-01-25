#Programa en Python
#Añadiendo elementos a un Set

#Creando un Set
set1=set()
print("Set inicial vacio: ")
print(set1)

#Añadiendo elementos al Set
set1.add(8)
set1.add(9)
set1.add(12)
set1.add(10)
set1.add(14)
print("\nConjunto despues de añadir 5 elementos: ")
print(set1)

#Añadiendo elementos a el Set
#Usando un Iterator(bucle for)
for i in range(1,6):
    set1.add(i)
print("\nConjunto despues de la Adicion de elementos del 1-5: ")
print(set1)

#Añadiedo Tuplas a un Conjunto(Set)
set1.add((6, 7))
print("\nConjunto despues de la adicion de una Tupla: ")
print(set1)

#Adicion de elmentos a un conjunto
#Utilizando la funcion de actualizacion(Update)
set1.update([10,11])
print("\nConjunto despues de la Adicion de elementos usando la Funcion de Actualizacion(Update):")
print(set1)
