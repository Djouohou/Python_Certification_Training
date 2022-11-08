import os

import random
dico={ }
dico["Quel est la capitale de la France?"]="Paris"
dico["Quel est le plus haut sommet du monde?"]="Mt.Everest"
dico["Qui a remporté la troisieme place à la dernière coupe d'Afrique?"]="Cameroun"
dico["Le corps humain à combien d'os?"]="208 os"
dico["Quel est la racine carrée de 9?"]="3"
dico["Quel est le nom du president actuel du Cameroun?"]="Paul Biya"
dico["Qui à inventé l'ampule électrique?"]="Thomas Edisson"
dico["Comment appelle t-on le medecin qui s'occupe des enfants?"]="Le pédiatre"
dico["Quel est la pandemie qui a frappé le monde depuis 2019?"]="COVID 19"
dico["Qui a recu le premier prix nobel de la paix en Afrique"]="Nelson Mandela"
dico["Quel est long fleuve d'afrique?"]="Le Nil"
dico["Combien d'Etat comptent le continent africain?"]="54 Etats"
dico["Où se trouve la maison des esclaves au Sénégal"]="Sur l'ìle de Gorée a Dakar"
points=0
nqp=0
for i in range(len(dico)):
    cleliste=random.sample(dico.keys(),1)
    cle=cleliste[0]
    print(cle)
    nqp+=1
    valeur=input("entrez la reponse")
    print(valeur)
    if valeur==dico[cle]:
        points=points+1
        print("bonne reponse")
    else:
        print("mauvaise reponse")
    del dico[cle]
    question="voulez vous continuez?"
    print(question)
    if dico=={}:
        break
    reponse=input("tapez 'o' pour oui et 'n' pour non:")
    if reponse=="o":
        continue
    else:
        break
print("ton score est:",points,"sur",nqp)
os.system("pause")
