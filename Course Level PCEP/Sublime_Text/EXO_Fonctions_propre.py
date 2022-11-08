import os

#https://apcpedagogie.com/exercices-fonctions-python/

#EXERCICE1

"""Énoncé
Écrire une procédure table_multiplication avec trois paramètres : mul(multiplicateur), bornInf et bornSup.
Cette procédure doit afficher la table de multiplication avec les trois paramètres.
Tester la procédure par un appel dans le programme principal.
"""
def table_multiplication(mul,borninf,bornsup):
    for i in range(borninf,bornsup+1):
        result=str(i)+" x "+str(mul)+" = "+str(i*mul)
        print(result)
mul=int(input("veuillez entrer le multiplicateur:"))
borninf=int(input("entrer la borne inferieur:"))
bornsup=int(input("entrer la borne superieur:"))
table_multiplication(mul,borninf,bornsup)

#EXERCICE2
"""
Énoncé

Écrire une fonction cube qui retourne le cube de son argument.
Écrire une fonction volumeSphere qui calcule le volume d’une sphère de rayon r fourni en argument et qui utilise la fonction cube.
Tester la fonction volumeSphere par un appel dans le programme principal.

Rappel
Le volume de l’espace délimité par une sphère (on parle alors du volume de la boule) est égal à 4/3 multiplié par π et par son rayon R au cube. [(4pi*R^{3})/{3}]
"""
def cube(a):
    cub=a**3
    return cub
a=int(input("entrer la valeur de a: "))
print(cube(a))

import math

def cube(a):
    cub=a**3
    return cub

def volumesphere(r):
    vol=(3/4)*(math.pi)*cube(r)
    return vol
r=int(input("entrer la valeur du rayon r: "))
print("Le volume de cette sphère est: ",volumesphere(r))

#EXERCICE3

"""Énoncé
Écrire une fonction triangle en langage python qui prend en paramètre un entier (n) et permet d’afficher un triangle isocèle formé d’étoile(*).
La hauteur du triangle (c’est a dire le nombre des lignes (n))sera fournie en programme principale.
"""
    
def triangle_isocele(n):
     for i in range(1,n+1):
        tri=(" "*(n-i)+"* "*i)
        print(tri)
triangle_isocele(int(input("entrer le nombre de ligne: ")))

#EXERCICE4
"""Énoncé
Écrire une fonction maximum permet d’afficher le plus grand de trois nombres entrés au clavier.
"""
def maximum (a,b,c):
    if a>=b and a>=c:   
        return a
    if b>=a and b>=c:
        return b
    if c>=a and c>=b:
        return c
a=int(input("veuillez entrer votre premier nombre: "))
b=int(input("veuillez entrer votre second nombre: "))
c=int(input("veuillez entrer votre troisième nombre: "))
print(maximum (a,b,c))

#EXERCICE5
"""Énoncé
Écrivez un programme Python pour construire le modèle suivant, en utilisant (Triangle avec des chiffres en Python) une boucle imbriqué.
Sortie attendue:

             11
            2222
           333333
          44444444
         5555555555
        666666666666
       77777777777777
      8888888888888888
     999999999999999999
"""

n=int(input('entrer la valeur de n: '))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i,-1,-1):
        print(i+1,end=" ")
    print()
n=int(input('entrer la valeur de n: '))
p=1
for i in range (n):
    for j in range(i,n):
        print(" ",end="")
    for j in range (i+1):
        print( p ,end="")
    for j in range(i+1):
        print( p ,end="")
    p=p+1
    print()

#EXERCICE6
"""
Ecrire une fonction chiffrePorteBonheur(nb) qui permet de déterminer si un nombre entier nb est chiffre porte Bonheur ou non.
Un nombre chiffre porte Bonheur est un nombre entier qui, lorsqu’on ajoute les carrés de chacun de ses chiffres, puis les carrés des chiffres de ce résultat et ainsi de suite jusqu’à l’obtention d’un nombre à un seul chiffre égal à 1 (un).
Le calcule s’arrête lorsque le chiffre devient inférieur à 10
Le résultat souhaité doit ressemble à l’exemple suivant:

    Nombre de départ: 913
    9^2=81
    1^2=1
    3^2=9
    Nouveau: 81+1+9=91
    9^2=81
    1^2=1
    Nouveau: 81+1=82
    8^2=64
    2^2=4
    Nouveau: 64+4=68
    6^2=36
    8^2=64
    Nouveau: 36+64=100
    1^2=1
    0^2=0
    0^2=0
    Nouveau: 1+0+0=1
    Le chiffre: 913 est un porte boneur
"""
def chiffreportebonheur (nb):  
    val=nb
    while (val>10):
       som=0
       for i in list(str(val)):
          som = som +int(i)**2
          val=som       
    if val == 1:
        print("Bravo,votre nombre est pas un chiffre porte bonheur")
    else:
        print("Désolé,votre nombre n'est pas un chiffre porte bonheur")

nb=int(input("veuillez entrer un nombre et découvrons ensemble si votre nombre est porte bonheur ou pas: "))
(chiffreportebonheur(nb))


#EXERCICE7et8
"""Énoncé
Fonction qui compte le nombre de mots d’une phrase
Ecrire une fonction compteMots(phrase) qui renvoie le nombre de mots contenus dans la phrase "phrase".
On considère comme mots les ensembles de caractères inclus entre des espaces.
"""

def comptemots(phrase):
    return (len(phrase.split(" ")))
phrase=(input("entrer votre phrase: ")
print(comptemots(phrase))

#EXERCICE9
"""Énoncé

Vous développez une application Python pour un jeu en ligne.
Vous devez créer une fonction répondant aux critères suivants:
    La fonction s’appelle update_score
    La fonction reçoit le score actuel et une valeur
    La fonction ajoute la valeur au score actuel
    La fonction renvoie le nouveau score
Comment devriez-vous compléter le code? Pour répondre, sélectionnez les segments de code appropriés dans la zone de réponse.
"""
def update_score(current,value):
    current = current + value
    return current
current=int(input("entrer le score actuel: "))
value=int(input("entrer la valeur à ajouter: "))
print(update_score(current,value))

#EXERCICE10
"""
Énoncé

Une société est en train de créer un programme qui permet aux clients d’enregistrer le nombre de kilomètres parcourus. Le programme enverra des messages en fonction du nombre de miles consignés par le client.
Vous créez le code Python suivant. Les numéros de ligne sont inclus pour référence seulement.
Vous devez définir les deux fonctions requises.
Quels segments de code devez-vous utiliser pour les lignes 01 et 04 ? Chaque réponse correcte présente une partie de la solution ? (Choisissez deux.)

    A.01 def get_name () :
    B.01 def get_name (biker) :
    C.01 def get_name (name) :
    D.04 def calc_calories ():
    E.04 def calc_calories (miles, burn_rate):
    F.04 def calc_calories (miles, calories_per_mile):

"""
def get_name ():
    name=input("quel est votre nom ?")
    return name
def calc_calories (miles,calories_per_mile ):
    calories = miles * calories_per_mile
    return calories
distance = int(input("combien de miles avez-vous fait cette semaine?"))
burn_rate = 50
biker = get_name()
calories_burned = calc_calories(distance,burn_rate)
print(biker, "vous avez bruler à propos " ,calories_burned, "calories.")

#EXERCICE11 non resolu

"""Énoncé

    Un administrateur d’un site web veut assurer un maximum de sécurité pour les utilisateurs du site. Pour ceci il décide de réaliser une application qui évalue la force des mots de passe des différents utilisateurs du site, sachant qu’un mot de passe est une chaîne de caractères qui ne comporte pas d’espaces et de lettres accentuées.
La force d’un mot de passe varie, selon la valeur d’un score calculé, de ‘Très faible’ jusqu’à ‘Très fort’ :

    Si le score <20, la force du mot de passe est ‘Très faible’
    Sinon si le score<40, la force d’un mot de passe est ‘Faible’
    Sinon si le score <80, la force du mot de passe est ‘Fort’
    Sinon la force du mot de passe est ‘Très fort’

    Le score se calcule en additionnant des bonus et en retranchant des pénalités.
    Les bonus attribués sont :
        Nombre total de caractères * 4
        (Nombre total de caractères – nombre de lettres majuscules) * 2
        (Nombre total de caractères – nombre de lettres minuscules) * 3
        Nombre de caractères non alphabétiques * 5
    Les pénalités imposées sont :
    La longueur de la plus longue séquence de lettres minuscules * 2
    La longueur de la plus longue séquence de lettres majuscules * 3
    Exemple
    Pour le mot de passe ‘P@cSI_promo2017’, le score se calcule comme suit :
    La somme de bous = 15*4 + (15-3) *2 + (15-6) *3+6*5=141
        Le nombre total de caractères = 15
        Le nombre de lettres majuscules = 3
        Le nombre de lettres minuscules=6
        Le nombre de caractères non alphabétiques =6
        La somme des pénalités = 5*2+2*2=14
        La longueur de la plus longue séquence de lettres minuscules(‘promo’) =5
        La longueur de la plus longue séquence de lettres majuscules(‘SI’) =2
    Le score final = 141-14=127 ; puisque 127>80 alors le mot de passe est considéré comme ‘Très fort’
    Travail demandé :
        Ecrire une fonction NbCMin(pass) qui retourne le nombre de caractères minuscules.
        Ecrire une fonction NbCMaj(pass) qui retourne le nombre de caractères majuscules.
        Ecrire une fonction NbCAlphapass) qui retourne le nombre de caractères non alphabétiques.
        Ecrire une fonction LongMaj(pass) retourne la longueur de la plus longue séquence de lettres majuscules.
        Ecrire une fonction LongMin(pass) retourne la longueur de la plus longue séquence de lettres minuscules.
        Ecrire une fonction Score(pass) qui affiche le score d’un mot de passe

    Source:https://developpement-informatique.com
"""
#mdp=motdepasse
def NbCMin(mdp):
    min=0
    z=list(mdp)
    for i in z:
        if (i.islower()):
            min=min+1
    return min
mdp=input("veuillez enter votre mot de passe: ")
print("le nombre de caracteres en minuscule est:",NbCMin(mdp))


def NbCAlpha(mdp):
    alpha=0
    z=list(mdp)
    for i in z:
        if (i.isdigit()):
            alpha+=1
        if((not i.isdigit()) and (not i.isalnum())):
            alpha+=1
    return alpha
mdp=input("veuillez enter votre mot de passe: ")
print("le nombre de caracteres en minuscule est:",NbCAlpha(mdp))

#
def LongMaj(mdp):
    z=list(mdp)
    mot=0
    long=0
    for i in z:
        if (i.isupper()):
            mot+=1
        else:
            if mot>long:
                long=mot
            else:
                mot=0
    return long
mdp=input("veuillez entrer votre mot de passe: ")    
print("la plus longue séquence de lettres majuscules compte",LongMaj(mdp),"caractères")



def LongMin(mdp):
    z=list(mdp)
    mot2=0
    long2=0
    for i in z:
        if (i.islower()):
            mot2+=1
        else:
            if mot2>long2:
                long2=mot2
            else:
                mot2=0
    return long2
mdp=input("veuillez entrer votre mot de passe: ")    
print("La plus longue séquence de lettres minuscules compte ",LongMin(mdp),"caractères")


#Nombre total de caractères=ntc
def Score(mdp):
    S=(somme_de_bonus())-(somme_des_penalites())
    return(S)

def somme_de_bonus(mdp):
    z=list(mdp)
    ntc=len(z)
    sommedebonus = (int(ntc)*4)+(int(ntc)- NbCMaj(mdp))*2)+(int(ntc) - NbCMin(mdp))*3)+((LongMaj(mdp))*5)
    return sommedebonus

def somme_des_penalites(mdp):
    sommedespenalites = ((LongMin(mdp))*2)+((LongMaj(mdp))*3)
    return sommedespenalites

mdp=input("veuillez entrer votre mot de passe: ")
print("Le score est:",Score(mdp))




#EXERCICE12
#Un nombre premier est un entier naturel qui admet exactement deux diviseurs distincts entiers et positifs. Ces deux diviseurs sont 1 et le nombre considéré,
#puisque tout nombre a pour diviseurs 1 et lui-même , les nombres premiers étant ceux qui ne possèdent pas d'autre diviseur.
"""Énoncé

Écrivez une fonction qui affiche tous les nombres premiers entre limite inférieur et limite supérieur où les deux limites sont deux paramètres saisies par l’utilisateur.
"""
def nombre_premier(limiteinf, limitesup):
    state=0
    
    for i in range (limiteinf, limitesup+1):
        state=0
        for j in range(2,i):
            if ((i % j)== 0):
                state=1
        if (state==0):
                print(i)
                    
limiteinf = int(input("enter la limite inferieure: "))
limitesup = int(input("entrer la limite superieure: "))
nombre_premier(limiteinf, limitesup)








os.system("pause")
