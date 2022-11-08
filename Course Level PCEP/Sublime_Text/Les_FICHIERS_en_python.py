
#ICI IL S'AGIT D'ECRIRE DANS UN FICHIER
#On peut utiliser l'option a ou l'option r

"""
fichier = open("monfichier.txt", "a")
fichier.write("\n Bonjour monde")
fichier.write("\n Bonjour à tous")
valeur=20
fichier.write("\n La valeur est de: "+str(valeur))

chiffre1 = input("\n veuillez entrer la première valeur: ")
chiffre2 = input("\n veuillez entrer la deuxieme valeur: ")

fichier.write("\n la premiere valeur est: "+str(chiffre1))
fichier.write("\n la deuxieme valeur est: "+str(chiffre2))

somme = int(chiffre1)+int(chiffre2)
print("\n La somme des deux valeurs est: ",somme)

fichier.write("\n Le résultat de la somme de ces deux chiffres est: "+str(somme))
fichier.close()



#MAINTENANT ON OUVRE UN FICHIER POUR LE LIRE
#On utilise l'option r
fichier = open("monfichier.txt", "r")
print(fichier.read())
fichier.close()
"""


#Il existe une autre syntaxe plus courte qui permet de s'emanciper du problème de fermeture du fichier: le mot clé with .

with open("monfichier.txt", "r") as fichier:
    print (fichier.read())

