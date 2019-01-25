#Programa de Python para demostracion de Tuplas
#Adicion de elementos a un Conjunto

#Creando una Tupla vacia
Tupla1=()
print("Tupla inical vacia: ")
print(Tupla1)

#Creando una Tupla
#Con el uos de cadenas
Tupla1=('Geeks', 'For')
print("\Tupla con el uso de una cadena: ")
print(Tupla1)

#Creando un Tupla con
#El uso de la lista
Lista1=[1,2,3,4,5,6,7,8,9,10]
print("\nTupla usando una Lista: ")
print(tuple(Lista1))

#Creando una Tupla
#Con el uso de un bucle
Tupla1=('Python')
n=5
print("\nTupla con un bucle: ")
for i in range(int(n)):
    Tupla1=(Tupla1, )
    print(Tupla1)

#Creando una Tupla con el
#Uso de la funcion incorporada tuple
Tupla1=tuple('Python es genial ')
print("\nTupla con el uso de la funcion: ")
print(Tupla1)

#Creando Tupla con el
#Uso de datos mixrtos
Tupla1=(5, 'Bienvenido', 7, 'Python')
print("\nTpla con uso de datos Mixtos: ")
print(Tupla1)

#Creando una Tupla
#Con Tuplas anidadas
Tupla1=(0,1,2,3,4,5)
Tupla2=('python','linux')
Tupla3=(Tupla1, Tupla2)
print("\nTupla con tuplas anidadas: ")
print(Tupla3)

#Creando un Tupla
#Con repeticion
#Tupla1 se repetira 3 veces
Tupla1=('python',) *3
print("\nTupla con repeticion: ")
print(Tupla1)
