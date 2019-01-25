#Codigo en Python para demostrar el funcionamiento de
#typecode, itemsize, buffer_info()

#Importamos "array para operaciones de array(matriz)
import array

#Inicializadno el array con valores
#Inicializa la matriz entera con signo
arr=array.array('i',[1,2,3,1,2,5])

#Usando typecode para imprimir en tipo de dato del array(matriz)
print("El tipo de datos de la matriz es: ",end="")
print(arr.typecode)

#Usando itemsize para
#Imprimir el tamaño de la matriz(array)
print("El tamaño del elemento de la matriz es: ",end="")
print(arr.itemsize)

#Usando buffer_info() para imprimir
#Informacion del bufer de la matriz
print("EL bufer de informacion de matriz es: ",end="")
print(arr.buffer_info())
