#Creando un Diccionario vacio
Dict={}
print("Diccionario vacio: ")
print(Dict)

#Añadiendo elementos uno a la vez
Dict[0]={"Geeks"}
Dict[1]={"For"}
Dict[2]={"Geeks"}
Dict[3]=1

print("\nDiccionario despues de añadir 3 elementos: ")
print(Dict)

#Sumando conjunto de valores
#A una sola llave
Dict['Value_Conjunto']=2,3,4
print("\nDiccionario despues de agregar 3 elementos: ")
print(Dict)

#Actualiza rel valor de la clave existente
Dict[2]="Bienvenido"
print("\nValor con clave actualizada: ")
print(Dict)

#Agreagar valor de clave anidada al Diccionario
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Geeks'}} 
print("\nAñadiendo una clave anidada: ") 
print(Dict) 
