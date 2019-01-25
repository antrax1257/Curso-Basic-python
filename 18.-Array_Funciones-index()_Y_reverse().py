#Programa python, demostracion de como trabaja
#Las Funciones index() y reverse()

#Importando "array para operaciones de array(matrix)
import array

#Inicializando matriz(array) con valores de matriz
#Inicializa la matriz(array) con enteros y con signos
arr=array.array('i',[1,2,3,1,2,5,1,2,7,1,2,9])

#Imprimiendo array original
print("La nueva matriz(array) creada es: ",end="")
for i in range(0,12):
    print(arr[i],end=" ")
print("\r")

#Usando index() para
#Impirmir el indice de
#La primera aparicion de 2

print("El inidice de la primera  aparicion de 2 es en la posicion: ", end="")
print(arr.index(2))

#Usando
#Reverse() para invertir la matriz (array)
arr.reverse()
print("La matriz despues de la inversion es: ",end="")
for i in range(0, 12):
    print(arr[i],end=" ")
    
