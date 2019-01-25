#Codigo en pytho para demostrar el tipo de conversion
#Usando Fucciones int(), float()

#nt(a,base) esta Funcion convierte cualquier tipo de datos a entero 'base'
#Especifica la base en la que se encuetra la cadena si el tipo de datos es una cadena

#float() Funcion que convierte cualquier tipo de datos a  un numero de punto flotante

#Inicializando la cadena
s="10010"

#Imprimiendo la cadena despues de convertir a int base 2
c=int(s,2)
print("Despues de convertir a base entera: ",end="")
print(c)

#Imprimiendo cadena convertida a float()
e=float(s)
print("Despues de convertir a float: ",end="")
print(e)
