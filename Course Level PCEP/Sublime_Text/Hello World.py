import os

"""
print("Hello sophie")
a=5
b="bonjour"
c=12,5
print("Initialement on a:")
print("a=",a,"b=",b,"c=",c)
a=10
b=c
c=a
print("A la fin on a:")
print("a=",a,"b=",b,"c=",c)
"""
"""
a=5
b=10
c=0
print("Initialement on a:")
print("a=",a,"b=",b,"c=",c)
c=a
a=b
b=c
print("A la fin on a:")
print("a=",a,"b=",b,"c=",c)
"""
"""
a=44.5
b=int(a)
print("b=",b)
a="44.5"
b=float(a)
print("b=",b)
a=44
b=float(a)
print("b=",b)
a=44
b=str(a)
print("b=",b)
a="44"
b=int(a)
print("b=",b)
a=10
b=5
c=a+b
print("c=",c)
a=10
b=5
c=str(a)+str(b)
print("c=",c)
a="10"
b="5"
c=a-b
print("c=",c)
"""
"""
a=1+2*3
print("a=",a)
a=(1+2)*3
print("a=",a)
a=4
a*=3
print("a=",a)
a=5>3
print("a=",a)
a=(3>5)and(2<5)
print("a=",a)
a=(3>5)or(2<5)
print("a=",a)
a=10
b=5
c=str(a)+str(b)
print("c=",c)
a="10"
print("a=",4*a)
"""
"""
if 2==2:
    print("true")
if 2==0:
    print("true")
else:
    print("false")
if 2==0:
    print("true")
elif 2>1:
    print("false")
else:
    print("non déterminé")
"""
"""
list=["a","a","a","b","c","c",]
print(list.index("b"))
list=["a","d","m"]
for letter in list:
    print(letter)
for letter in enumerate(list):
    print(letter)
"""
"""
list=["a","b","c"]
print(list)
b=tuple(list)
print(b)
print("affiche")
print(list[0])
print(list[1])
print(list[2])
print("fin")

list=["13","b","c"]
a=list[0]
print(a)
b=list(a)
print(b)
print(tuple(b))

maliste=["hey","toi"]
for i in maliste:
    print([i])

maliste=["hey","toi"]
i=0
while i<2:
    print(maliste[i])
    i=i+1

a=345.56
b=int(a)
liste=(str(b))
print(liste)
print(tuple(liste))

dico={"1":"234"}
a=dico["1"]
print(a)
b=list(a)
print(b)
print(tuple(b))

i=0
while i<15:
    print("je veux manger la banane")
    i=i+1

v="bonjour toi"
for letter in v:
    print(letter)

maliste=[1,5,10,15,20,25,30]
for i in maliste:
    if i>20:
        print("la boucle s'arrete")
    if i>=26:
        print("on stoppe la boucle")
        break
    print(i)

maliste=["1","a","ciao"]
for letter in enumerate(maliste):
    print(letter)

x=["1","2","3"]
y=x[:]
print(y)

a=dict ()
a["nom"]="djouohou"
a["prenom"]="ingrid"
print(a)

laliste=[]
laliste.append(3)
laliste.append("a")
laliste.append("b")
laliste.append(5)
laliste.append(1)
print(laliste)

laliste1=["0","1","2","3","4","1","4","3","0","1"]
print(laliste1)
laliste1.reverse()
print(laliste1)
print(len(laliste1))
print(laliste1.count("2"))
print(laliste1.index("4"))
print(sorted(laliste1))
laliste1.sort(reverse =True)
print(laliste1)
laliste1.sort(reverse =False)
print(laliste1)
print(laliste1.index("4"))

laliste=[]
i=0
while i <5:
    laliste.append(2**i)
    i=i+1
print(laliste)

laliste=[]
n=input("enter la valeur de n:")
val=int(n)
i=1
val1=val
while i<18:
    print(val1)
    laliste.append(val1)
    i+=i
    val1=val**i
    print("i=",i)
print(laliste)

chiffre=[1,2,3,4,5]
for i in range(5):
    print (chiffre[i])

i = 0
while i < 10:
    reponse = input("Entrez un entier supérieur à 10 : ")
    i = int(reponse)
print(i)


import random
dico={ }
dico["Quel est la capitale de la France?"]="Paris"
dico["Quel est le plus haut sommet du monde?"]="Mt.Everest"
dico["Qui a remporté la troisième place à la dernière coupe d'Afrique?"]="Cameroun"
dico["Le corps humain à combien d'os?"]="208 os"
dico["Quel est la racine carrée de 9?"]="3"
dico["Quel est le nom du président actuel du Cameroun?"]="Paul Biya"
dico["Comment appelle t-on le médecin qui s'occupe des enfants?"]="Le pédiatre"
dico["Quel est la pandémie qui frappe le monde depuis 2019?"]="COVID 19"
dico["Qui a reçu le premier prix Nobel de la paix en Afrique"]="Nelson Mandela"
dico["Quel est long fleuve d’Afrique?"]="Le Nil"
dico["Combien d’État comptent le continent africain?"]="54 États"
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
"""
print(17%3, print(14%3.5))


os.system("pause")
