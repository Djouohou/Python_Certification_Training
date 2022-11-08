import os
"""
def affiche():
    return "hello world"
val=affiche()
print(val)
val2=affiche()
print(val2)
"""
"""
#ici il s'agit d'une procedure
def somme_de_deux_nombres(a,b):
    sum=a+b
    print(sum)
somme_de_deux_nombres(2,8)
"""
"""
def somme(*liste):
    sum=0
    for i in liste:
        sum=sum+i
    return sum
print(somme(14,15,14,15,45,41))
"""
"""
#en utilisant une fonction
#EXERCICE1
def table_multiplication(mul,borninf,bornsup):
    for i in range(borninf,bornsup):
        b=(i," x ",mul," = ",i*mul)
    return b
mul=int(input("veuillez entrer le multiplicateur:"))
borninf=int(input("entrer la borne inferieur:"))
bornsup=int(input("entrer la borne superieur:"))
print(table_multiplication(mul,borninf,bornsup))
"""
"""
#en programmant simplement
mul=int(input("veuillez entrer le multiplicateur:"))
borninf=int(input("entrer la borne inferieur:"))
bornsup=int(input("entrer la borne superieur:"))
for i in range(borninf,bornsup):
    print(i," x ",mul," = ",i*mul)

#EXERCICE2
def cube(a):
    cub=a**3
    return cub
a=int(input("entrer la valeur de a: "))
print(cube(a))

def volumesphere(r):
    def cube(a):
        r=a**3
        return r
    vol=1.3333*3.14*(r)
    return vol
print(volumesphere(1))

#EXERCICE3
# Exemples
n=int(input('donner n'))
for x in range(0,n):
	print (x*"*")
# inverse 
n=int(input('donner n'))
for x in range(n,0,-1):
	print (x*"*")

def triangle_motif(n,motif) :   
    for i in range (1,n+1):
        s='*'
        for j in range(1,i):
            s+=motif
        print(s)
n=int(input('entrer la valeur de n: '))
triangle_motif(n,"*")"""
"""
def triangle_isocéle(n):
    for i in range(1,n+1):
        tri=(" "*(n-i)+"* "*i)
        print(tri)
triangle_isocéle(int(input("entrer le nombre de ligne: ")))
"""
#EXERCICE5
"""n=int(input('entrer la valeur de n: '))
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
    for j in range (i):
        print( p ,end="")
    for j in range(i+1):
        print( p ,end="")
    p=p+1
    print()

#EXERCICE4
def maximum (a,b,c):
    if a>b and a>c:   
        return a
    if b>a and b>c:
        return b
    if c>a and c>b:
        return c
a=int(input("veuillez entrer votre premier nombre: "))
b=int(input("veuillez entrer votre second nombre: "))
c=int(input("veuillez entrer votre troisième nombre: "))
print(maximum (a,b,c))
"""
"""
#EXERCICE6
def chiffreportebonheur(nb):
    for number in nb:
        return number
    number=number**2

print("veuillez entrer votre nombre")
nb=int(input("nombre de depart: "))
print(nb)
chiffreportebonheur(nb)
def chiffreportebonheur (nb):
    s=0
    for k in str(nb):
        s=s+(int(k)*int(k))
    print (s)
    i=s
    while i:
         
print("veuillez entrer votre nombre")
nb=int(input("nombre de depart: "))
print (chiffreportebonheur(nb))
"""
#EXERCICE7et8
"""phrase=str(input("entrer votre phrase: "))
print(phrase)
mot=(phrase.split(" "))
print(mot)
print(len(mot))

def comptemots(phrase):
    return print(len(phrase.split(" ")))
phrase=str(input("entrer votre phrase: "))
(comptemots(phrase))

def somme(a,b):
    return a+b
def moyenne(a,b):
    s=somme(a,b)
    return s/2
print(moyenne(10,14))

def update_score(current,value):
    current = current + value
    return current
current=int(input("entrer le score actuel: "))
value=int(input("entrer la valeur à ajouter: "))
print(update_score(current,value))

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
def calc_calories (miles, calories_per_mile):
    calories = miles * calories_per_mile
    return calories
distance = int(input("combien de miles avez-vous fait cette semaine?: "))
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
def NbCMin():
    min=0
    z=len(mdp)
    for i in range(0,z):
        if (mdp[i] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']):
            min=min+1
        else:
            pass
    print(min)
mdp=input("veuillez enter votre mot de passe: ")
NbCMin()

def NbCMaj():
    maj=0
    z=len(mdp)
    for i in range(0,z):
        if (mdp[i] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']):
            maj=maj+1
        else:
            pass
    print("le nombre de caracteres en majuscules est: ", maj)
mdp=input("veuillez enter votre mot de passe: ")
NbCMaj()

def NbCAlpha():
    alpha=0
    z=len(mdp)
    for i in range(0,z):
        if (mdp[i] in ['0', '1', '2', '3', '4', '5', '6', '8', '9']):
            alpha+=1
        else:
            pass
    print("le nombre de caracteres non alphabetique est: ", alpha)
mdp=input("veuillez enter votre mot de passe: ")
NbCAlpha()


def LongMaj():
    list=mdp.split()
    mot1=""
    for i in list:
        if len(i)>len(mot1):
            mot1=i
        else:
            pass
    print("la plus longue séquence de lettres majuscules est ", mot1,"qui compte",len(mot1) ,"caractères")
mdp=input("veuillez enter votre mot de passe: ")    
LongMaj()


def LongMin():
    list=mdp.split()
    mot2=list
    for i in list:
        if len(i)<len(mot2):
            mot2=i
        else:
            pass
    print("la plus longue séquence de lettres minuscules est ", mot2,"qui compte",len(mot2) ,"caractères")
mdp=input("veuillez enter votre mot de passe: ")    
LongMin()


#Nombre total de caractères=ntc

def somme_de_bonus():
    list=mdp.split()
    ntc=len(list)
    sommedebonus = ((ntc)*4)+((ntc- NbCMaj())*2)+((ntc - NbCMin())*3)+((LongMaj())*5)
    return sommedebonus
mdp=input("veuillez enter votre mot de passe: ")
print(somme_de_bonus())

def somme_des_penalites():
    sommedespenalites = ((LongMin())*2)+((LongMaj())*3)
    return sommedespenalites
print(somme_des_penalites())
def Score():
    S=(somme_de_bonus())-(somme_des_penalites())
    return(S)
print(Score())


#EXERCICE12


min = int(input("Entrez le min : "))
max = int(input("Entrez le max : "))
for n in range(min,max + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)

def nombre_premier():
    for i in range (limiteinf, limitesup+1):
        if i > 1:
            for j in range(2,i):
                if (i % j)== 0:
                    break
            else:
                print(i)
limiteinf = int(input("enter la limite inferieure: "))
limitesup = int(input("entrer la limite superieure: "))
nombre_premier()
"""
def get_name ():
    name=input("quel est votre nom ?")
    return name
def calc_calories (miles,calories_per_mile ):
    calories = miles * calories_per_mile
    return calories
distance = int(input("combien de miles avez-vous fait cette semaine? "))
burn_rate = 50
biker = get_name()
calories_burned = calc_calories(distance,burn_rate)
print(biker, "vous avez bruler à propos " ,calories_burned, "calories.")












os.system("pause")
