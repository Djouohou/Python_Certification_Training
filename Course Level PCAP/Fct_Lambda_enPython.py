#LES FONCTIONS MAP(), FILTER() ET ZIP() EN PYTHON
Python fournit les fonctions map(), filter() et zip() qui permettent d’avoir un code plus efficace dans le traitement des données. En fait, ces fonctions peuvent
vous faire gagner beaucoup de temps lorsque vous travaillez avec des itérables.
L’idée est de prendre une petite fonction que vous écrivez et de l’appliquer à tous les éléments d’une séquence, ce qui vous évitera d’écrire une boucle.


x=lambda a,b : a + b
print(x(5, 6))

def somme(a,b):
    return a+b

print(somme(5,6))  #-11


x=lambda x,y,z : 2*x-3*y+z
print(x(5, 6, 4))   #-4

print((lambda x : x*x*x)(10))   #1000



a = [5, 9, 2, 4, 7]
b = [3, 7, 1, 9, 2]
c = [6, 8, 0, 5, 3]
maxs =map(lambda n: max(*n), zip(a, b, c))
print(list(maxs))


zip(a, b, c)==[(5, 3, 6), (9, 7, 8), (2, 1, 0), (4, 9, 5), (7, 2, 3)]

#ecrivez une fonction qui prend une liste en paramètres et multiplie tous les éléments de cette liste par deux et retourne le résultat.
def function (*liste):
    val=0
    elem=[]
    for i in liste:
        val=i**2
        elem.append(val)
    return elem

print(function(2,3,4,5,6,7,8))

#en utilisant map et lambda ecrivez une fonction qui prend une liste en paramètres et multiplie tous les éléments de cette liste par deux et retourne le résultat.
liste=[2,3,4,5,6]
x=map(lambda i:i**2, liste)
print(list(x))


#écrivez une fonction qui filtre une liste et retourne tous les nombres impairs de la liste.
liste=[2,3,4,5,6,7,8,9,10]
x=filter(lambda i: i%2!=0, liste)
print(list(x))


#LA FONCTION MAP()
La fonction map () de Python applique une fonction sur tous les éléments d’une séquence itérable et renvoie un objet map.
La fonction map() prend deux arguments positionnels, la fonction à exécuter sur l’itérable et l’itérable lui même (par exemple: une liste).
Le résultat sera un objet map avec un emplacement en mémoire.

Par exemple, multiplions les nombres d’une liste par 2 de manière basique et stockons le résultat dans une nouvelle liste.
nombres = [2,3,4,5,6]
produit = [] 
for i in nombres: 
    produit.append(i * 2) 
print (produit)               #[4, 6, 8, 10, 12]

La fonction map() nous permet d’avoir le même résultat d’une manière beaucoup plus simple et élégante.
nombres = [2,3,4,5,6]
produit = list(map(lambda x: x * 2, nombres))
print (produit)

Vous avez certainement remarqué que nous avons utilisé la fonction lambda, qui est très pratique dans ces situations. On utilise souvent lambda avec les
fonctions map, filter et zip . Lambda est une fonction qui peut utiliser n’importe quelle nombre de paramètres, mais qui n’utilise qu’une seule expression.


#LA FONCTION FILTER()
La fonction filter() crée une liste d’éléments pour lesquels la fonction renvoie True. Elle nécessite une fonction et une séquence (itérable) comme paramètres.

Supposons que nous voulions récupérer les nombres pairs à partir d’une liste et les mettre dans une nouvelle liste.
nombres = [1,2,3,4,5,6,7,8,9,10,11,12]
nouvelle_list = []
for i in nombres:
    if i % 2 == 0:
        nouvelle_list.append(i)
print(nouvelle_list)             #[2, 4, 6, 8, 10, 12]

En fait, nous pouvons utiliser la fonction filter() et avoir le même résultat avec un code plus performant.
nombres = [1,2,3,4,5,6,7,8,9,10,12]
nouvelle_list = list (filter (lambda x: (x % 2==0), nombres))
print(nouvelle_list)

Mais, quel est la différence entre map() et filter() ?

Prenons à nouveau le même exemple de nombres pairs en utilisant map().

nombres = [1,2,3,4,5,6,7,8,9,10,12]
nouvelle_list = list (map (lambda x: (x % 2==0), nombres))
print(nouvelle_list)

L’exécution du code nous donne :  [False, True, False, True, False, True, False, True, False, True, True]  Qui est une liste de booléens.

#Donc, la fonction filter() renvoie la valeur des éléments évalués à True, tandis que map() renvoie tous les éléments de la liste renvoyés par la fonction.

#Vous allez vous demandé pourquoi on a enveloppé map() et filter() dans la fonction list() ?
Exécutez ce code :
nouvelle_list = map (lambda x: (x % 2==0), nombres)
print(nouvelle_list)       #<map object at 0x7fe3df7bcac0>
print(type(nouvelle_list))#<class 'map'> renvoie un objet donc on est obligé de convertir en list avant de l'utliser.


#LA FONCTION ZIP()

La fonction zip() en Python combine les éléments de 2 listes selon les index correspondants en une liste de tuples intérable.

lettres = ['a', 'b', 'c', 'd', 'e']
nombres = [1,2,3,4,5]
resultat = list(zip(lettres, nombres))
print(resultat)

L’exécution de ce code nous donne une liste de tuples des éléments des deux listes.

Un exemple simple de l’utilisation combinée de map() et zip() et de trouver l’élément le plus grand en parcourant plusieurs séquences, c’est-à-dire le plus
grand du premier élément de chaque séquence, puis du second, et ainsi de suite.

a = [5, 9, 2, 4, 7]
b = [3, 7, 1, 9, 2]
c = [6, 8, 0, 5, 3]
maxs = map(lambda n: max(*n), zip(a, b, c))
print(list(maxs))            #[6, 9, 2, 9, 7]






































