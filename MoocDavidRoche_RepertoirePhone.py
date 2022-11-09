#Le fichier texte a ete cree dans le blocnote de windows puis maintenant il faut l'ouvir en mode Lecture ou Read.
"""
fichier = open("fichier_Mooc_DavidRoche.txt", "r")
print (fichier.read())
"""

#Maintenant ouvrons le fichier en mode Ecriture ou Write. Ici a chaque ouverture,le contenu du fichier est ecrasé.
"""
fichier1 = open("fichier_Mooc_DavidRoche.txt", "w")

fichier1.write("\n formation mooc")

fichier1.close()
"""

#Maintenant ouvrons le fichier en mode Ajout ou Append. l'ajout se fait à la fin du fichier.
#pour append et write , si le fichier txt n'existe pas python le cree au meme emplacement que le fichier py.
"""
fichier1 = open("fichier_Mooc_DavidRoche.txt", "w")

fichier1.write("\n formation mooc ")
fichier1.write(" de david roche")

fichier1.close()
"""

#PROJET REPERTOIRE TELEPHONIQUE
"""
En utilisant les connaissances acquises jusqu'à présent, vous allez écrire un programme de gestion de répertoire téléphonique.

Cahier des charges

Ce programme devra proposer le menu suivant à l'utilisateur :

0-quitter
1-écrire dans le répertoire
2-rechercher dans le répertoire
Votre choix ?

Si le choix est 0 : Le programme sera stoppé.

Si le choix est 1 :

L'utilisateur devra saisir un nom ou 0 s'il veut terminer la saisie (" Nom (0 pour terminer) : ") :

    L'utilisateur entre 0 => le programme devra le renvoyer vers le menu
    L'utilisateur entre un nom => le programme devra lui demander de saisir le numéro de téléphone correspondant au nom. Une fois le numéro saisi, le programme devra lui proposer d'entrer un nouveau nom (ou 0 pour terminer)...
Si le choix est 2 :

L'utilisateur devra saisir le nom recherché (" Entrer un nom : ").

    Si le nom recherché est présent dans le répertoire, le programme devra afficher " Le numéro recherché est : " suivi du numéro de téléphone correspondant au nom saisi.
    Si le nom recherché est absent du répertoire, le programme devra afficher " Inconnu ".

L'utilisateur est ensuite redirigé vers le menu principal.

Les noms et numéros de téléphone devront être stockés dans un fichier texte.

Votre programme devra être composé au minimum de 3 fonctions : une fonction " menu ", une fonction " lecture " et une fonction " ecriture ".
"""




















#Projet Création de QCM
"""
Vous allez écrire un programme permettant de générer un QCM (l'ordinateur pose une question, l'utilisateur doit apporter une réponse parmi plusieurs possibilités).

Cahier des charges 

L'utilisateur doit pouvoir choisir parmi au moins 2 thèmes (par exemple "science", "histoire") à l'aide d'un menu principal.

Les questions et les réponses devront se trouver dans un (ou des) fichier(s) texte(s).

Voici une capture d'écran pour une question d'histoire.

    Si l'utilisateur fait un autre choix que 1,2 ou 3, il faudra afficher : Désolé, vous faites erreur, quel est votre choix ?

    Si la réponse est correcte, on affichera : Bravo, c'est une bonne réponse.

    Si la réponse n'est pas correcte : Désolé, c'est une mauvaise réponse. Il fallait choisir la réponse 3.

Après 5 questions (et réponses) le programme devra proposer une note à l'utilisateur : Votre note : 4 / 5

Une fois la note affichée, nous aurons un retour au menu principal.
"""
















