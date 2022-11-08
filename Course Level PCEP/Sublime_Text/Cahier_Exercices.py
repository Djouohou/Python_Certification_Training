

import os

# -*- coding: utf-8 -*-

"""
print("bonjour\nmonsieur")

print("un",end=" ")
print("deux",end=" ")
print("trois",end=" ")
print()

distance = 55758000
print(distance)
print(2*distance)

nbredef=2
nbredes=4
print(nbredef+nbredes)

entier=0
for i in range (1,100+1):
    print(i)
    entier+=1
print("ouf")

entier=100
for i in range (100,0,-1):
    print(i)
print("ouf")

for i in range (5):
    for j in range(10):
        print(j,end=" ")
    print()

n=5
for j in range (n):
    for i in range (n):
        print("*",end=" ")
    print()

n=5
i=0
for i in range(n):
    for j in range (i+1):
        print(j,end=" ")
    print()

EXO:
Dans le programme suivant, la fonction randint(1,10) permet d'obtenir un nombre entier aléatoire entre 1 et 10.
Que fait alors le programme suivant ?
from random import randint 
for i in range(5):
    a=randint(1,10)
    b=randint(1,10)
    r=int(input(str(a)+" * "+str(b)+" = ? "))
    if r==a*b:
        print("bien")
Compléter ce programme pour qu'il affiche un message d'erreur lorsque la réponse donnée n'est pas la bonne.
Modifier ce programme pour qu'il compte, et affiche à la fin, le nombre de bonnes réponses.

from random import randint

#nqp=nombre de questions posées
#nbr=nombre de bonnes reponses

for i in range(5):
    nqp=5
    nbr=0
    a=randint(1,10)
    b=randint(1,10)
    r=int(input(str(a)+" * "+str(b)+" = ? "))
    if r==a*b:
        nbr+=1
        print("bien")
    else :
        r!=a*b
        print("vous avez entré une mauvaise reponse")
print("vous avez obtenu ",nbr,"bonnes reponses sur",nqp,"questions")

#non resolu
n=5
i=0
for i in range(n):
    for i in range(0,n,+1):
        print(i,end=" ")
    for j in range (n):
        print(j)
    print()

"""
#EXERCICES A FAIRE
#http://xymaths.free.fr/Informatique-Programmation/python/exercices-fonctions.php
"""
 Exercice 1:

1.Qu'affiche le programme suivant ?

    def Stars(n):
        print(n*"*")

    Stars(3)
    Stars(10)

2.En utilisant cette fonction dans une boucle, produire l'affichage suivant:

    * 
    **
    ***
    ****
    *****
    ******
"""
def Stars(n):
    print(n*"*")

Stars(3)
Stars(10)


def etoiles(n):
    for i in range (n):
        for j in range (i+1):
            print("*",end="")
        print()
etoiles(6)

def etoiles(n):
    for i in range (n):
        for j in range (i,n):
            print("*",end="")
        print()
etoiles(10)
"""
 Exercice 2:

   1. Que fait et affiche le programme suivant ?

    def MaFonction(a,b):
        y=a+b
        return y
        
    a=2;b=5
    c=MaFonction(a,b)
    print("c = ", c)

    z=Mafonction(3,2+5)
    print("z = ", z)

    Combien la fonction nommée MaFonction a-t'elle d'arguments en entrée ? en sortie ?
    2.Écrire une fonction, nommée MyNewFct, avec trois arguments qui retourne la moyenne des trois valeurs.
    3.Écrire une fonction, nommée Mention, qui a un argument en entrée: une note entre 0 et 20, et en sortie renvoie la mention correspondante: P, AB, B, TB.
    Compléter cette fonction pour qu'elle affiche un message d'erreur si la note entrée est négative ou supérieure à 20.
    4.Écrire une troisième fonction, nommée Apprecie, avec trois arguments en entrée et qui renvoie la mention correspondante à la moyenne des trois valeurs entrées.
    Cette fontion sera écrite en appelant les deux fonctions précédentes: MyNewFct et Mention.
"""
#1. ce programme fait la somme c de deux valeurs a et b entrées en paramètres.
#MaFonction a deux arguments en entrée et en sortie.

def MyNewFct(a,b,c):
    d = ((a+b+c)/3)
    return (d)
print(MyNewFct(15,6,42))


#P=passable10-11/AB=assez bien 12-14/B=bien 15-17/TB=tres bien 18-20
def Mention (m):
    while m in range(0,20+1):
        if m in range(10,12):
            return("votre mention est: P ou passable")
        if m in range(12,15):
            return("votre mention est: AB ou assez bien")
        if m in range(15,18):
            return("votre mention est: B ou bien")
        if m in range(18,20+1):
            return("votre mention est: TB ou tres bien")
    if m<0 or m>20:
        print("Oups!!! vous avez entré une valeur hors de l'intervalle donné")
        raise ValueError(m)    #comment faire exécuter tout de meme le print 'merci' aprés que l'exception est été lévé
        
m=int(input("veuillez entrer votre note obtenue entre 0 et 20: "))
print(Mention(m))
print("Merci!")

def Apprecie(l,m,n):
    moyenne = MyNewFct(l,m,n)
    mention = Mention (moyenne)
    return mention
l = int(input("veuillez entrer votre première valeur: "))
m = int(input("veuillez entrer votre deuxième valeur: "))
n = int(input("veuillez entrer votre troisième valeur: "))
print(Apprecie(l,m,n))
print("Merci!")
    
 """Exercice 3:

Qu'affiche le programme suivant ?

def f(x):
    return 100*x-4*x**2+2
print(f(2))

Écrire un programme qui affiche les valeurs f(x) pour tous les nombres entiers x entre 0 et 20 (utiliser une boucle for ...).
Modifier le programme précédent pour qu'il trouve et affiche le maximum de la fonction f, et la valeur de x correspondante.
"""
def f(*x):
    for i in range (0,20):
        return 100*x-4*x**2+2
print(f(x))



#https://www.codingame.com/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/cours---variables-et-operations
#DEJA FAIT(fait en ligne directement)

#http://www.fredpeuriere.com/NSI/1/calculs-variables-exos-correc.pdf
#DEJA FAIT

#http://maximiliendreveton.fr/Lycee/A1_A2_exos_type_correction.pdf
#DEJA FAIT

#http://alain.troesch.free.fr/2014/Fichiers/corrinfo1.pdf
#DEJA FAIT MAIS AVEC QUESTION


#https://gayerie.dev/docs/python/python3/fonction.html

#Exercice : comparaison à la moyenne
"""
Écrivez un programme qui demande à l’utilisateur sa taille puis qui indique l’écart en centimètres par rapport à la moyenne. On pourra utiliser comme moyenne 1m75.
Pour réaliser ce programme, vous allez avoir besoin de la fonction input(). Cette fonction accepte en paramètre le message à afficher à l’utilisateur. L’appel à cette fonction bloque le programme et attend que l’utilisateur saisisse une valeur puis tape sur Entrer. La fonction retourne alors la valeur saisie sous la forme d’une chaîne de caractères.

Exemples d’utilisation du programme :
Quelle est votre taille ? 1.70
Vous avez un écart de -5 centimètres par rapport à la moyenne

Quelle est votre taille ? 1.75
Vous avez un écart de 0 centimètres par rapport à la moyenne
"""
taille = float(input("veuillez entrer votre taille: "))
moyenne=1.75
ecart = (taille - moyenne)*100 
print("Vous avez un écart de",round(ecart),"centimètres par rapport à la moyenne")



#Exercice : conversion Fahrenheit / Celsius
"""
Écrivez un programme qui demande à l’utilisateur de saisir une température en degré Fahrenheit et qui affiche le résultat de la conversion en degré Celsius avec
 un seul chiffre après la virgule.
La formule à appliquer :

d(f) = {f - 32}/{1.8}

Exemple d’utilisation du programme :
Température Fahrenheit ? 42
Une température de 42.0°F correspond à 5.5°C
"""

temp=float(input("Entrer la température en degré Fahrenheit:"))
celsius=(temp-32)/1.8
print("Cette temperature correspond à",round(celsius,1),"°C")


#Exercice :QCM en invite de commande
"""
Écrivez un programme qui pose des questions pour lesquelles l’utilisateur doit fournir une réponse. Pour chaque réponse correcte, l’utilisateur marque un point.
À la fin, le programme indique le nombre de réponses justes et le nombre de réponses fausses.

Exemple d’utilisation du programme :

Quel est ton nom ?
Sir Robin de Camelot.
Quelle est ta quête ?
Trouver le Saint Graal.
Quelle est la capitale de la Syrie ?
Je sais pas ça !

Réponses correctes : 2
Réponses incorrectes : 1
"""

import random
dico= { }
dico["Quel est ton nom ?"]=["Sir Robin de Camelot."]
dico["Quelle est ta quête ?"]=["Trouver le Saint Graal."]
dico["Quelle est la capitale de la Syrie ?"]=["Je sais pas ça !"]
repcor=0
repincor=0
for i in range(len(dico)):
    question=random.choice(list(dico.keys()))
    print(question)
    reponse=input("Entrer votre reponse: ")
    print(reponse)
    if reponse==dico[question]:
        repcor+=1
        print(True)
    else:
        print(False)
        repincor+=1
    del dico[question]
print("reponses correctes : ",repcor)
print("reponses incorrectes : ",repincor)













os.system("pause")
