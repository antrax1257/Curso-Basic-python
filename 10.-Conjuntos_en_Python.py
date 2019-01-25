#Programa en python para la demostracion de creacion de conjuntos
#Creando un set en Python

#Creando un Set
set1=set()
print("Conjunto inicial en blanco: ")
print(set1)

#Creando un Set
#Con el uso de una Cadena
set1=set("PythonforHacking")
print("\nConjunto con el uso de una Cadena: ")
print(set1)

#Creando un Set con
#El uso de un constructor
#Usando un objeto para almacenar cadena
String="python hacking"
set1=set(String)
print("\nConjunto con el uso de un objeto: ")
print(set1)

#Creando un Set con
#El uso de una Lista
set1=set(["Geeks", "Python", "Programacion"])
print("\nConjunto con el uso de una Lista: ")
print(set1)

#Creando un Set con
#Una Lista de numeros
#(Puede tener valores duplicados)
set1=set([1,2,3,4,5,4,4,5,5,6,])
print("\nConjunto con el uso de una Lista de numeros: ")
print(set1)

#Creando un Set con
#Un tipo  mixto de valores
#(Puede tener numeros y cadenas)
set1=set([1,2,"Python",4,"for",6,"Programacion"])
print("\nConjuntocon el uso de valores mixtos: ")
print(set1)
