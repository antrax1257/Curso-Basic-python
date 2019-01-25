
# Funcion para encontrar  las permutaciones en una cadena
from itertools import permutations 
  
def allPermutations(str): 
       
     # Obtener permutacion de la cadena'ABC' 
     permList = permutations(str) 
  
     # Imprimiendo todas las permutaciones
     for perm in list(permList): 
         print (''.join(perm)) 
        
# Corriendo Programa
if __name__ == "__main__": 
    str = 'oas'
    allPermutations(str) 
