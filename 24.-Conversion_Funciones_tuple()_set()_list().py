#Codigo en python para demostrar Tipo de conversion
#Usando tuple(), set(), list()

#tupla() Funcion que se utiliza para convertir a una tupla
#set()Funcion que devuelve el tipo despues de convertir a set
#list() Funcion que se utiliza para convertir cualquier tipo de datos a un tipo de lista .

#Inicializando cadena
s='Python'

#Impresion de la cadena de conversion a tupla()
c=tuple(s)
print("Despues de convertir la cadena en tupla: ",end="")
print(c)

#Impresion de la cadena de conversion a establecer set()
c=set(s)
print("Despues de convertir la cadena a set(): ",end="")
print(c)

#Impresion de la cadena convertida a lista
c=list(s)
print("Despues de convertir la cadena a una lista: ", end="")
print(c)
