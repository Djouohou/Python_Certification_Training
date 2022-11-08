
import os

import random
dico={ }
dico["Quel est la capitale de la France?"]="Paris"
dico["Quel est le plus haut sommet du monde?"]="Mont everest"
dico["Qui a remporté la troisième place à la dernière coupe d'Afrique?"]="Cameroun"
dico["Le corps humain à combien d'os?"]="208"
dico["Quel est la racine carrée de 9?"]="3"
dico["Quel est le nom du président actuel du Cameroun?"]="Paul biya"
dico["Comment appelle t-on le médecin qui s'occupe des enfants?"]="Pediatre"
dico["Quel est la pandémie qui frappe le monde depuis 2019?"]="Covid 19"
dico["Qui a reçu le premier prix Nobel de la paix en Afrique"]="Nelson mandela"
dico["Quel est long fleuve d’Afrique?"]="Nil"
dico["Combien d’État comptent le continent africain?"]="54"
dico["Où se trouve la maison des esclaves au Sénégal"]="Sur l’ile de Gorée a Dakar"
points=0
nqp=0
#nqp=nombre de questions posées
for i in range(len(dico)):
    a=random.choice(list(dico.keys()))
    print(a)
    nqp=nqp+1
    mot1=input("votre reponse:")
    print(mot1)
    if mot1 == dico[a]:
        print (True)
        points=points+1
    else:
        print(False)
    del dico[a]
    mot2=input("Voulez vous continuer avec les questions? taper 'o' pour oui et 'n' pour non: ")
    while((mot2!="o") and (mot2!="n")):
        print("choix non déterminé")
        mot2=input("Taper 'o' pour oui et 'n' pour non: ")
    if dico=={ }:
        break
    elif mot2=="o":
        continue
    else:
        mot2=="n"
        break
print("vous avez obtenu ",points,"sur",nqp,"points")    
print("Merci et à bientòt pour un nouveau quiz.")




#Othee example
"""
We've prepared a simple example, showing how tuples and dictionaries can work together.

Let's imagine the following problem:

    you need a program to evaluate the students' average scores;
    the program should ask for the student's name, followed by her/his single score;
    the names may be entered in any order;
    entering an empty name finishes the inputting of the data (note 1: entering an empty score will raise the ValueError exception,
but don't worry about that now, you'll see how to handle such cases when we talk about exceptions in the second part of the Python Essentials course series)
    a list of all names, together with the evaluated average score, should be then emitted.

Look at the code in the editor. This how to do it.

Now, let's analyze it line by line:

    line 1: create an empty dictionary for the input data; the student's name is used as a key,
    while all the associated scores are stored in a tuple (the tuple may be a dictionary value - that's not a problem at all)
    line 3: enter an "infinite" loop (don't worry, it'll break at the right moment)
    line 4: read the student's name here;
    line 5-6: if the name is an empty string (), leave the loop;
    line 8: ask for one of the student's scores (an integer from the range 0-10)
    line 9-10: if the score entered is not within the range from 0 to 10, leave the loop;
    line 12-13: if the student's name is already in the dictionary, lengthen the associated tuple with the new score (note the += operator)
    line 14-15: if this is a new student (unknown to the dictionary), create a new entry - its value is a one-element tuple containing the entered score;
    line 17: iterate through the sorted students' names;
    line 18-19: initialize the data needed to evaluate the average (sum and counter)
    line 20-22: we iterate through the tuple, taking all the subsequent scores and updating the sum, together with the counter;
    line 23: evaluate and print the student's name and average score.
"""
#AUTRES

school_class = {}

while True:
    name = input("Enter the student's name: ")
    if name == '':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
	    break
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)






#new
dico={}
dico['1']=(1,2)
dico['2']=(2,1)

for x in dico.keys():
    print(dico[x][1],end="")     #result 21

















os.system("pause")
