#LES EXCEPTIONS EN PYTHON
"""
Exercice 1: V ́erification de l’ˆage
 ́Ecrire un programme qui demande `a l’utilisateur d’ ́ecrire son
ˆage et qui g`ere le cas o`u celui-ci n’entre pas un nombre.
"""
age=input('veuillez entrer votre age: ')
try:
    if age.isdigit():
        print(age)
    else:
        raise ValueError("Ooops Erreur!") #ce bloc permet siplement de lever ou definir l'erreur qui sera lancer mais ce bloc ne s'eexecute pas. d'ou le ooops erreur ne sera pas print.

except ValueError:
    print("Désole! vous n'avez pas entré un nombre.") #c'est ce message qui s'affiche quand l'exception est gèré.
    
"""
Exercice 2: Fonction d ́efinie par morceau
 ́Ecrire une fonction sinc qui prend en entr ́ee un nombre x
et renvoie la valeur sin(x)/x si x != 0 et 1 sinon.
Le programme doit g ́erer une exception. La fonction sin est
disponible dans le module math de Python
"""
from math import sin

def sinc():
    x=int(input('Entrez la valeur de x: '))
    res = 0
    try:
        res =  sin(x)/x
    except ZeroDivisionError:
        print("Division par zero ! ")
        
    if x != 0:
    	return res
    else:
    	return 1

print(sinc())

"""
Exercice 3 Ouverture de fichier
Lorsque l’on essaie d’ouvrir un fichier qui n’existe pas avec la
fonction open de Python, l’interpr ́eteur nous renvoie une ex-
ception (mal d ́efinie en Python < 3 et IOError en Python3)
 ́Ecrire un programme qui demande `a l’utilisateur le nom d’un
fichier et essaie de le lire. Si le fichier n’existe pas, le pro-
gramme affiche qu’il n’existe pas et redemande `a l’utilisateur
un autre nom de fichier.
"""
try:
    fchier=open(input('entrer le nom de votre fichier texte '),'r')
    print(fichier.read())
except FileNotFoundError:
    print("Ce fichier n’existe pas, veuillez entrer un autre nom de fichier.")



#file=os.path.exists(nom du fichier situécdans le meme emplacement que le fichier .py qui porte le code)

#CORRECTION PAR PROF


pathNotExist = True
while pathNotExist:
    path=input('entrer le nom de votre fichier texte ')
    try:
        fichier=open(path,'r') #quand le fichier n'exixte pas l'exception est levé et géré mais la boucle ne peut terminer son execution et on va donc jamais tomber sur la condition false d'en bas d'ou on retournera a chaque fois au debut de la boucle.
        pathNotExist=False   # quand le fichier exist le fichier s'ouvre et la boucle se termine(donc le False sera donc pris en compte et le boucle ne retournera plus au debut.)
    except FileNotFoundError:
        print("Ce fichier n’existe pas.") 
print(fichier.read())

"""
Exercice 4 Un jeu
Voici le d ́ebut d’un jeu tr`es simple consistant `a arrˆeter une boucle sur un nombre pr ́ecis ́e `a l’avance :
1 #! / u s r / b i n / pyt hon
#c o d i n g : u t f −8
3 import random
import time
5 x = random . r a n d i n t ( 0 , 1 0 0 )
print ’ Vous devez a r r e t e r l e programme s u r %d ’%x
7 print ’ Pour a r r e t e r l e programme , i l f a u t f a i r e C t r l+C. ’
print ’ Appuyer s u r E ntr ee pour commencer . . . ’
9 b = r a w i n p u t ( )
i =0
11 while ( i <100) :
i+=1
13 print ”%d\ x0d ”%i ,
time . s l e e p ( 0 . 2 )
En g ́erant l’exception KeyboardInterrupt, completer le programme pour qu’il ŕeponde aux sp ́ecifications.
Remarque : Le code ASCII ≪ \x0d ≫ est le caract`ere retour chariot donn ́e comme code hexad ́ecimal.
"""
import random
import time
x = random . randint ( 0 , 100 )
print ('Vous devez arreter le programme sur %d '%x)
print ("Pour arreter le programme , il faut faire Ctrl+C.")
print ("Appuyer sur Entree pour commencer . . . ")

b = input()
try:
    i =0
    while ( i <100) :
        i+=1
        print ("%d "%i)
        time . sleep(0.2)
except KeyboardInterrupt:
    print("Vous avez interrompu l'execution du programme. ")

"""
Exercice 5: Pente d’une droite
Nous d́esirons  ́ecrire un programme qui calcule la pente d’une
droite passant par deux points dont nous connaissons les co-
ordonn ́ees.
1)́Ecrire une fonction pente(xA, yA, xB , yB ) qui utilise la
formule math ́ematique et renvoie la pente de la droite
(AB).
2)Modifier le programme dans le cas o`u l’utilisateur com-
met une division par z ́ero en g ́erant l’exception associ ́ee
"""


def pente(xA, yA, xB , yB):
    x = 0
    try:
        if (xB-xA) != 0:
            x=(yB-yA)/(xB-xA)
        else:
            raise ZeroDivisionError("Division par zero ! ")
    except ZeroDivisionError:
        print("Division par zero ! ")
    return x


xA =int(input("entrer xA "))
yA =int(input("entrer yA "))
xB =int(input("entrer xB "))
yB =int(input("entrer yB "))

print(pente(xA, yA, xB , yB))


"""
Exercice 6: Racines reelles
Nous d ́esirons  ́ecrire un programme qui calcule les racines
ŕeelles d’un polynome et qui leve une exception ≫NameEr-
ror≪ avec un message adapt ́e lorsque le discriminant est stric-
tement n ́egatif.
1 ◮  ́Ecrire une fonction racines(a, b, c) qui utilise la for-
mule math ́ematique pour renvoyer une valeur approch ́ee
des racines r ́eelles.
2 ◮ Tester ce programme avec un discriminant n ́egatif puis
avec un argument a  ́egal `a 0. G ́erer en cons ́equence les
exceptions (et les changemets de formules !)
"""
import math

def racines(a, b, c):
    delta=(b**2)-(4*a*c)
    r1=(-b + math.sqrt(delta))/(2*a)
    r2=(-b - math.sqrt(delta))/(2*a)
    return r1, r2

a =int(input("entrer a "))
b =int(input("entrer b "))
c =int(input("entrer c "))

result = racines(a, b, c)
print("les racines sont: " + str(result[0]) + " et " + str(result[1]))


# Quand le discriminant (ici delta) est négatif, on a ValueError: math domain error

# lorsque a égal à 0, on a un ZeroDivisionError: float division by zero


def racines(a, b, c):
    delta=(b**2)-(4*a*c)
    r1 = -1000
    r2 = -1000
    try:
        if delta < 0:
            raise NameError(" ")
        else:
            r1=(-b + math.sqrt(delta))/(2*a)
            r2=(-b - math.sqrt(delta))/(2*a)
       
    except NameError:
        print("Désolé Erreur")
        
    return r1, r2

a =int(input("entrer a "))
b =int(input("entrer b "))
c =int(input("entrer c "))

result = racines(a, b, c)
print("les racines sont: " + str(result[0]) + " et " + str(result[1])) #concatener pour afficher car il s'agit des entiers et chaines de caracteres, donc deux types differents

"""
Exercice 7 Addition en temps limit ́e
1 ◮  ́Ecrire un programme qui demande `a l’utilisateur de cal-
culer la somme de deux nombres (pris al ́eatoirement
entre 0 et 100).
2 ◮ En utilisant le module time, lever une exception lorsque
l’utilisateur ne r ́epond pas apr`es 10 secondes.
Conseil : on utilisera une boucle while
"""
import time
import random

a = random.randint(0, 100)
b = random.randint(0, 100)

print("a = ",a)
print("b = ",b)


start=time.time()
somme = int(input("entrer la somme de a et b: "))
end=time.time()

val = end - start

while val>10:
    raise KeyboardInterrupt("dix secondes sont passes")

if somme == a + b:
    print("Juste!")
    print(a," + ",b," = ",somme)
else :
    print('Mauvaise reponse')





"""
Exercice 8: Fonctions r ́ecursives ⋆
Voici une fonction r ́ecursive qui

def fibonacci ( n ) :
    if n == 0 or n == 1 :
        return 1
    else:
        return fibonacci( n−1)+ fibonacci( n−2)

1 ◮ Modifier le programme pour qu’il renvoie le nombre
d’appel r ́ecursifs n ́ecessaires au calcul de fibonacci(n).
Conseil : on pourra ajouter un argument `a fibonacci.
2 ◮ Modifier le programme pour qu’il l`eve une exception
lorsque le niveau de r ́ecursivit ́e d ́epasse 100
"""
#En mathématiques, la suite de Fibonacci est une suite d'entiers dans laquelle chaque terme est la somme des deux termes qui le précèdent.






































