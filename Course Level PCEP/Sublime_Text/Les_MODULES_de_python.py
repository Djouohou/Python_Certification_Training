#EXEMPLES D'UTILISATION DES MODULES DE BASE EN PYTHON

#Le module random
from random import randint

for i in range(5):
    a = randint(1,10)   #choisi une valeur aléatoire dans l'intervalle (1,10)
    b = randint(15,60)
    x = a*b
    print(x)

import random
print(random.choice([1,3,5,5]))
print(random.randint(5,50))

#Le module math
"""Calcul de la longueur d’un des côtés dans un triangle ABC rectangle en A, l’hypoténuse [BC] mesure x=6 cm, l’angle aBc a pour mesure y=40°.
Calculer la longueur du côté [AB]."""

import math
def triangle (cote1, angle):
    cote2 = cote1*(math.cos(angle))
    return cote2
cote1 = int(input('Entrer la valeur de x: '))
angle = int(input('Entrer la valeur de y: '))
print(triangle (cote1, angle))

#Le module sys
import sys

x = 20
if x < 100:
     sys.exit("Valeur non valide") #permet de sortir de l'excécution
else:
     print("Valeur valide!")

#Le module os
import os 
user = os.getlogin() 
print(user) # imprime le nom d'utilisateur

print(os.mkdir("c:/myFolder")) # crée un dossier nommé myFolder sur le disque C:\

rep_actuel = os.getcwd()
print(rep_actuel) # renvoie le répertoire actuel (l'emplacement du fichier actuel)

#Le module time
import time

print(time.ctime())  #La fonction ctime([secs]),sans paramètre retourne la date d’aujourd’hui au format texte.
print(time.ctime(10000)) #10000secondes (affiche la date de l’Epoch après que ce nombre de secondes se soit écoulé).


#Le module calendar
import calendar

annee = 2022
mois = 3    
print(calendar.month(annee, mois))  # Affiche le calendrier du mois de Mars en 2022. 

print ("le calendier de 2022 est : ")  
print (calendar.calendar(2022))


#Le module profile
import profile

def fonction():
    print("Madame le ministre")
profile.run(fonction())           #décrit comment et pendant combien de temps les differentes paties du programme sont executees

#Le module urllib2
"""urllib.request s'utilise pour l’ouverture et la lecture.
il permet de définir des fonctions et des classes pour ouvrir des URL (principalement HTTP). L’un des moyens les plus simples d’ouvrir de telles URL est:
urllib.request.urlopen (url)"""

import urllib.request

request_url = urllib.request.urlopen('https://docs.python.org/') 
print(request_url.read()) 

#Le module re
import re
chiffre = "1 4 8"
print(re.search("4", chiffre))

if re.search("4", chiffre):    # ici on utilise la fonction search du module re.
    print("trouvé")             #Elle permet de rechercher un motif, c'est-à-dire une regex, au sein d'une chaîne de caractères 














