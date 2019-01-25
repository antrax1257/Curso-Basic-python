#Codigo en python para ver como trabaja
#fromlist() Y tolist()

#Importamos "array" para operaciones de matriz
import array

#Inicializando array(matriz) con valores de matriz
#Inicializa el arraty con signos enteros
arr=array.array('i',[1, 2, 3, 1, 2, 5])

#Inicalizando lista
lista=[1, 2, 3]

#Usando fromlist() para agregar la lista al final de la matriz(array)
arr.fromlist(lista)
print("La matriz(array) modificada es: ",end="")
for i in range(0, 9):
    print(arr[i],end=" ")

#Usando tolist() para convertir la matriz(array) a una lista
lista2=arr.tolist()

print("\r")

#Imprimiendo la nueva lista
print("La nueva lista creada es: ",end="")
for i in range(0,len(lista2)):
    print(lista2[i],end=" ")
