# Creating a Set(Conjunto)
set1 = set([1, 2, 3, 4, 5, 6,  
            7, 8, 9, 10, 11, 12]) 
print("Conjunto Inicial: ") 
print(set1)

#Removiendo elementos del Conjunto
#Usando el Metodo Remove()
set1.remove(5)
set1.remove(6)
print("\nConjunto despues de remover 2 elementos: ")
print(set1)

#Removiendo elementos del Conjunto
#Usando el Metodo Discard()
set1.discard(8)
set1.discard(9)
print("\nConjunto despues de descartar 2 elementos: ")
print(set1)

#Removiendo elementos del
#Conjunto usando el Metodo Iterator(bucle)
for i in range(1, 5):
    set1.remove(i)
print("\Conjunto despues de remover un rango de elementos: ")
print(set1)

#Eliminando elementos del
#Conjunto usando el
#Metodo pop()
set1.pop()
print("\nConjunto despues de resaltar un elemento: ")
print(set1)

#Removiendo elementos del
#Conjuntunto Usando el MEtodo clear()
set1.clear()
print("\nConjunto despues de borrar todos los elementos: ")
print(set1)


