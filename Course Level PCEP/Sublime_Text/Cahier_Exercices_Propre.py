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
        print()   #Le print ci servira à revenir à la ligne: sinon on aura *********************
etoiles(6)

def etoiles(n):
    for i in range (n):
        for j in range (i,n):
            print("*",end="")
        print()
etoiles(10)

#exemple pour comprendre l'usage du print() isolé en bas:

for i in range(3):
    print('bonjour', end=' ')

print('monsieur')
#result: bonjour bonjour bonjour monsieur

for i in range(3):
    print('bonjour', end=' ')

print()
print('monsieur')

#result:
bonjour bonjour bonjour 
monsieur

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
for i in range (0,20):
    print(f(i))


def f(x):
    return 100*x-4*x**2+2
print(f(2))

for i in range (0,21):
    fmax=0
    imax=0
    if f(fmax)>f(i):
        fmax=f(i)
        imax=i
print(f(i))
print(i)


#Exercice 4:
"""
    Qu'affiche le programme suivant ?

    def u(n):
        if n==0:
            return 2
        else: 
            return 3*u(n-1)-2

    print(u(0))
    print(u(1))
    print(u(2))

    n=10
    print(u(n))

    La fonction définie et utilisée ici s'appelle une fonctions récursive: c'est une fonction qui s'appelle elle-même…
    Modifier le programme précédent pour qu'il calcule les termes de la suite $(u_n)$ définie par l'expression
    $u_n=\dfrac{2u_{n-1}^2-1}{u_{n-1}^2+2}$.
    Afficher en particulier les termes $u_{10}$ et $u_{20}$.
    Une autre manière de programmer les calculs des termes d'une telle suite est:

    u=2
    n=10
    for i in range(n):
        u=(2*u**2-1)/(u**2+2)
    print(u)

    qui calcule ici $u_{10}$, le terme de rang 10.
    Utiliser ce programme pour afficher en particulier les termes $u_{10}$, $u_{100}$ et $u_{1000}$.
    Qu'observe-t-on pour des valeurs de plus en plus grandes de n ? 
"""
def u(n):
    if n==0:
        return 2
    
    else:
        return ((2*(u(n-1))**2)-1)/((u(n-1)**2)+2)
print(u(1))
print(u(10))
print(u(20))



u=2
n=10
for i in range(n):
    u=(2*u**2-1)/(u**2+2) #Pour les valeurs de plus en plus grandes de n, u reste constant(garde la meme valeur)
print(u)

u=2
n=100
for i in range(n):
    u=(2*u**2-1)/(u**2+2)
print(u)

u=2
n=1000
for i in range(n):
    u=(2*u**2-1)/(u**2+2)
print(u)


#Autre exemple de recursion.
def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)  # so a+fun(28)==a+(a+fun(28+3))==a+a+3==25+28+3==56


print(fun(25))     #result 56   


# Recursive implementation of the factorial function.

def factorial(n):
    if n == 1:    # The base case (termination condition.)
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4)) # 4 * 3 * 2 * 1 = 24


#The Fibonacci numbers definition is a clear example of recursion. We already told you that:   Fib(i) = Fib(i-1) + Fib(i-2)
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)



#Exercice 5:
"""
    Un village comptait 4000 habitants en 2000. Chaque année depuis, cette population a augmenté de 3% d'une année à la suivante.
    Écrire un programme qui calcule le nombre d'habitants dans ce village en 2001, puis 2002, puis 2010, puis cette année.
    Modifier le programme précédent pour qu'il détermine en quelle année la population du village aura triplé.
    
"""
hab = 4000 #habitants en 2000
for i in range(2001,2023):
    hab = hab+(4000*3)/100
    if i==2001:
        print("En 2001 il y'a eu",hab,"habitants")
    if i==2002:
        print("En 2002 il y'a eu",hab,"habitants")
    if i==2010:
        print("En 2010 il y'a eu",hab,"habitants")
    if i==2022:
        print("Cette année 2022 on aura",hab,"habitants")


#ou encore on peut faire
def hab(n):
    if n==0:
        return 4000
    else:
        return ((1.03)**n)*(4000) #suite geometrique Vn=((1.03)**n) *(Vo)
print(hab(n))

#Le triple de la population
hab = 4000
annee=2000
while hab<=12000:
    hab=hab+(4000*3)/100
    annee+=1
print(hab)
print("Le village aura triplé en",annee)


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
print("Vous avez un écart de" ,round(ecart), "centimètres par rapport à la moyenne")



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



#Exercice : comparaison à la moyenne

Reprenez l’exercice qui permet de comparer une taille saisie avec la moyenne.
Créez trois fonctions dans le programme :

demander_taille()
Cette fonction demande sa taille à l’utilisateur et retourne la valeur saisie sous la forme d’un nombre.

comparer_taille()
Cette fonction compare une première taille à une seconde et donne la différence en centimètres.
Le second paramètre a une valeur par défaut qui correspond à la moyenne de la taille.

afficher_difference_moyenne()
Cette fonction prend en paramètre un écart de taille en centimètres et affiche l’information à l’utilisateur.

def demander_taille():
    taille = float(input("veuillez entrer votre taille: "))
    return taille
print(demander_taille())

def comparer_taille(taille,moyenne=1.75):
    taille = float(input("veuillez entrer votre taille: "))
    return (taille-moyenne)*100
print(comparer_taille(taille,moyenne=1.75))

def afficher_difference_moyenne(ecart):
    print("Vous avez un écart de",round(afficher_difference_moyenne(ecart)),"centimètres par rapport à la moyenne")

taille= demander_taille()
ecart= comparer_taille(taille)
afficher_difference_moyenne(ecart)



#Exercice : fonction de conversion Fahrenheit / Celsius

Écrivez une fonction pour convertir une température en degré Fahrenheit en une température en degré Celsius.

def FahrenheitCelsius(temp):
    celsius=(temp-32)/1.8
    return celsius
    
temp=float(input("Entrer la température en degré Fahrenheit:"))
print("Cette temperature correspond à",round(FahrenheitCelsius(temp),1),"°C")



#http://xymaths.free.fr/Informatique-Programmation/python/exercices.php NOUVEAU A FAIRE

#Exercice 1:
"""
Que fait le programme suivant:

n=int(input("Combien de semaines avant les vacances ?"))
print("Plus que "+str(n)+" semaines avant les vacances !")

Compléter ce programme pour qu'il affiche aussi le nombre de jours avant les vacances, puis le nombre de jours de cours avant les vacances
ainsi que le nombre de week-ends.
Modifier ce programme pour que l'affichage soit toujours sans faute (et s'il n'y a pas plusieurs semaines ou plusieurs jours, et un seul week-end)
"""
n=int(input("Combien de semaines avant les vacances ?"))
print("Plus que "+str(n)+" semaines avant les vacances !")
print("Plus que "+str(n*7)+" jours avant les vacances !")
print("Plus que "+str(n*5)+" jours de cours avant les vacances !")
print("Plus que "+str(n*1)+" week-ends avant les vacances !")

if n>1:
    print("Plus que "+str(n)+" semaines avant les vacances !")
    print("Plus que "+str(n*1)+" week-ends avant les vacances !")
else:
    print("Plus que "+str(n)+" semaine avant les vacances !")
    print("Plus que "+str(n*1)+" week-end avant les vacances !")

if n*7 > 1:
    print("Plus que "+str(n*7)+" semaines avant les vacances !")
    
else:
    print("Plus que "+str(n*7)+" semaine avant les vacances !")

if n*5 > 1:
    print("Plus que "+str(n*5)+" semaines avant les vacances !")
    
else:
    print("Plus que "+str(n*5)+" semaine avant les vacances !")


#Exercice 2:
"""
Le programme suivant permet de récupérer et afficher la date actuelle et de demander une date à l'utilisateur:

from datetime import datetime
date=datetime.now()
ja=date.day;ma=date.month;aa=date.year
# ja, ma, et aa sont: jour, mois et année actuels
print("Nous sommes le: "+str(ja)+"/"+str(ma)+"/"+str(aa))

dn=input('Votre date de naissance ? (format jj/mm/aaaa) :')
dn=dn.split('/');
jn=int(dn[0]);mn=int(dn[1]);an=int(dn[2])
# jn, mn, et an sont: jour, mois et année de naissance saisis

    Tester le programme précédent. Compléter le programme pour qu'il affiche les différentes valeurs des jours, mois et années.
    Compléter le programme pour qu'il demande à l'utilisateur sa date de naissance et affiche en retour son age.
    Compléter ce programme pour qu'il affiche dans combien de mois est l'anniversaire de la personne.
    (et un message spécial si l'anniversaire est ce mois, dans quel cas on affiche dans combien de jours est la fête).
"""
from datetime import datetime
date=datetime.now()
ja=date.day;ma=date.month;aa=date.year
# ja, ma, et aa sont: jour, mois et année actuels
print("Nous sommes le: "+str(ja)+"/"+str(ma)+"/"+str(aa))

dn=input('Votre date de naissance ? (format jj/mm/aaaa) :')
dn=dn.split('/');
jn=int(dn[0]);mn=int(dn[1]);an=int(dn[2])
# jn, mn, et an sont: jour, mois et année de naissance saisis
print("votre date de naissance saisie est: "+str(jn)+"/"+str(mn)+"/"+str(an))

N=input('Entrez votre date de naissance ? (format jj/mm/aaaa) :')
nais=N.split("/")
naissance=int(nais[2])
age = aa-naissance
print("Vous avez",age,"ans")

mois=int(nais[1])
anniv = 0
if mois>ma:
    anniv = mois-ma
elif mois<ma:
    anniv=12-ma+mois
    
print("votre anniversaire est dans",anniv,"mois")

jours=int(nais[0])

if anniv==0:
    jours=jours-ja
    print("Votre anniversaire est ce mois donc dans",jours,"jours")


#Exercice 3:
"""
    Qu'affiche le programme suivant:

    n=int(input("Entrer n: "))
    c=0
    for i in range(n+1):
        c=c+1
        print("c= ",c)

    Remarque: la variable c précédente s'appelle un compteur, et permet donc de compter à chaque fois que le programme "passe" par cette ligne.
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
"""
from random import randint 

BonnesReponses=0
for i in range(5):
    a=randint(1,10)
    b=randint(1,10)
    r=int(input(str(a)+" * "+str(b)+" = ? "))
    if r==a*b:
        BonnesReponses+=1
        print("bien")
    else:
        r!=a*b
        raise ValueError ('Mauvaise Réponse')
print("Vous avez obtenu",BonnesReponses,"bonnes réponses")


#Exercice 4:
"""
    Que calcule le programme suivant:

    n=int(input("Entrer n: "))
    s=0
    for i in range(1,n+1):
        s=s+i
        print("i= ",i, " - s= ",s)

    Modifier le programme précédent pour qu'il calcule, à un nombre n donné (ou demandé à l'utilisateur), les sommes:
        S = 1 + 1/2 + 1/3 + 1/4 + 1/5 + …
        T = 1 + 1/2**2 + 1/3**2 + 1/4**2 + 1/5**2 + …
        U = 1 + 1/2**1 + 1/2**2 + 1/2**3 + 1/2**4 + …
    Qu'observe-t'on pour les valeurs de ces sommes lorsque n est de plus en plus grand (n = 10, n = 100, n = 1000, …) ?
"""
n=int(input("Entrer n: "))
s=0
t=0
u=0
for i in range(1,n+1):
    s = s + 1/i
    t = t + 1/(i)**2
    u = u + 1/(2)**i
print(" i= ",i, " s= ",s)
print(" i= ",i, " t= ",t)
print(" i= ",i, " u= ",u)
#lorsque n est de plus en plus grand, les valeurs de ces sommes sont de plus en plus proche.

#Exercice 5:
"""
    Que calcule et affiche le programme suivant ?

    def f(x):
        y=3*x**2+2
        return y

    print(f(1))

    x=3
    print(f(x))

    Rappel / remarque: L'opération notée ** en python est la puissance, souvent notée ^ dans les autres langages et calculatrices. Par exemple, 2**3=2*2*2=8.
    On définit ici une fonction. (re)Voir éventuellement le cours sur les fonctions.
    On considère maintenant la fonction: P(x) = x4 − 101324x3 − 101323x2 − 202650x.
    On sait que l'équation P(x) = 0 a une solution qui est un nombre entier strictement positif.
    Trouver cette solution.
"""
def p(x):
    return x**4 - 101324*(x**3) - 101323*(x**2) - 202650*(x)

x=1
while p(x) != 0:
    x+=1
    
print("La valeur de x est ",x)



#Exercice 6:
"""
    Que fait le programme suivant ? Qu'affiche-t'il ?

    from random import randint 
    d=randint(1,6)
    if (d==6): 
       print("Gagné")
    else:
       print("Dommage")

    Modifier le programme précédent, et créer un programme qui lance 10 fois un dé et qui compte le nombre de 6 obtenus.
    Calculer et afficher le pourcentage de 6 obtenus.

    Que devient ce pourcentage si on lance 100 fois, ou 1000 fois, ou 10000 fois, …, le dé ?
"""

from random import randint

nbre6=0
for i in range (1,10+1):
   d=randint(1,6)
   if (d==6):
      nbre6+=1
      
print("On a obtenu 6: ",nbre6,"fois")
pourcentage=(nbre6 / 10)*100
print("Le pourcentage de 6 obtenu est: ",pourcentage)
#Si on lance le dé 100 fois, ou 1000 fois, ou 10000 fois, …, ce pourcentage reduit de plus en plus considérablement.

#Exercice 8:
"""
    Quels sont les affichages successifs du programme suivant ?

    s="je vais travailler ce soir "
    print(s[3])
    print(s[3:7])
    print(len(s))

    for i in range (len(s)):
        print(s[i])

    Compléter le programme précédent de manière à ce qu'il compte le nombre de "a" dans la chaîne s précédente.
    Reprendre la question précédente pour compter et afficher le nombre de mots.
    Bien sûr, il est interessant de tester le programme avec divers textes dans la chaîne s. 
"""

s="je vais travailler ce soir "
print(s[3])
print(s[3:7])
print(len(s))

for i in range (len(s)):
   print(s[i])

print(s.count("a"))
         
l=s.split(" ")
print(len(l))


#Exercice 9:
"""
Le programme suivant permet de décomposer les chiffres qui composent un nombre: le nombre n est converti en chaîne de caractères. Cette chaîne s peut alors être manipulée comme un tableau.
Qu'affiche le programme suivant ?

n=412
s=str(n)
print(s[2])

for i in s:
    print(i)

print(s[0]+s[1]+s[2])
print(int(s[0])+int(s[1])+int(s[2]))

    Écrire un programme qui, à un nombre donné (ou demandé à l'utilisateur), retourne la somme des chiffres qui le compose.
    Par exemple, pour n=412, le programme retourne 4+1+2=7.
    Écrire un programme qui, à un nombre donné (ou demandé à l'utilisateur), retourne la somme des carrés des chiffres qui le compose.
    Par exemple, pour n=412, le programme retourne 42+12+22=21.
    Un nombre heureux est un nombre entier qui, lorsqu'on ajoute les carrés de chacun de ses chiffres, puis les carrés des chiffres de ce résultat et ainsi de suite jusqu'à l'obtention d'un nombre à un seul chiffre égal à 1.
    Par exemple 7 et 13 sont heureux: 72=49, puis 42+92=97, puis 92+72=130, puis 12+32+02=10, puis 12+02=1

    De même pour 13: 12+32=10, puis 12+02=1.

    par contre 12 n'est pas heureux: 12+22=5 ≠ 1.

    Écrire un programme qui, à un nombre donné (ou demandé à l'utilisateur), retourne s'il est heureux ou non.
"""

nbre = input("Entrer un nombre: ")
liste = list(str(nbre))
somme = 0
for i in liste:
   somme = somme + int(i)
print(somme)

nbre = input("Entrer un nombre: ")
liste = list(str(nbre))
somme = 0
for i in liste:
   somme = somme + (int(i)**2)
print(somme)


nbre = input("Entrer un nombre: ")
s=int(nbre)

while s>9:
   somme=0
   liste=list(str(s))
   for i in liste:
      somme = somme +int(i)**2
      s=somme
if s == 1:
   print("Bravo, votre nombre est un nombre heureux")
else:
   print("Désolé, votre nombre n'est pas un nombre heureux")


#Exercice 10:
"""
    Écrire un programme qui construit une liste de 5 nombres entiers aléatoires compris entre 1 et 6. (voir par exemple exercice 6)
    Compléter le programme précédent pour qu'il affiche de plus:
        "paire": si 2 chiffres sont identiques
        "brelan": si 3 chiffres sont identiques
        "carré": si 4 chiffres sont identiques
        "yams": si les 5 chiffres sont identiques
    Modifier le programme précédent pour compter, sur 1000 tirages de 5 chiffres, le nombre de paires, de brelans, de carrés et de yams obtenus.
"""
#SOLUTION UNE
from random import randint

liste=[]
for i in range(5):
   r=randint(1,6)
   liste.append(r)
print(liste)


occ = []
for i in liste:
    occ.append(liste.count(i))
print(occ)

state2 = False
state3 = False
state4 = False
state5 = False

for i in occ:
    if((i == 2)and(state2==False)):
        print("Paire")
        state2 = True
    if((i == 3)and(state3==False)):
        print("brelan")
        state3 = True
    if((i == 4)and(state4==False)):
        print("carré")
        state4 = True
    if((i == 5)and(state5==False)):
        print("yams")
        state5 = True
        

#SOLUTION DEUX
from random import randint

list=[ ]
for i in range(5):
   r=randint(1,6)
   list.append(r)
   print (r)
print(list)



#DERNIERE QUESTION ,SOLUTION UNE

from random import randint
paire = 0
brelan = 0
carre = 0
yams = 0

liste=[]

for i in range(1000):
    for i in range(5):
       r=randint(1,6)
       liste.append(r)
    print(liste)

    occ = []
    for i in liste:
        t = (i, liste.count(i))
        if t not in occ:
            occ.append(t)
    print(occ)

    for i in occ:
        if(i[1] == 2):
            paire +=1
        if(i[1] == 3):
            brelan +=1
        if(i[1] == 4):
            carre +=1
        if(i[1] == 5):
            yams +=1
        
print("Le nombre de paires est: ", paire)
print("Le nombre de brelans est: ", brelan)
print("Le nombre de carrés est: ", carre)
print("Le nombre de yams est: ", yams)








#https://www.codingame.com/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/cours---variables-et-operations
#DEJA FAIT et corrigés

#http://www.fredpeuriere.com/NSI/1/calculs-variables-exos-correc.pdf
#DEJA FAIT

#http://maximiliendreveton.fr/Lycee/A1_A2_exos_type_correction.pdf
#DEJA FAIT

#http://alain.troesch.free.fr/2014/Fichiers/corrinfo1.pdf
#DEJA FAIT


#https://www.w3schools.com/quiztest/quiztest.asp?qtest=PYTHON QUIZ A FAIRE



#http://xymaths.free.fr/Informatique-Programmation/python/exercices.php NOUVEAU A FAIRE
Exercice 1:

Que fait le programme suivant:

n=int(input("Combien de semaines avant les vacances ?"))
print("Plus que "+str(n)+" semaines avant les vacances !")

Compléter ce programme pour qu'il affiche aussi le nombre de jours avant les vacances, puis le nombre de jours de cours avant les vacances ainsi que le nombre de week-ends.
Modifier ce programme pour que l'affichage soit toujours sans faute (et s'il n'y a pas plusieurs semaines ou plusieurs jours, et un seul week-end)






#http://hebergement.u-psud.fr/iut-orsay/Pedagogie/MPHY/Python/exercices-python3.pdf

#Cours no 1 : « Premiers pas en Python »
"""
1. Affectez les variables temps et distance par les valeurs 6.892 et 19.7.
Calculez et affichez la valeur de la vitesse.
Améliorez l’affichage en imposant un chiffre après le point décimal.
2. Saisir un nom et un âge en utilisant l’instruction input(). Les afficher.
Refaire la saisie du nom, mais avec l’instruction raw_input(). L’afficher.
Enfin, utilisez la « bonne pratique » : recommencez l’exercice en transtypant les saisies
effectuées avec l’instruction raw_input()
"""

temps=6.892
distance=19.7
vitesse=distance/temps
print(vitesse)
print(round(vitesse,1))


nom=input("Entrer le nom:")
age=int(input("entrer votre age:"))
print("nom:",nom,"\nage:",age)

#La fonction raw_input n'est plus inclus dans python.

#Cours no 2 : « Contrôle du flux d’instructions »
"""
1. Saisissez un flottant. S’il est positif ou nul, affichez sa racine, sinon affichez un message
d’erreur.
2. L’ordre lexicographique est celui du dictionnaire.
Saisir deux mots, comparez-les pour trouver le « plus petit » et affichez le résultat.
Refaire l’exercice en utilisant l’instruction ternaire :
<res> = <a> if <condition> else <b>
"""
f=float(input("Entrer un reel: "))
if f>=0:
    print(f**0.5)
else:
    raise ValueError ("Oups",f,"est inferieur à zéro")


















