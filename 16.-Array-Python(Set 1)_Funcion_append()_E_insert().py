#Codigo en python para demostrar como trabaja el
#array(), append(), insert()

#Importando "array"(matriz) para operaciones de matriz
import array

#Inicializadno matriz(array) con valores de matrz
#Inicializando la matriz con enteros  y con signos
arr=array.array('i',[1,2,3,4,5])

#Imprimiendo el array original
print("La nueva matriz(array) creada es: ", end=" ")
for i in range(0, 5):
    print(arr[i],end=" ")

print("\r")

#Usando append()
#Para insertar un
#Nuevo valor al final
arr.append(4);

#Matriz(array) de impresion
#append()
print("La matriz(array) nueva es :", end="")
for i in range(0, 4):
    print (arr[i], end=" ")

#Usando insert() par insertar un valor
#En una posicion especifica
#Inserta 5 en la 2da posicion
arr.insert(2, 5)
print("\r")

#Matriz(array) de impresion
#Despues de la intersecion
print("La matriz(array) despues de la intersesion es: ",end="")
for i in range(0, 5):
    print(arr[i], end=" ")
    
