#Codigo en Python para demostrar codificacion de una Cadena

#Inicializando Cadena
a='PythonProgramacion'

#Inicializando un Objeto Byte
c= b'PythonProgramacion'

#Usando encode() para codificar la Cadena
#La version codificada se almacena utilizando
#El mapeo ASCII
d=a.encode('ASCII')

#Checando si esta convertido a Bytes o no
if(d==c):
    print("Codificacion Exitosa: ")
else:
    print("La Codificacion ha Fallado: ")



print("\nDecodificacion de la cadena:")

#Inicializando Cadena
a='PythonProgramacion'

#Inicializando un Objeto Byte
c= b'PythonProgramacion'

#Usando encode() para codificar la Cadena
#La version codificada se almacena utilizando
#El mapeo ASCII
d=c.decode('ASCII')

#Checando si esta convertido a Bytes o no
if(d==a):
    print("DeCodificacion Exitosa: ")
else:
    print("La DeCodificacion ha Fallado: ")
    
