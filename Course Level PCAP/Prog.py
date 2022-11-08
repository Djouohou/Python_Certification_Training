"""
#import ModuleA as modA

#from ModuleA import somme
from Package.ModuleA import *
#from Package.ModuleB import *

nombre1 = int (input("Entrez le premier nombre: "))
nombre2 = int (input("Entrez le second nombre: "))
#print(somme(nombre1, nombre2))
print(impair(nombre1))

"""
def decomposition( nbre):
        Ldiv = []
        for i in range(2,int(nbre/2)):
            while nbre%i==0:
                c = nbre/i
                nbre=c
                Ldiv.append(i)
        return Ldiv

print(decomposition(120))


def listDive( nbre):
        Ldiv = []
        for i in range(2,nbre):
            if nbre%i==0:
                Ldiv.append(i)
        return Ldiv

print(listDive(12))










"""
def fibonajcci ( n , compteur ) :
    if n == 0 or 1 :
        return 1
    else:
        compteur+=1
        return fibonacci( n-1)+ fibonacci( n-2)
    
    return compteur

compteur=int(input('c'))   
n=int(input('entrer la valeur de n: '))
print(fibonacci ( n,compteur ) ) 


def myfunction():
    
    myfunction.counter += 1
    return 2+2
myfunction.counter = 0
print(myfunction())
print(myfunction())
print(myfunction())
print(myfunction.counter)


"""






  
      
