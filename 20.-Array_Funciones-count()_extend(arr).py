#Codigo Python para desmotrar como funciona
#count() y extend(arr)

#Importamos "array para relizar operaciones de array
import array

#Inicializando matriz 1 con valores de matriz
#Inicializa la matriz de enteros con signo
arr1=array.array('i',[1, 2, 3, 1, 2, 5, 1])

#Inicializando matriz 2 con valores de matriz
#Inicaliza matriz de enteros con signo
arr2=array.array('i',[1, 2, 3])

#Usando count() para contar las aparaciones de 1 en la matriz
print("Las aparaciones de 1 en la matriz 1 son: ",end="")
print(arr1.count(1))

#Usando extend() para agregar elementos de matriz 2 a matriz 1
arr1.extend(arr2)

print("La matriz modificada es: ",end="")
for i in range(0, 9):
    print(arr1[i],end=" ")
