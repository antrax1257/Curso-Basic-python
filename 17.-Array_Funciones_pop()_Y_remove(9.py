#Programa en python para desmostracion de como trabaja
#pop() y remove()

#Importando "array" para operaciones de matriz(array)
import array

#Inicializando matriz con valores de
#Inicializa la matriz con enteros  y signos
arr=array.array('i',[1,2,3,1,5])
print("La nueva matriz(array) creada es: ", end="")
for i in range(0, 5):
    print(arr[i],end=" ")
print("\r")

#Usando pop() para eliminar el
#Elemento en la segunda posicion
print("EL elemento que aparece en la segunda posicion es: ",end="")
print(arr.pop(2));

#Matriz(array) de impresion despues
#De hacer estallar
print("La matriz despue de hacer estallar es: ",end="")
for i in range(0, 3):
    print(arr[i],end=" ")
print("\r")

#Imprimiendo array despues
#De usar la funcion remove()
arr.remove(1)
print("La matriz despues de eliminar es: ", end="")
for i in range(0, 3):
    print(arr[i],end=" ")
