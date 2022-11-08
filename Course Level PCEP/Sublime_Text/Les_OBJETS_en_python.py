#SOURCES: https://python.doctor/page-apprendre-programmation-orientee-objet-poo-classes-python-cours-debutants


class Voiture:
    def __init__(self, nbreR):            #dans ce cas, on stock le nom dans l'attribut nom .
                                               #self.nom est une manière de stocker une information dans la classe
        self.nom = "Ferrari"
        self.couleur = "rouge"
        self.nbreRoues = nbreR
	
    def modifierNom(self, nom):
        self.nom = nom

ma_voiture = Voiture(4)
print(ma_voiture.nom)

ma_voiture.modifierNom("Toyota")
print("nom: ",ma_voiture.nom ,"nombre de roues: ",ma_voiture.nbreRoues)

ma_voiture.modele = "250"
print(ma_voiture.modele)

 #les methodes
class Voiture:
        def __init__(self):
                self.nom = "Ferrari"

	def donne_moi_le_modele(self):
		return "250"

ma_voiture=Voiture()
print(ma_voiture.donne_moi_le_modele())


# les proprietes

class Voiture(object):

    def __init__(self):
        self._roues=4

    def _get_roues(self):
        print("Récupération du nombre de roues")
        return self._roues

    def _set_roues(self, v):
        print("Changement du nombre de roues")
        self._roues  =  v

    roues=property(_get_roues, _set_roues)


ma_voiture=Voiture()
ma_voiture.roues=5                  #Changement du nombre de roues
print(ma_voiture.roues)          #Récupération du nombre de roues

#Il existe une autre syntaxe en passant par des décorateurs ,le résultat est le meme mais la lecture du code est amélioré
class Voiture(object):

    def __init__(self):
        self._roues=4

    @property
    def roues(self):
        print("Récupération du nombre de roues")
        return self._roues

    @roues.setter
    def roues(self, v):
        print("Changement du nombre de roues")
        self._roues  =  v

#La fonction dir vous donne un aperçu des méthodes de l'objet
print(dir(ma_voiture))

#L'attribut spécial __dict__ donne les valeurs des attributs de l'instance
print(ma_voiture.__dict__)


#HERITAGE DE CLASSE
"""L'héritage est un concept très utile. Cela permet de créer de nouvelles classes mais avec une base existante.
Gardons l'exemple de la voiture et créons une classe VoitureSport"""

class Voiture:

	roues = 4
	moteur = 1

	def __init__(self):
		self.nom = "A déterminer"

class VoitureSport(Voiture):

	def __init__(self):
		self.nom = "Ferrari"

#On peut toujours instancier la classe Voiture si on le désire:

ma_voiture=Voiture()
print(ma_voiture.nom)
print(ma_voiture.roues)

#Instancions maintenant la classe VoitureSport

ma_voiture_sport=VoitureSport()
print(ma_voiture_sport.nom)
print(ma_voiture_sport.roues)

 

# POLYMORPHISME/SURCHARGE DE METHODE

class Voiture:

    roues = 4
    moteur = 1

    def __init__(self):
        self.nom = "A déterminer"
        
    def allumer(self):
        print("La voiture démarre")

class VoitureSport(Voiture):

    def __init__(self):
        self.nom = "Ferrari"

ma_voiture_sport = VoitureSport()
print(ma_voiture_sport.allumer())

#Il est cependant possible d' écraser la méthode de la classe parente en la redéfinissant. On parle alors de surcharger une méthode .

class Voiture:

    roues = 4
    moteur = 1

    def __init__(self):
        self.nom = "A déterminer"
        
    def allumer(self):
        print("La voiture démarre")

class VoitureSport(Voiture):

    def __init__(self):
        self.nom = "Ferrari"
        
    def allumer(self):
        print("La voiture de sport démarre")

ma_voiture_sport = VoitureSport()
print(ma_voiture_sport.allumer())

#Enfin dernier point intéressant: il est possible d'appeler la méthode du parent puis de faire la spécificité de la méthode.
class Voiture:

    roues = 4
    moteur = 1

    def __init__(self):
        self.nom = "A déterminer"
        
    def allumer(self):
        print("La voiture démarre")

class VoitureSport(Voiture):

    def __init__(self):
        self.nom = "Ferrari"
        
    def allumer(self):
        Voiture.allumer(self)
        print("La voiture de sport démarre")

ma_voiture_sport = VoitureSport()
print(ma_voiture_sport.allumer())



#COURS EXPLICATIF AVEC LE PROF

class Voiture:
    def __init__(self, nbreR):          
                                               
        self.nom = "Ferrari"
        self.couleur = "rouge"
        self.nbreRoues = nbreR
	
    def modifierNom(self, nom):
        self.nom = nom
        
    def _get_nom(self):
        print("Récupération du nombre de nom")
        return self.nom

    def _set_nom(self, v):
        print("Changement du nombre de nom")
        self.nom  =  v

    name = property(_get_nom, _set_nom)

    def _get_couleur(self):
        print("Récupération du nombre de couleur")
        return self.couleur

    def _set_couleur(self, c):
        print("Changement du nombre de couleur")
        self.couleur  =  c

    color = property(_get_couleur, _set_couleur)

    @property
    def _nom(self):
        print("Récupération du nombre de nom")
        return self.nom
    
    @_nom.setter
    def _nom(self, v):
        print("Changement du nombre de nom")
        self.nom  =  v


ma_voiture = Voiture(4)
print(dir(ma_voiture))


print(ma_voiture.nom)

ma_voiture.modifierNom("Toyota")
print("nom: ",ma_voiture.nom ,"nombre de roues: ",ma_voiture.nbreRoues)


print(ma_voiture._get_nom(),"nombre de roues: ",ma_voiture.nbreRoues)

ma_voiture.modifierNom("Toyota")
print("nom: ",ma_voiture._get_nom() ,"nombre de roues: ",ma_voiture.nbreRoues)

ma_voiture._set_nom("BMW")
print("nom: ",ma_voiture._get_nom() ,"nombre de roues: ",ma_voiture.nbreRoues)


#print(ma_voiture.nom)
#print(ma_voiture.name)
 
ma_voiture.nom=("pagerot")
ma_voiture.name=("pagerot")

print(ma_voiture.name)


ma_voiture.couleur=("jaune")
ma_voiture.color=("jaune")
print(ma_voiture.color)


#HERITAGE DE CLASSE EXPLICATION

class Voiture:
    moteur=10
    def __init__(self, nbreR):          
                                               
        self.nom = "Ferrari"
        self.couleur = "rouge"
        self.nbreRoues = nbreR
	
    def modifierNom(self, nom):
        self.nom = nom

    @property
    def _nom(self):
        print("Récupération du nom")
        return self.nom
    
    @_nom.setter
    def _nom(self, v):
        print("Changement du nom")
        self.nom  =  v
    def allumer(self):
        print("la voiture demarre")
        
    

class VoitureSport(Voiture):

    def __init__(self):
        self.nom="Toyota"

    def allumer(self):
        Voiture.allumer(self)
        print("la voiture de sport demarre")
        
        
voiture_sport=VoitureSport()
print(voiture_sport.nom)
print(voiture_sport.moteur)
















