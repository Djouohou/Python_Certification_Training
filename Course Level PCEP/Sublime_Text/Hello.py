
import os

"""
print("Hello  world!!!")
a=5
print(a)
b=12.5
print(b)
c="Bonjour"
print(c)
"""
"""
a=5
print("la valeur initial de a est:",a)
b=10
print("la valeur initial de b est:",b)
c=0
print("la valeur initial de c est:",c)
c=a
print("la valeur finale de c est:",c)
a=b
print("la valeur finale de a est:",a)
b=c
print("la valeur finale de b est:",b)

v1=int("10")
v2=float("10.5")
print(v1)
print(v2)

maliste=["bonjour","me","voici"]
print(maliste[0])
print(maliste[1])
print(maliste[2])
print(maliste)
maliste[0]="salut"
print(maliste)
maliste.append("ici")
print(maliste)

montuple=("1","2","3")
print(montuple)
print(montuple[0])
liste=list(montuple)
print(liste)
print(tuple(liste))

sophietuple=("bonjour")
liste=list(sophietuple)
print(liste)
print(tuple(liste))


dico={"je":"i","tu":"you","me":"moi"}
print(dico["me"])
print(dico["tu"])
print(dico["je"])
"""
"""
t = ("sandy", "mandy", "candy","andy")
print(sorted(t))



x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]

liste=[]
for i in x:
    if type(i)== list:
        liste.append(i)



x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

print(sum(x.keys()))< (x.get(1) + x.get(2) + x.get(3) + x.get(4) + x.get(5))
"""
import math





print(math.lcm())
print(math.lcm(0, 23))
print(math.lcm(44, 12))
print(math.lcm(-69, 23))
print(math.lcm(0, 0))

"""
if (max(x[0]) - x[2][1]) == (x[0][0]):
    print("True!")
    
elif (len(x[0]) - len(x[1])) == (x[2][0]):
    print("False!")

elif (sum([2])) % 2 == 0:
    print("Maybe!")

else:
    print("None!")


{ } 
sum(type(x)== list for x in lst)


from random import randint
p=0
b=0
c=0
yam=0

liste=[]
for i in range(5):
   r=randint(1,6)
   liste.append(r)
   print (r)
print(liste)

occ=[]
for i in liste:
    occ.append(liste.count(i))
print(occ)

mixt=zip(liste,occ)
print((mixt))

city = ["Amsterdam", "Berlin", "Chongqing"]
country = ["Netherlands", "Germany", "China"]

merged = []
for i in range(len(city)):
    merged.append((city[i], country[i]))
print(merged)

"""

"""
    if y == 2:
       print("paire")
       p+=1
    if y == 3:
       print("brelan")
       b+=1
    if y == 4:
       print("carré")
       c+=1
    if y == 5:
       print("yams")
       yam+=1
    

print("On a obtenu",p,"paires")
print("On a obtenu",b,"brelans")
print("On a obtenu",c,"carrés")
print("On a obtenu",yam,"yams")
"""

"""

z=0
for i in list:
    x=random.choice(list)
    y= list.count(x)
    del (list(x))
    print(x)
    if x==y:
        z+=1
        print(z)
        if y == 2:
           print("paire")
        if y == 3:
           print("brelan")
        if y == 4:
           print("carré")
        if y == 5:
           print("yams")
        else:
           print(y)
           
"""

"""
liste = [10, 20, 4, 45, 99,55,48,16]
#Trouver la plus petite valeur
def MinList(liste):
minimum = liste[0]
for x in liste:
if x < minimum :
minimum = x
return minimum
#Trouver la plus grande valeur
def MaxList(liste):
maximum = liste[0]
for x in liste:
if x > maximum :
maximum = x
return maximum
print("L'élément minimum est:", MinList(liste))
print("L'élément le plus grand est :", MaxList(liste))
"""






os.system("pause")
