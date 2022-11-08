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
        
object_book = Book('mon histoire' , 'sophie ingrid', 'cent euro')
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

    def testPrim(nb):  #ici on regarde si ce nombre n'a aucun diviseur entre 2 et lui meme.Vu que tous les diviseur d'un nombre sont inferieur à lui-meme.
        for i in range (2,nb):
            if nb%i==0:
                return False
        return True

    def Prims(x,y):  #on cherche les diviseurs commun entre les deux et si ce diviseur est 1 alors il le sont.
        for i in range (2,x+1): #on doit mettre range n+1 car ca peut arriver que le plus petit soit diviseur du plus grand
            for j in range(2,y+1):
                if i==j:
                    if x%i == 0 and y%j == 0:
                        return False
        return True

    def tableMult(nbre):
        for i in range(10):
            print (str(i)+' * '+str(nbre)+' = '+str(i*nbre))

    def allTablesMult():
    for j in range(1,10):
        for i in range(10):
            print (str(i)+' * '+str(j)+' = '+str(i*j))
        print('------------------------')

    def listDiv(nbre):
    Ldiv = []
    for i in range(1,nbre+1):
        if nbre%i==0:
            Ldiv.append(i)
    return Ldiv

print(listDiv(20))


def listDivPrim(nbre):
    Ldiv = []
    liste = []
    for i in range(1,nbre+1):
        if nbre%i==0:
            Ldiv.append(i)
            liste.append(i)
    for x in Ldiv:
        for y in range(2,x):
            if x%y==0:
                if x in liste:
                    liste.remove(x)
    return liste

print(listDivPrim(100))


    
obj = Calcul()
print(obj.Factorielle(10))
print(obj.Somme(5))
print(obj.testPrims(10))
print(obj.Prims(3,21))
tableMult(9)
allTablesMult()


#EXERCICES POO PDF

#Exercice 1:
"""
On considère une classe Personnage représentant un personnage de Jeu.
Le plateau de jeu est représenté par un repère orthonormé à trois axes.
La position du joueur dans le plateau est repérée par ses attributs x, y, z.
1) Ecrire un constructeur initialisant les mesures.
2) Ecrire les méthodes avance, droite et saute permettant respectivement de faire avancer, aller
à droite et sauter le personnage, c’est-à-dire d’augmenter de 1 respectivement x, y et z.
3) Implémenter une autre méthode coord renvoyant les coordonnées sous forme d’un triplet.
4) Essayer avec : Laura = Personnage(0, 0, 0)
"""
class Personnage:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def avance(self):
        a = self.x + 1
        return a

    def droite(self):
        b = self.y + 1
        return b

    def saute(self):
        c = self.x + 1
        return c

    def coord(self):
        return self.avance(),self.droite(),self.saute()

Laura = Personnage(0,0,0)
print(Laura.coord())



#Exercice 2
"""
Voici un programme en Python :
import random
class Piece :
def alea(self) :
return random.randint(0,1)
def moyenne(self, n):
tirage = [ ]
for i in range (n) :
tirage.append( self.alea() )
return sum(tirage) / n
p = Piece()
print( p.moyenne(100) )
Expliquer en détail ce qu’il permet d’afficher
"""
Tout d'abord le code importe le module random.
Ce programme effectue un lance d'une piece et choisi aleatoirement deux entier entre
soit 0 soit 1. Puis il calcule la moyenne des aleas possible des 100 lances.



#Exercice 3
"""
On considère une classe Carre admettant la mesure des côtés d’un carré en attribut.
1) Ecrire un constructeur initialisant les mesures.
2) Ecrire les méthodes :
• perimetre , permettant de retourner le périmètre du carré.
• aire permettant de retourner son aire.
3) Créer des exemples
"""
class Carre :
   def __init__(self, cote):
       self.cote = cote

    def Perimetre (self):
        return self.cote*4

    def aire(self):
        return self.cote * self.cote

ex=Carre(9)
ex2=Carre(32)
print(ex.Perimetre())


#Exercice 4
"""
Définir une classe Fraction pour représenter un nombre rationnel.
Cette classe possède deux attributs num et denom, qui sont des entiers et désignent
respectivement le numérateur et le dénominateur.
De plus, on demande que le dénominateur soit particulièrement un entier strictement positif.
1) Ecrire un constructeur de cette classe.
Le constructeur doit lever une ValueError si le dénominateur fourni n’est pas strictement positif. Pour cela, on utilise : raise 
2) Ajouter une methode __str__ qui renvoie une chaîne de caractère de la forme "12 / 13", ou
simplement de la forme "12" lorsque le dénominateur vaut 1.( __str__(self) est une méthode de Python : renvoie une chaîne de caractères)
3) Ajouter des méthodes __eq__ et __lt__ qui reçoivent une deuxième fraction en argument et
renvoie True si la première fraction représente respectivement un nombre égal ou un nombre strictement inférieur à la fraction.
( __lt__(self, u) est une méthode de Python : Pour self = t, elle renvoie True si t est strictement plus petit que u )
( __eq__(self, u) est une méthode de Python : Pour self = t, elle renvoie True si t est égal à u )
4) Ajouter des méthodes __add__ et __mul__ qui reçoivent une deuxième fraction en argument et
renvoie une nouvelle fraction représentant respectivement la somme et le produit des deux fractions.
5) Tester ces opérations
6) Question bonus : S’assurer que les fractions sont toujours sous forme réduite.

"""

# f1, f2, f3, f4 sont recuperés sous forme de chaine de caractères

class Fraction:
    def __init__(self, num, denom):
       self.num = num  
       self.denom = denom  #entier strictement positif
       if self.denom <= 0:
           raise ValueError('vous devez entrer un denom positif')

    def __str__(self):
        if self.denom == 1:
            return str(self.num)
        else :
            return str(self.num)+ '/' +str(self.denom)

    def __eq__(self, f1):
        v=f1.split('/')
        if (self.num/self.denom) == (int(v[0])/int(v[1])):
            return True
        return False

    def __lt__(self, f2):
        v=f2.split('/')
        if (self.num/self.denom) < (int(v[0])/int(v[1])):
            return True
        return False

    def __add__(self, f3):
        v=f3.split('/')
        snum = (self.num * int(v[1])) + (self.denom * int(v[0]))
        sdeno = self.denom * int(v[1])
        return str(snum)+'/'+str(sdeno)
            

    def __mul__(self, f4):
        v=f4.split('/')
        snum = self.num * int(v[0])
        sdeno = self.denom * int(v[1])
        return str(snum)+'/'+str(sdeno)

    
#fract1=Fraction(9,0)
fract2=Fraction(9,1)
fract3=Fraction(4,8)

#print(fract1.__main__())
print(fract2.__str__())
print(fract2.__str__())
print(fract3.__eq__('35/8'))
print(fract3.__lt__('35/8'))
print(fract3.__add__('35/8'))
print(fract3.__mul__('35/8'))


#solution dernière question
class Fraction:
    def __init__(self, num, denom):
       self.num = num  
       self.denom = denom  #entier strictement positif
       if self.denom <= 0:
           raise ValueError('vous devez entrer un denom positif')

    def __str__(self):
        if self.denom == 1:
            return str(self.num)
        else :
            return str(self.num)+ '/' +str(self.denom)

    def __eq__(self, f1):
        v=f1.split('/')
        if (self.num/self.denom) == (int(v[0])/int(v[1])):
            return True
        return False

    def __lt__(self, f2):
        v=f2.split('/')
        if (self.num/self.denom) < (int(v[0])/int(v[1])):
            return True
        return False

    def __add__(self, f3):
        v=f3.split('/')
        snum = (self.num * int(v[1])) + (self.denom * int(v[0]))
        sdeno = self.denom * int(v[1])
        return str(snum)+'/'+str(sdeno)

#la fonction qui renvoie les diviseurs d'un nombre est differentes de celle qui renvoie (les diviseurs de) la decomposition en produit de facteur premier.
#Exemple: leur diviseur de 12 sont 2,3,4,6 mais en decomposition de facteur premier les diviseurs obtenus sont 2,2,3
    def decomposition(self, nbre):
        Ldiv = []
        for i in range(2,int(nbre/2)):
            while nbre%i==0:
                c = nbre/i
                nbre=c
                Ldiv.append(i)
        return Ldiv

    def mul(self, liste):
        val = 1
        for i in liste:
            val=val*i
        return val 

            

    def __mul__(self, f4): #parcourir les deux et voir s'il ya un element dans la liste du num et du denom , on le retire dans les deux listes.
        #pour mettre une fraction sous forme reduite on la decompose en produit de facteur premier.(recuperer la liste de ses diviseurs tel que en les multipliant on obtient le nombre de depart)
        v=f4.split('/')
        snum = self.num * int(v[0])
        sdeno = self.denom * int(v[1])
        lnum = self.decomposition(snum)#liste des diviseurs du numerateur
        ldeno = self.decomposition(sdeno)#liste des diviseurs du denominateur

        secondlist = []
        if len(lnum) > len(ldeno):
            tmp = lnum
            secondlist = ldeno
        else:
            tmp = ldeno
            secondlist = lnum
            
        for i in tmp:
            if i in secondlist:
                ldeno.remove(i)
                lnum.remove(i)
        return str(self.mul(lnum))+'/'+str(self.mul(ldeno))
#si une des liste remove tous ses elements alors la fraction renverra soit 1/1, soit 1/x, soit x/1 car dans la methode mul, val = 1.
    #donc la liste etant vide, la boucle for dans val ne va pas se declenche d'ou val=1 sera retourné.

    
#fract1=Fraction(9,0)
fract2=Fraction(9,1)
fract3=Fraction(4,8)

#print(fract1.__main__())
print(fract2.__str__())
print(fract2.__str__())
print(fract3.__eq__('35/8'))
print(fract3.__lt__('35/8'))
print(fract3.__add__('35/8'))
print(fract3.__mul__('7/11'))


#EXERCICE 12.7 G.SWINNEN
'''
12.7 Definissez une classe JeuDeCartes() permettant d’instancier des objets dont le comportement soit similaire à celui d’un vrai jeu de cartes. La classe devra
comporter au moins les quatre méthodes suivantes :
• méthode constructeur : création et remplissage d’une liste de 52 éléments, qui sont
eux-mêmes des tuples de 2 entiers. Cette liste de tuples contiendra les caractéristiques
de chacune des 52 cartes. Pour chacune d’elles, il faut en effet mémoriser séparément un entier indiquant la valeur (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
les 4 dernières valeurs étant celles des valet, dame, roi et as), et un autre entier indiquant la couleur de la carte (c’est-a-dire 3,2,1,0 pour Coeur, Carreau, Trefle et Pique).
Dans une telle liste, l’élément (11,2) désigne donc le valet de Trefle, et la liste terminée doit être du type :
[(2, 0), (3,0), (3,0), (4,0), ..... (12,3), (13,3), (14,3)]
• méthode nom_carte() : cette méthode doit renvoyer, sous la forme d’une chaine,
l’identité d’une carte quelconque dont on lui a fourni le tuple descripteur en argument.
Par exemple, l’instruction : print(jeu.nom_carte((14, 3))) doit provoquer
l’affichage de : As de pique
• méthode battre() : comme chacun sait, battre les cartes consiste à les mélanger.
Cette méthode sert donc à mélanger les éléments de la liste contenant les cartes,
quel qu’en soit le nombre.
• méthode tirer() : lorsque cette méthode est invoquée, une carte est retirée du jeu.
Le tuple contenant sa valeur et sa couleur est renvoyé au programme appelant. On
retire toujours la première carte de la liste. Si cette méthode est invoquée alors qu’il
ne reste plus aucune carte dans la liste, il faut alors renvoyer l’objet spécial None au
programme appelant. Exemple d’utilisation de la classe JeuDeCartes() :
jeu = JeuDeCartes() # instanciation d'un objet
jeu.battre() # mélange des cartes
for n in range(53): # tirage des 52 cartes :
c = jeu.tirer()
if c == None: # il ne reste plus aucune carte
print('Termine !') # dans la liste
else:
print(jeu.nom_carte(c)) # valeur et couleur de la carte
'''
import random

class JeuDeCartes:
    def __init__(self):
        self.liste = []
        self.val = 0
        self.coul = 0
        for i in range (2, 15):
            self.val = i
            for j in range(4):
                self.coul = j
                x=(i, j)
                self.liste.append(x)
                self.liste.sort(key=lambda x: x[1])
        print (self.liste)

    def nom_carte(self, m):
        dico1 = {2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'Valet', 12:'Dame', 13:'Roi',14:'As'}
        dico2 = {0:'Coeur', 1:'Carreau', 2:'Trefle', 3:'Pique'}
        if m[0] not in dico1 or m[1] not in dico2:
            return str(m[0])+' de '+str(m[1])
        else:
            return str(dico1[m[0]])+' de '+str(dico2[m[1]])
            

    def battre(self):
        random.shuffle(self.liste)
        return self.liste

    def tirer(self):
        while len(self.liste)>0:
            x = self.liste.pop(0)
            return x      #ou  return jeu.nom_carte(x)
        else:
            return None
            

jeu = JeuDeCartes() 
print(jeu.nom_carte((14, 3)))
print(jeu.battre()) 
for n in range(53): # tirage des 52 cartes :
    c = jeu.tirer()
    if c == None: # il ne reste plus aucune carte
        print('Termine !') # dans la liste
    else:
        print(jeu.nom_carte(c)) # valeur et couleur de la carte

















