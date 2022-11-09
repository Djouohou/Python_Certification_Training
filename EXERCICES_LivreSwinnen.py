#EXERCICES_SWINNEN

#Exercices CHAPITRE 2:

2.1 Décrivez le plus clairement et le plus complètement possible ce qui se passe a chacune des trois lignes de l'exemple ci-dessous :
>>> largeur = 20       #On déclare ue variable nommée 'largeur' à laquelle on affecte la valeur 20.
>>> hauteur = 5 * 9.3   #On déclare ue variable nommée 'largeur' à laquelle on assigne le produit des deux valeurs 5 et 9.3.
>>> largeur * hauteur   #Cette ligne fait la multiplication des deux variables dèclarées donc largeur et hauteur.

2.2 Assignez les valeurs respectives 3, 5, 7 a trois variables a, b, c.
Effectuez l’opération a - b//c. Interprétez le résultat obtenu.

a = 3
b = 5
c = 7
print(a - b//c) #result is 3 car la division est prioritaire sur la soustraction. Or la div entiere entre b et c est zéro, le resultat final sera donc a-0 qui font 3.

2.3 Testez les lignes d’instructions suivantes. Décrivez dans votre cahier ce qui se passe :
>>> r, pi = 12, 3.14159  #affectation de 12 et 3.14159 aux variables r et pi respectivement.
>>> s = pi * r**2    #declaration de la variable s qui prend pour assignation le produit entre pi et r carrée
>>> print(s)         #affichage de la valeur de s qui vaut: 452.38896
>>> print(type(r), type(pi), type(s))    #Affichage du type de r, pi et s qui sont: <class 'int'> <class 'float'> <class 'float'>
Quelle est, à votre avis, l’utilité de la fonction type() ?  #permet de dire sous quel type une donnée est enregistré dans la mémoire Python.


#Exercices CHAPITRE 4:

4.2 Ecrivez un programme qui affiche les 20 premiers termes de la table de multiplication par 7.
a=7
for i in range(20):
    print (str(a)+' * '+str(i)+' = '+str(i*a))

4.3 Ecrivez un programme qui affiche une table de conversion de sommes d’argent exprimées en euros, en dollars canadiens. La progression des sommes de la table
sera ≪ géométrique≫, comme dans l’exemple ci-dessous :
1 euro(s) = 1.65 dollar(s)
2 euro(s) = 3.30 dollar(s)
4 euro(s) = 6.60 dollar(s)
8 euro(s) = 13.20 dollar(s)
etc. (S’arrêter à 16384 euros.)

dollar=1.65
euro=1
while euro <= 16384 :
    print(str(euro)+' euro(s)'+' = '+str('%.2f' %(euro*dollar))+' dollar(s)')
    euro+=euro


print('%.2f' %(euro*dollar))      #54067.20
print('%.5f' % round((euro*dollar)))      #54067.00000

4.4 Ecrivez un programme qui affiche une suite de 12 nombres dont chaque terme soit égal au triple du terme précèdent.
u=5
n=12
for i in range(n):
    print(u)
    u*=3


4.5 Ecrivez un programme qui calcule le volume d’un parallélépipède rectangle dont sont fournis au départ la largeur, la hauteur et la profondeur.
l=int(input('entrer la largeur: '))
h=int(input('entrer la hauteur: '))
p=int(input('entrer la profondeur: '))
    
volume=l*h*p
print('le volume du parallélépipède est: ',volume)


4.6 Ecrivez un programme qui convertit un nombre entier de secondes fourni au départ en un nombre d’années, de mois, de jours, de minutes et de
secondes (utilisez l’opérateur modulo : %).
#conversion en annees
nbre=int(input('entrer les secondes à convertir: '))
val=31540000 #1an=3.154*10**7 secondes

annee = nbre // val
print(str(nbre)+' seconde(s) = '+str(annee)+' année(s)')

#conversion en mois
nbre1=nbre%val
val1=2628000 #1mois= 2628000 secondes

mois = nbre1 // val1
print(str(nbre1)+' seconde(s) = '+str(mois)+' mois')

#conversion en jours
nbre2=nbre1%val1
val2=86400 #1jour=86400 secondes

jour = nbre2 // val2
print(str(nbre2)+' seconde(s) = '+str(jour)+' jour(s)')

#conversion en minutes
nbre3=nbre2%val2
val3=60 #1minute=60 secondes

minute = nbre3 // val3
print(str(nbre3)+' seconde(s) = '+str(minute)+' minute(s)')

#conversion en secondes
seconde=nbre3%val3

print("donc, {} secondes font {} années,{} mois,{} jours,{} minutes et {} secondes\n" .format(nbre, annee, mois, jour, minute, seconde))
print(str(nbre)+' seconde(s) = '+str(annee)+' année(s) = '+str(mois)+' mois = '+str(jour)+' jour(s) = '+str(minute)+' minute(s) = '+str(seconde)+' seconde(s)')


4.7 Ecrivez un programme qui affiche les 20 premiers termes de la table de multiplication par 7, en signalant au passage
(à l’aide d’une astérisque) ceux qui sont des multiples de 3.
Exemple : 7 14 21 * 28 35 42 * 49 ...
s=0
n=20
for i in range(1,n+1):
    s=i*7
    if s%3==0:
        print(s,'*',end=' ')
    else:
        print(s,end=' ')


4.8 Ecrivez un programme qui calcule les 50 premiers termes de la table de multiplication par 13, mais n’affiche que ceux qui sont des multiples de 7.
s=0
for i in range(50):
    s=i*13
    if s%7==0:
        print(s,end=' ')
    else:
        continue


4.9 Ecrivez un programme qui affiche la suite de symboles suivante :
* 
**
***
****
*****
******
*******

n=7
for i in range(n):
    for j in range(i+1):
        print('*',end='')
   print() 


#Exercices CHAPITRE 5:

5.1 Ecrivez un programme qui convertisse en radians un angle fourni au départ en degrés, minutes, secondes.







5.2 Ecrivez un programme qui convertisse en degrés, minutes, secondes un angle fourni au départ en radians.

angle=float(input("entrer la valeur de l'angle: "))

degree = int(angle)
conv = 60 * (angle - degree)
minute = int(conv)
seconde = 60 * (conv - minute)

print('en DMS on a : ', degree,'°', minute,'\'', seconde,'"')    












dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)


re.split('[°\'"]+', """78°55'44.29458"N""")

s="78°55'44.29458"

print(s.split('°\''))



5.3 Ecrivez un programme qui convertisse en degrés Celsius une température exprimée au départ en degrés Fahrenheit, ou l’inverse.
La formule de conversion est : T F=TC ×1,8+32.

fahr=float(input('entrer la temperature en degres fahrenheit: '))
#TF=TC*1.8+32 ==> TC=(TF-32)/1.8
celsius=(fahr-32)/1.8
print('En degre celsius on a: ',celsius)


5.4 Ecrivez un programme qui calcule les intérêts accumules chaque année pendant 20 ans, par capitalisation d’une somme de 100 euros placée
en banque au taux fixe de 4,3 %.

somme=100
interet=0
somme1=0
depart=somme
for i in range (20):
    interet=somme*(4.3/100)
    somme1=somme+interet
    somme=somme1
    
print(somme)
interetcumule = somme-depart
print(interetcumule)



5.5 Une légende de l’Inde ancienne raconte que le jeu d’échecs a été inventé par un vieux sage, que son roi voulut remercier en lui affirmant qu’il
lui accorderait n’importe quel cadeau en récompense. Le vieux sage demanda qu’on lui fournisse simplement un peu de riz pour ses vieux jours, et plus
précisément un nombre de grains de riz suffisant pour que l’on puisse en déposer 1 seul sur la première case du jeu qu’il venait d’inventer, deux sur la suivante,
quatre sur la troisième, et ainsi de suite jusqu’à la 64e case.

Ecrivez un programme Python qui affiche le nombre de grains à déposer sur chacune des 64 cases du jeu. Calculez ce nombre de deux manières :
• le nombre exact de grains (nombre entier) ;
• le nombre de grains en notation scientifique (nombre réel).







































