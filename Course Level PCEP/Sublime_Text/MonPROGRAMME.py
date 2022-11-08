
#import MonMODULE
#from MonMODULE import somme
#from MonMODULE import *
from MonPACKAGE.Module import somme

nombre1 = int(input('entrer le premier nombre: '))
nombre2 = int(input('entrer le deuxième nombre: '))

#print(MonMODULE.somme(nombre1, nombre2))


print(somme(nombre1, nombre2))
print(hello('sophie'))
