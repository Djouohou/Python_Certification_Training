import os

print("EXERCICES SUR LES LISTES EN PYTHON")
print("EXERCICE 1: Definition liste")
print("-Une liste en python est une variable à l'interieur de laquelle on peut mettre plusieurs éléments ou variables.")
print("Elle peut contenir des éléments de types differents(entier,flottant,chaine de cacartère et aussi des listes etc...).")
laliste=[]
print("-Affichage d'une liste vide:",laliste)
print("EXERCICE 2: Ajouter des éléments dans une liste")
print("laliste=[]")
laliste.append("3")
laliste.append("a")
laliste.append("b")
laliste.append("5")
laliste.append("1")
print("La nouvelle liste est:",laliste)
print("EXERCICE 3: 'Reverse' en python")
print("-La fonction reverse() en python sert à inverser les éléments d'une liste")
print("Soit la liste suivante: ['Bonjour','madame','le','ministre']")
print("-En appliquant la fonction reverse() sur la liste ci-dessus, on obtient le resultat suivant:")
liste=["Bonjour","madame","le","ministre"]
liste.reverse()
print(liste)
print("EXERCICE 4: Donner les instructions erronées")
print("soit la variable liste= []")
blocliste=["a. liste[0]='a'","b. liste[1]=1","c. liste.append(elt)","d. liste.append('c')","e. liste.append(1)"]
for i in blocliste:
    print(i)
print("-Les instructions 'a' et 'b' sont érronées car elles permettent de modifier et non d'ajouter des éléments dans une liste or notre liste étant vide, l'excécution ne peut etre effectué.")
print("-L'instruction 'c' est érronée car il s'agit ici d'ajouter une chaine de caractère à la liste mais cette chaine de caractère n'est pas défini à cause de l'absence des doubles cotes, d'où l'ordinateur ne pourra pas le reconnaitre.")
print("Les instructions 'd' et 'e' sont correctes")
print("EXERCICE 5: Soit la liste suivante: [0,1,2,3,4,1,4,3,0,1]")
maliste=["0","1","2","3","4","1","4","3","0","1"]
a=(len(maliste))
print("-La taille de cette liste est:" ,a)
print("-Occurence des elements de la liste:")
b=maliste.count("0")
c=maliste.count("1")
d=maliste.count("2")
e=maliste.count("3")
f=maliste.count("4")
print("*Le nombre d'occurence de 0 est: ",b)
print("*Le nombre d'occurence de 1 est: ",c)
print("*Le nombre d'occurence de 2 est: ",d)
print("*Le nombre d'occurence de 3 est: ",e)
print("*Le nombre d'occurence de 4 est: ",f)
g=maliste.index("3")
print("-L'élement '3' dans la liste 'maliste' se trouve à la position: ",g)
print("-Trie de la liste par ordre croissant:")
h=sorted(maliste)
print("La nouvelle liste triée est: ",h)
print("-La difference entre la fonction sort() et la fonction sorted() est que:")
print("*sort() trie la liste et remplace la liste d'origine tandis que")
print("*sorted() renvoie une copie triée de la liste sans modifier la liste d'origine.")
print("EXERCICE 6: Affichage des éléments d'une liste")
uneliste=["a","Hello","1","2","3","4","T","10","20","Oui","Moi","Toi","Bonjour monsieur"]
print("Soit la liste suivante: ",uneliste)
print("-L'affichage de chaque élément de cette liste est:")
for i in uneliste:
    print(i)
print("EXERCICE 7: ")
theliste=[]
n=input("enter la valeur de n: ")
mot=int(n)
i=1
mot1=mot
while i<20:
    print(mot1)
    theliste.append(mot1)
    i=i+i
    mot1=mot**i
    print("i=",i)
print(theliste)

print("EXERCICE 8: Résultat de l'excecution des programmes")
print("-Le résultat du premier programme donne:")
liste1=["1","2","3","4"]
print("Affichage de la liste 1")
print(liste1)
liste2=["4","5","1","0"]
print("Affichage de la liste 2")
print(liste2)
liste1.extend(liste2)
print("Affiche de nouveau la liste 1")
print(liste1)
print("-Le résultat du second programme donne:")
liste1=["1","2","3","4"]
print("Affichage de la liste 1")
print(liste1)
liste2=["4","5","1","0"]
print("Affichage de la liste 2")
print(liste2)
print("Affichage de l'addition des deux listes")
print(liste1+liste2)
print("-Le résultat du dernier programme donne:")
liste1=["1","2","3","4"]
print("Affichage de la liste 1 multipliée par 5")
print(liste1 * 5)
print("EXERCICE 9: Sortie écran d'un script")
liste1=["1","2","3","4"]
print("Soit la liste: ",liste1)
print("Multiplication de la liste par 5:")
print(liste1*5)
print(liste1[0]*5)
print("Affichage des deux premiers éléments de la liste")
print(liste1[:2])
print("Affichage du dernier élément de la liste")
print(liste1[-1])
print("Affichage du troisième élément de la liste en partant de la fin")
print(liste1[-3])
print("Affichage des trois derniers éléments d'une liste")
print(liste1[-3:])



#AUTRES
lst=[[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")          #result ###



foo=(1,2,3)
foo.index(0)  #ValueError: tuple.index(x): x not in tuple
      


























os.system("pause")
