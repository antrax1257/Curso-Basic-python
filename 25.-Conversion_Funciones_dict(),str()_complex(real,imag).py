#Codigo en Python para demostrar el
#Uso de dict(), complex(), str()

 #dict (): esta función se utiliza para convertir una tupla de orden (clave, valor) en un diccionario .
 #str (): se utiliza para convertir un entero en una cadena.
# complex(real, imag):: esta función convierte los números reales en complejos (real,

#Inicializando Enteros
a=1
b=2

#Inicializando tupla
tupla=(('a', 1) ,('f', 2) , ('g', 3))

#Impime entero convirtiendo a numero complejo
c=complex(1, 2)
print("Despues de convertir un entero en un numero complejo: ",end="")
print(c)

#Imprimiendo enteo convertido a cadena
c=str(a)
print("Despues de convertir un enteo en una cadena: ",end="")
print(c)

#Imprimiendo tupla convertida a un diccionario
c=tuple(tupla)
print("Despues de convertir la Tupla al diccionario: ",end="")
print(c)
