#Codigo en Python para demostrar el Tipo de Conversion
#Usando Funciones ord(), hex(), oct()

#ord (): esta función se utiliza para convertir un carácter a entero.
#hex (): esta función es convertir un entero en una cadena
#oct (): esta función es convertir un entero en una cadena octal .

#Inicializando Entero
s='4'
#Impresion de caracteres convirtiendo a entero
c=ord(s)
print("Despues de convertir el caracter a entero: ",end="")
print(c)

#Imprimiendo enteros convirtiendo a cadena hexadecial
c=hex(56)
print("Despues de convertir 56 a cadena hexadecimal: ",end=" ")
print(c)

#Imprimeindo entero a una cadena octal
c=oct(56)
print("Despues de convertir 56 a cadena octal",end="")
print(c)
