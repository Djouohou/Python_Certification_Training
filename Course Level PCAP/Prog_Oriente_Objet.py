 class MyClass:
    x=5

print(MyClass)  #<class '__main__.MyClass'>

p1=MyClass()
print(p1)  #<__main__.MyClass object at 0x000001F3CB7F1C00>

print(p1.x)#5

p2=MyClass(10)
print(p2.x)   #5

#ci_dessus, p1 et p2 ont la meme valeur 5 mais avec la fonction init, on a la possibilite de
class MyClass:
    def __init__(self,x):
        self.x=x

p1=MyClass(5)
print(p1.x)  #5

p2=MyClass(10)
print(p2.x)   #10

#exercice d'apllication:
creer une classe Personne. une personne a pour caracteristiques: nom,prenom,age, taille,teint, couleur de cheveux.
creer deux personne et pour chaque personnne afficher les infos qui lui sont liees.

class Personne:
    def __init__(self,a,b,c,d,e,f):
        self.nom=a
        self.prenom=b
        self.age=c
        self.taille=d
        self.teint=e
        self.couleur_cheveux=f

p1=Personne('julianna','bemo',35,179,'noir','blonde')
print("p1 s'appelle {} {},a {} ans et fais {} cm de taille, de teint {} et avec une couleur de cheveux {}".format(p1.nom,p1.prenom,p1.age,p1.taille,p1.teint,p1.couleur_cheveux))  

p2=Personne('christy','oliver',19,155,'blanc','brune')
print("p2 s'appelle {} {},a {} ans et fais {} cm de taille, de teint {} et avec une couleur de cheveux {}".format(p2.nom,p2.prenom,p2.age,p2.taille,p2.teint,p2.couleur_cheveux))  
#si les deux personnes ont le meme age de 35 ans ,on va directement affecter 35 a self.age et on aura plus besoin de passer c en parametre,ni dans la definition ni dans l'appel.


#Une classe peut contenir plusieurs autres methodes en dehors de --init--.
class MyClass:
    def __init__(self,val):
        self.x=val
        self.y=10

    def info(self):
        return str(self.x) + ',' + str(self.y)

p1=MyClass(5)

print(p1.info()) #5,10


#ajouter une methode qui renvoie toutes les informations sur une personne
class Personne:
    def __init__(self,a,b,c,d,e,f):
        self.nom=a
        self.prenom=b
        self.age=c
        self.taille=d
        self.teint=e
        self.couleur_cheveux=f

    def information(self):
        return self.nom, self.prenom, self.age, self.taille, self.teint, self.couleur_cheveux
        

p1=Personne('julianna','bemo',35,179,'noir','blonde')
print(p1.information())  #('julianna', 'bemo', 35, 179, 'noir', 'blonde')

p2=Personne('christy','oliver',19,155,'blanc','brune')
print(p2.information())  #('christy', 'oliver', 19, 155, 'blanc', 'brune')


#ajouter une methode qui augmente l'age de la personne de 10 ans.
class Personne:
    def __init__(self,a,b,c,d,e,f):
        self.nom=a
        self.prenom=b
        self.age=c
        self.taille=d
        self.teint=e
        self.couleur_cheveux=f

    def information(self):
        return self.nom, self.prenom, self.age, self.taille, self.teint, self.couleur_cheveux
    def newage(self):
        self.age=self.age + 10
     
        
p1=Personne('julianna','bemo',35,179,'noir','blonde')
p1.newage()
print(p1.information())  #('julianna', 'bemo', 45, 179, 'noir', 'blonde')

p2=Personne('christy','oliver',19,155,'blanc','brune')
p2.newage()
print(p2.information())   #('christy', 'oliver', 29, 155, 'blanc', 'brune')


#ajouter une methode qui augmente l'age de la personne d'une valeur quelconque.
class Personne:
    def __init__(self,a,b,c,d,e,f):
        self.nom=a
        self.prenom=b
        self.age=c
        self.taille=d
        self.teint=e
        self.couleur_cheveux=f

    def information(self):
        return self.nom, self.prenom, self.age, self.taille, self.teint, self.couleur_cheveux
    def newage(self,age):
        self.age=self.age + age
     
        
p1=Personne('julianna','bemo',35,179,'noir','blonde')
p1.newage(15)
print(p1.information())   #('julianna', 'bemo', 50, 179, 'noir', 'blonde')

p2=Personne('christy','oliver',19,155,'blanc','brune')
p2.newage(30)
print(p2.information())  #('christy', 'oliver', 49, 155, 'blanc', 'brune')


#EXERCICE: Ecrire une classe en langage python permettant de construire un rectangle dotee d'attributs longueur et largeur.
#Ecrire une methode Perimettre() permettant de calculer le perimetre et une methode surface permettant de calculer la surface du rectangle.
#creer les getters et les setters

class Rectangle:
    def __init__(self,longueur,largeur):
        self.__longueur=longueur
        self.__largeur=largeur

    def Perimetre(self):
       return (self.__longueur + self.__largeur)*2

    def Surface(self):
        return self.__longueur * self.__largeur 

    def get__longueur(self):
        return self.__longueur
    def set__longueur(self,x):
        self.__longueur=x

    def get__largeur(self):
        return self.__largeur
    def set__largeur(self,y):
        self.__largeur=y
    
    

Rec=Rectangle(12,6)

#avant la creation des setters et getters
print('La surface est: ',Rec.Perimetre()) #La surface est:  36
print('Le perimetre est: ',Rec.Surface())  #Le perimetre est:  72

Rec.set__longueur(25)
Rec.set__largeur(14)

print(Rec.get__longueur())
print(Rec.get__largeur())

#Apres la creation des setters et getters
print('La surface est: ',Rec.Perimetre())  #La surface est:  78
print('Le perimetre est: ',Rec.Surface()) #Le perimetre est:  350









































