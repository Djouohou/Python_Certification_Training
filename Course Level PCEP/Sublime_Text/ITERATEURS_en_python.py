

#LES ITERATEURS
#Une liste est un itérateur:

chaine = ['hello world']
for letter in chaine:
    print(letter)

chaine = 'hello world'
iterateur=iter(chaine)
print(type(iterateur))
print(list(iterateur))

#Créons notre propre classe iterateur:

class MonIter():
    
    current=0

    def __init__(self,stop):
        self.stop=stop

    def __iter__(self) :
        return self

    def next(self) :
        self.current+= 1
        
        if self.current>self.stop:
            raise StopIteration

        if self.current == 5:
            print("Quoi déjà 5eme tour?")

        return self.current

#Nous pouvons maintenant boucler sur cet élément:

m=MonIter(10)
for i in range(9):
    print(m.next())




#AUTRE EXEMPLE


class MonIterateur(object):
    def __init__(self, obj):
        self.obj = obj
        self.length = len(obj)
        self.count = 0

    def __iter__(self):
        return self

    def next(self):
        if self.count > self.length:
            raise StopIteration

        else:
            result = self.obj[self.count]

        self.count += 2
        return result

if __name__ == "__main__":
    chaine = "hello_world"
    ma_classe_iterateur = MonIterateur(chaine)
    iterateur = ma_classe_iterateur. __iter__ ()
    try:
        for idx in range(len(chaine)):
            print(iterateur.next())
    except StopIteration:
        print("fin d'iteration")
        
# en simplifiant la fin du code
"""if __name__ == "__main__":
    chaine = "hello_world"
    ma_classe_iterateur = MonIterateur(chaine)
    try:
        for lettre in ma_classe_iterateur:
            print(lettre)
    except StopIteration:
        print("fin d'iteration")"""


# LES GENERATEURS
"""Le mot clé « yield » est à la base des générateurs. C'est grâce à lui qu'un générateur peut fonctionner.

Il peut être assimilé à un « return », à deux principales différences près.
Alors qu'un return vous renverra un ensemble de valeurs (sous forme de liste, chaine de caractères…) et mettra fin à l'exécution de la procédure/fonction/...,
un yield vous retournera une valeur, puis se mettra en pause, en attendant l'appel suivant.
"""
"""
def mon_generateur():
    yield 'h'
    yield 'e'
    yield 'l'
    yield 'l'
    yield 'o'
    yield ' '
    yield 'w'
    yield 'o'
    yield 'r'
    yield 'l'
    yield 'd'

generateur = mon_generateur()
for value in generateur:
    print(value)

#OU simplement

def mon_generateur(data):
    for value in data:
        yield value

generateur = mon_generateur("hello world")
print (generateur)
for value in generateur:
    print(value)
"""
#Maintenant, faisons la liaison avec les itérateurs.

def mon_generateur(data):
    iterateur = iter(data)
    for idx in range(len(data)):
        yield (iterateur.__next__())


generateur = mon_generateur("hello world")
print (generateur)
for value in (generateur):
    print(value)

"""
#À tout moment, vous pouvez interrompre le générateur via la méthode « close() ».

def mon_generateur(data):
    for value in data:
        yield value


generateur = mon_generateur("hello world")
print (generateur)
for value in generateur:
    if value == 'w':
        generateur.close()
    else:
        print(value)
"""










