#https://www.tresfacile.net/tp-exercices-avec-solutions-sur-les-fichiers-file-io-en-python/

Exercice 1

Ecrire un programme Python qui permet de créer un fichier sur le bureau nommé monFichier.txt et décrire le texte
T="Python est un langage de programmation orienté objet".
Ecrire un programme Python qui permet lire le fichier  monFichier.txt.

with open('monfichier.txt', 'w') as fichier:
    fichier.write("Python est un langage de programmation orienté objet") 

with open('monfichier.txt', 'r') as fichier:
    print(fichier.read())




#https://holypython.com/intermediate-python-exercises/exercise-16-python-list-comprehensions/

#exercice 1: Create an identical list from the first list using list comprehension.
lst1=[1,2,3,4,5]

#Type your answer here.
lst2=[x for x in lst1]

print(lst2)  #[1,2,3,4,5]

#exercice 2: Use list comprehension to contruct a new list but add 6 to each item.
lst1=[44,54,64,74,104]

lst2=[x+6 for x in lst1]

print(lst2) #[50, 60, 70, 80, 110]


#exercice 3: Create a list from the elements of a range from 1200 to 2000 with steps of 130, using list comprehension.
rng= range(1200, 2000, 130) ou encore (x for x in range(1200,2000,130))

lst=[i for i in rng]

print(lst)     #[1200, 1330, 1460, 1590, 1720, 1850, 1980]

#exercice4: Using list comprehension, construct a list from the squares of each element in the list.
lst1=[2, 4, 6, 8, 10, 12, 14]

#Type your answer here.
lst2=[x**2 for x in lst1]
print(lst2) #[4, 16, 36, 64, 100, 144, 196]


#exercice5: Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50.
lst1=[2, 4, 6, 8, 10, 12, 14]

#Type your answer here.
lst2=[x**2 for x in lst1 if x**2>50]    #[64, 100, 144, 196]
print(lst2)


#exercice6: Given dictionary is consisted of vehicles and their weights in kilograms. Contruct a list of the names of vehicles with weight below 5000 kilograms.
In the same list comprehension make the key names all upper case.

dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

#Type your answer here.
lst=[keys.upper() for keys in dict.keys() if dict[keys]<5000]

print(lst)    #['SEDAN', 'SUV', 'PICKUP', 'MINIVAN', 'VAN', 'BICYCLE', 'MOTORCYCLE']


#exo
liste=['pomme', 'orange', 'mangue', 'raison', 'poire', 'pastèque']
nouvelle_liste=[elem for elem in liste if elem.startswith('p') or elem.startswith('o')]
print(nouvelle_liste)



#https://towardsdatascience.com/beginner-to-advanced-list-comprehension-practice-problems-a89604851313

#Find all of the numbers from 1–1000 that are divisible by 8




    Find all of the numbers from 1–1000 that have a 6 in them
    Count the number of spaces in a string (use string above)
    Remove all of the vowels in a string (use string above)
    Find all of the words in a string that are less than 5 letters (use string above)
    Use a dictionary comprehension to count the length of each word in a sentence (use string above)
    Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit besides 1 (2–9)
    For all the numbers 1–1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by



#https://python.developpez.com/tutoriels/apprendre-programmation-python/notions-avancees/?page=classe

#EXERCICES PROGRAMMATION ORIENTEE OBJET
#https://www.tresfacile.net/tp-poo-et-les-classes-en-python3-exercices-avec-solutions/

#Exercice 2. Classe Compte bancaire :
"""
    Créer une classe Python nommée CompteBancaire qui représente un compte bancaire, ayant pour attributs : numeroCompte (type numérique ) ,
    nom (nom du propriétaire du compte du type chaine), solde.
    Créer un constructeur ayant comme paramètres : numeroCompte, nom, solde.
    Créer une méthode Versement() qui gère les versements.
    Créer une méthode Retrait() qui gère les retraits.
    Créer une méthode Agios() permettant d'appliquer les agios à un pourcentage de 5 % du solde.
    #Les agios désignent, dans le domaine bancaire, l'ensemble des frais perçus par la banque pour le fonctionnement d'un compte à l'occasion d'opérations particulière.
    Créer une méthode afficher() permettant d’afficher les détails sur le compte
    Donner le code complet de la classe CompteBancaire.
"""
class CompteBancaire:
    def __init__(self,numeroCompte, nom, solde):
        self.numeroCompte = numeroCompte
        self.nom = nom
        self.solde = solde

    def __str__(self):
        return 'Le solde de départ est: ' + str(self.solde)
        

    def Versement(self,ver):
        self.solde += ver
        return 'versement: ' + str(ver)

    def Retrait(self, ret):
        self.solde -= ret
        return 'retrait: '+ str(ret)

    def Agios(self):
        agio = (self.solde * 5)/100
        self.solde = self.solde - agio
        return 'agios: ' + str(agio)

    def Afficher(self):
        return 'Le compte numero '+str(self.numeroCompte)+',appartenant à mr/mrs ' +str(self.nom)+' a pour solde '+str(self.solde)+' euro.'
    
objet = CompteBancaire(9, 'sophie', 20000)
print(objet)
print(objet.Versement(10000))
print(objet.Retrait(5000))
print(objet.Agios())
print(objet.Afficher())

#AUTRES SOLUTIONS

#coding: utf-8
class CompteBancaire:
    def __init__(self, idNumber, nomPrenom, solde):
        self.idNumber = idNumber
        self.nomPrenom = nomPrenom
        self.solde = solde
        
    def versement(self, argent):
        self.solde = self.solde + argent
    
    def retrait(self, argent):
        if(self.solde < argent):
            print(" Impossible d'effectuer l'opération. Solde insuffisant !")
        else:
            self.solde = self.solde - argent
    
    def agios(self):
        self.solde =self.solde*95/100
    
    def afficher(self):
        print("Compte numéro : " , self.idNumber)
        print("Nom & Prénom : ", self.nomPrenom)
        print(" Solde  : ", self.solde , " DH ")
        print("Sauf erreur ou omisssion ! ")
        
monCompte = CompteBancaire(16168891, " Benoit Beppe", 26000)
monCompte.versement(35000)
monCompte.retrait(47)
#monCompte.agios()
monCompte.afficher()


#Exercice 3. Classe Cercle 
"""
    Définir une classe Cercle permettant de créer un cercle C(O,r) de centre O(a,b) et de rayon r à l'aide du constructeur :

    def __init__(self , a , b , r):
        self.a = a
        self.b = b
        self.r = r

    Définir une méthode Surface() de la classe qui permet de calculer la surface du cercle
    Définir une méthode Perimetre() de la classe qui permet de calculer le périmètre du cercle
    Définir une méthode testAppartenance() de la classe qui permet de tester si un point A(x,y) appartient ou non au cercle C(O,r)
"""

import math
class Cercle:

    def __init__(self , a , b , r):
        self.a = a
        self.b = b
        self.r = r

    def Surface(self):
        S = ((self.r)**2)*math.pi
        return 'surface: '+str(S)

    def Perimetre(self):
        P = 2 * self.r * math.pi
        return 'perimetre: '+str(P)

    def testAppartenance(self, x, y):
        OA = math.sqrt(((x - self.a)**2) + ((y - self.b)**2))
        if OA <= self.r:
            print ('le point A(x,y) appartient au cercle C de centre O et de rayon r.')
        else :
            print("le point A(x,y) n'appartient pas au cercle C.")

obj = Cercle(3,4,5)
print(obj.Surface())
print(obj.Perimetre())
obj.testAppartenance(6,7)


#Exercice 4. Classe Calcul arithmétique 
"""
    1. Créer une classe Calcul ayant un constructeur par défaut (sans paramètres) permettant d’effectuer différents calculs sur les nombres entiers.
    2. Créer au sein de la classe Calcul une méthode nommée Factorielle() qui permet de calculer le factorielle d'un entier.
    Tester la méthode en faisant une instanciation sur la classe.
    3. Créer au sein de la classe Calcul une méthode nommée Somme() permettant de calculer la somme des n premiers entiers:  1 + 2 + 3 + .. + n. Tester la méthode.
    4. Créer au sein de la classe Calcul une méthode nommée testPrim() permettant de tester la primalité d'un entier donné. Tester la méthode.
    5. Créer au sein de la classe Calcul une méthode nommée testPrims() permettant de tester si deux nombres sont premier entre eux.
    6. Créer une méthode tableMult() qui crée et affiche la table de multiplication d'un entier donné.
    Créer ensuite une méthode allTablesMult() permettant d'afficher toutes les tables de multiplications des entiers 1, 2, 3, ..., 9.
    7. Créer une méthode  listDiv() qui récupère tous les diviseurs d'un entier donné sur une liste Ldiv.
    Créer une autre méthode listDivPrim() qui récupère tous les diviseurs premiers d'un entier donné
"""
import math

class Calcul:
    def __init__(self):
        pass

    def Factorielle(self, ent):
        fac = math.factorial(ent)
        return fac
    
    def Somme(self, n):
        s = (n*(n+1))/2
        return s

    def testPrim():
        
    
obj = Calcul()
print(obj.Factorielle(10))
print(obj.Somme(5))


#Solution
#coding: utf-8
class Calcul:
    def __init__(self):
        pass
#---Factorielle ------------    
    def factorielle(self, n):
        j=1
        for i in range(1,n+1):
            j = j*i
        return j
#---Somme des n premiers nombres----
    def somme(self, n):
        j=1
        for i in range(1,n+1):
            j = j+i
        return j
#---Test primalité d'un nombre------------
    def testPrim(self, n):
        j=0
        for i in range(1,n+1):
            if(n%i==0):
                j = j + 1
        if(j == 2):
            return True
        else:
            return False 
            
# ---Test primalité de deux nombres entiers------------
    def testprims(self , n , m):
        divCommun = 0
        for i in range(1 , n+1):
            if (n%i == 0 and m%i == 0):
                divCommun = divCommun + 1
        if divCommun == 1:
            print("Les nombres " , n , " et ", m , " sont premiers entre eux")
        else:
            print("Les nombres " , n , " et ", m , " ne sont pas premiers entre eux")
            
#---Table de multiplication-------------
    def tableMult(self,k):
        for i in range(1,10):
            print(i," x ",k," = ",i*k)

#---Toutes les tables de multiplication des nombres 1, 2, .., 9
    def toutesLesTables(self):
        for k in range(1,10):
            print("\nla table de multiplication de : ",k, " est : ")
            for i in range(1,10):
                print(i," x ",k," = ",i*k)
                
#----- liste des diviseurs d'un entier                
    def listDiv(self , n):
        # initialisation de la liste des diviseurs
        lDiv = []
        for i in range(1 , n+1):
            if ( n%i == 0):
                lDiv.append(i)
        return lDiv
    
# ------liste des diviseurs premiers d'un entier----------------    
    def listDivPrim(self , n):
        # initialisation de la liste des diviseurs
        lDiv = []
        for i in range(1 , n+1):
            if ( n%i == 0 and self.testPrim(i)):
                lDiv.append(i)
        return lDiv                 
                
# Exemple Instanciation
Cal = Calcul()
Cal.testprims(13 , 7)
print("Liste des diviseurs de 18 : ", Cal.listDiv(18))
print("Liste des diviseurs premiers de 18 : ", Cal.listDivPrim(18))
Cal.toutesLesTables()






#Exercice 6 
"""
1. Définir une classe Book avec les attributs suivants : Title, Author (Nom complet), Price.
2. Définir un constructeur ayant comme attributs: Title, Author, Price.
3. Définir la méthode View() pour afficher les informations d'une instance object Book.
4. Ecrire un programme pour tester la classe Book.
"""
class Book :
    def __init__(self, Title, Author, Price):
        self.Title = Title
        self.Author = Author
        self.Price = Price

    def view(self):
        print('le titre est: ',self.Title)
        print("l'auteur est: ",self.Author)
        print('il coute: ',self.Price)
        
object_book = Book('mon histoire' , 'benoit beppe', 'cent euro')
object_book.view()



#Exercise 7 Classe Geometry 
"""
Ecrire une classe Python nommée Geometry avec un constructeur par défaut sans paramètres.
1. Ajouter une méthode nommée distance() à la classe geometry qui permet de calculer la distance entre deux points

A = (a1, a2), B = (b1, b2) (avec la convention: un point est identifié à ses coordonnées M = (xM , yM) )
2. Ajouter une méthode nommée middle() à la classe geometry qui permet de déterminer le milieu d'un bipoint (A , B).
3. Ajouter une méthode nommée trianglePerimeter() à la classe geometry qui permet de calculer le périmètre d'un triangle ABC.
4. Ajouter une méthode nommée triangleIsoscel() qui renvoie True si le triangle est isoscel et False sinon.
"""
import math

class Geometry:
    def __init__(self):
        pass

    def distance(self,a1,a2,b1,b2):
        AB = math.sqrt(((a1 - a2)**2) + ((b1 - b2)**2))
        return AB

    def middle(self,a1,a2,b1,b2):
        I1 = (a1 + a2)/2
        I2 = (b1 + b2)/2
        return I1,I2
        
    def trianglePerimeter(self,AB,BC,AC):
        P=AB+BC+AC
        return P

    def triangleIsoscel(self,AB,BC,AC):
        if AB == BC or AB == AC or AC == BC:
            return True
        else :
            return False
    
obj=Geometry()
print(obj.distance(2,6,3,7))
print(obj.middle(2,6,3,7))
print(obj.trianglePerimeter(15,31,9))        
print(obj.triangleIsoscel(15,31,31))        



#Exercice 5:
"""
Coder une classe  myString permettant de doter les chaines de caractères des méthodes append() et pop() faisant les mêmes opérations que celles des listes.
Exemple si on crée  des chaines via l'instanciation s1 = myString("Hello") et s2 = "bonjour", et on lui applique les méthodes :

print(s1.append(" world !")) # affiche  'Hello world !'
print(s2.pop(2))  # affiche 'bojour'  
"""

class myString:

    def __init__(self,s):
        self.s = s

    def append(self,mot):
        return self.s + str(mot)

    def pop(self,i):
        s1 = self.s[0:i]
        s2 = self.s[i+1:len(self.s)]
        return s1+s2

s = myString('Hello')
print(s.append(" world !"))
print(s.pop(1))










































































































































