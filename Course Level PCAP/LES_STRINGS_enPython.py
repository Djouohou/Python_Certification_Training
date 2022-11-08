# a STRING is any series of characters that are interpreted literally by a script. All string methods returns new values. They do not change the original string.

#REMARQUE: chaque méthode de string ne modifie pas la string d’origine mais renvoie une nouvelle string avec les attributs modifiés. 

# string.ascii_letters
"""
Make sure to import string library function inorder to use ascii_letters.
Doesn't take any parameter, since it's not a function.
La concaténation des constantes ascii_lowercase et ascii.uppercase décrites ci-dessous.
Cette valeur n’est pas dépendante de l’environnement linguistique, donc ne changera pas.
"""
# import string library function
import string
  
# Storing the value in variable result
result = string.ascii_letters
print(result)     #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

#string.ascii_lowercase       Les lettres minuscules 'abcdefghijklmnopqrstuvwxyz'.
def check(value): 
    for letter in value: 
        if letter not in string.ascii_lowercase: 
            return False
    return True
     
# Driver Code 
input1 = "GeeksForGeeks"
print(input1, "--> ",  check(input1)) #False
     
input2 = "geeks for geeks"
print(input2, "--> ", check(input2))  #False
     
input3 = "geeksforgeeks"
print(input3, "--> ", check(input3))  #True


# string.ascii_uppercase    Les lettres majuscules 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.
import string
result = string.ascii_uppercase 
print(result)   #ABCDEFGHIJKLMNOPQRSTUVWXYZ


#string.digits   La chaîne '0123456789'.
import string
def check(value): 
    for letter in value: 
        if letter not in string.digits: 
            return False
    return True
     
# Driver Code 
input1 = "0123 456 789"
print(input1, "--> ",  check(input1))   #False
     
input2 = "12.0124"
print(input2, "--> ", check(input2))     #False
     
input3 = "12345"
print(input3, "--> ", check(input3))     #True



#string.hexdigits         La chaîne '0123456789abcdefABCDEF'.
import string
result = string.hexdigits 
print(result)         #0123456789abcdefABCDEF

#string.octdigits      La chaîne '01234567.


#string.punctuation    Chaîne de caractères ASCII considérés comme ponctuation dans l’environnement linguistique C.
import string
result = string.punctuation 
print(result)          #!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~


#string.printable     Chaîne de caractères ASCII considérés comme affichables. C’est une combinaison de digits, ascii_letters, punctuation, et whitespace.
import string
Sentence = "Hey, Geeks !, How are you?"  
for i in Sentence:
      
    # checking whether the char is printable value
    if i in string.printable:   

    if i.isprintable:
          
        # Printing the printable values 
        print("printable Value is: " + i)        
"""
pour avoir ce resultat, on peu aussi utilisé la syntaxe: if i.isprintable au lieu de if i in string.printable
printable Value is: H
printable Value is: e
printable Value is: y
printable Value is: ,
printable Value is:  
printable Value is: G
printable Value is: e
printable Value is: e
printable Value is: k
printable Value is: s
printable Value is:  
printable Value is: !
printable Value is: ,
printable Value is:  
printable Value is: H
printable Value is: o
printable Value is: w
printable Value is:  
printable Value is: a
printable Value is: r
printable Value is: e
printable Value is:  
printable Value is: y
printable Value is: o
printable Value is: u
printable Value is: ?
"""


#string.whitespace   Une chaîne comprenant tous les caractères ASCII considérés comme espaces. Sont inclus les caractères espace, tabulations, saut de ligne, retour du chariot, saut de page, et tabulation verticale.

Sentence = "Hey, Geeks !, How are you?" 
  
for i in Sentence:
      
    # checking whether the whitespace is present 
    if i in string.whitespace:
          
        # Printing the whitespace values 
        print("printable Value is: " + i)    
"""
printable Value is:  
printable Value is:  
printable Value is:  
printable Value is:  
printable Value is:
"""


#EXEMPLES DE FORMATS

#Accéder à un argument par sa position :

print('{0}, {1}, {2}'.format('a', 'b', 'c'))
a, b, c

print('{}, {}, {}'.format('a', 'b', 'c'))  # 3.1+ only
a, b, c

print('{2}, {1}, {0}'.format('a', 'b', 'c'))
c, b, a

print('{2}, {1}, {0}'.format(*'abc'))      # unpacking argument sequence
c, b, a

print('{0}{1}{0}'.format('abra', 'cad'))  # arguments' indices can be repeated
abracadabra


#Accéder à un argument par son nom :
print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
Coordinates: 37.24N, -115.81W

coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print('Coordinates: {latitude}, {longitude}'.format(**coord))
Coordinates: 37.24N, -115.81W

#Accéder aux attributs d’un argument :
c = 3-5j
print(('The complex number {0} is formed from the real part {0.real}''and the imaginary part {0.imag}.').format(c))
#The complex number (3-5j) is formed from the real part 3.0 and the imaginary part -5.0.

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)

print(str(Point(4, 2)))         #Point(4, 2)

#Accéder aux éléments d’un argument :
coord = (3, 5)
print('X: {0[0]};  Y: {0[1]}'.format(coord))        #X: 3;  Y: 5

#Remplacer %s et %r :
print("repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2'))  #repr() shows quotes: 'test1'; str() doesn't: test2

#Aligner le texte et spécifier une longueur minimale :
print('{:<30}'.format('left aligned')          #'left aligned                  '
print('{:>30}'.format('right aligned')         #'                 right aligned'
print('{:^30}'.format('centered')            #'           centered           '
print('{:*^30}'.format('centered')  # use '*' as a fill char
#'***********centered***********'


#Remplacer %+f, %-f, et %f et spécifier un signe :
print('{:+f}; {:+f}'.format(3.14, -3.14))  # show it always
#'+3.140000; -3.140000'
print('{: f}; {: f}'.format(3.14, -3.14))  # show a space for positive numbers
#' 3.140000; -3.140000'
print('{:-f}; {:-f}'.format(3.14, -3.14))  # show only the minus -- same as '{:f}; {:f}'
#'3.140000; -3.140000'


#Remplacer %x et %o et convertir la valeur dans différentes bases :

# format also supports binary numbers
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))         #'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
# with 0x, 0o, or 0b as prefix:
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))     #'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'


#Utiliser une virgule comme séparateur des milliers :
print('{:,}'.format(1234567890))      #'1,234,567,890'

#Exprimer un pourcentage :
points = 19
total = 22
print('Correct answers: {:.2%}'.format(points/total))       #'Correct answers: 86.36%'

#Utiliser un formatage propre au type :
import datetime
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))       #'2010-07-04 12:15:58'


#Arguments imbriqués et des exemples plus complexes :
for align, text in zip('<^>', ['left', 'center', 'right']):
    print('{0:{fill}{align}16}'.format(text, fill=align, align=align))

'left<<<<<<<<<<<<'
'^^^^^center^^^^^'
'>>>>>>>>>>>right'

octets = [192, 168, 0, 1]
print('{:02X}{:02X}{:02X}{:02X}'.format(*octets))       #'C0A80001'

print(int('9842000', 16))        #159653888

width = 5
for num in range(5,12):
    for base in 'dXob':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print()

"""
    5     5     5   101 
    6     6     6   110 
    7     7     7   111 
    8     8    10  1000 
    9     9    11  1001 
   10     A    12  1010 
   11     B    13  1011 
"""

#AUTRES METHODES DES OBJETS STRINGS
#string.index(c) : retrouve l'index de la première occurrence du caractère "c" dans la chaîne, ou déclenche une erreur si absent (ValueError: substring not found).
La méthode index() recherche la première occurrence de la valeur spécifiée. Elle lève une exception si la valeur n’est pas trouvée.
La méthode index() est presque pareil à la méthode find(), la seule différence est que la méthode find() renvoie -1 si la valeur n’est pas trouvée.
Syntaxe: string.index(value, start, end)
Paramètres:
value(Obligatoire) : La valeur à rechercher
start(Optionnel) : Où commencer la recherche. La valeur par défaut est 0
end(Optionnel) : Où terminer la recherche. La valeur par défaut est à la fin de la chaîne
Valeur de retour: La méthode index() renvoie une valeur entière:
Si la sous-chaîne existe à l’intérieur de la chaîne, elle renvoie l’index le plus petit de la chaîne où se trouve la sous-chaîne.
Si la sous-chaîne n’existe pas à l’intérieur de la chaîne, elle déclenche une exception ValueError.

foin = "Portez ce vieux whisky au juge blond qui fume"
print (foin.index("w"))      #16

#string.find(aiguille) : cherche la position d'une sous-chaîne aiguille dans la chaîne, en partant du début.
La méthode find() recherche la première occurrence de la valeur spécifiée et renvoie -1 si la valeur n’est pas trouvée.
La méthode find() est presque pareil à la méthode index(),la seule différence est que la méthode index() lève une exception si la valeur n’est pas trouvée.
Paramètres:
value(Obligatoire) : La valeur à rechercher
start(Optionnel) : Où commencer la recherche. La valeur par défaut est 0
end(Optionnel) : Où terminer la recherche. La valeur par défaut est à la fin de la chaîne 
Valeur de retour: La méthode find() renvoie une valeur entière:
Si la sous-chaîne existe à l’intérieur de la chaîne, elle renvoie l’index de la première occurrence de la sous-chaîne.
Si la sous-chaîne n’existe pas à l’intérieur de la chaîne, elle renvoie 1.

foin = "Cette leçon vaut bien un fromage, sans doute ?"
aiguille = "fromage"
print(foin.find(aiguille))       #25

#rfind(aiguille) : pareil que "find" mais en partant de la fin (reverse).
La méthode rfind() recherche la dernière occurrence de la valeur spécifiée et renvoie 1 si la valeur n’est pas trouvée.
La méthode rfind() est presque la même que la méthode rindex().
Paramètres: La méthode rfind() prend trois paramètres:
value(Obligatoire) : La valeur à trouver
start(Optionnel) : Où commencer la recherche. La valeur par défaut est 0
end(Optionnel) : Où terminer la recherche. La valeur par défaut est à la fin de la chaîne
Valeur de retour: La méthode rfind() renvoie une valeur entière.
Si la sous-chaîne existe dans la chaîne, elle renvoie l’index le plus élevé où la sous-chaîne est trouvée.
Si la sous-chaîne n’existe pas dans la chaîne, elle renvoie 1.      

foin = "Cette leçon vaut bien deux fromages, dont un fromage râpé ?"
aiguille = "fromage"
print(foin.rfind(aiguille))           #45
          
#string.count(aiguille) : compte le nombre de sous-chaînes aiguille dans la chaîne.
La méthode count() renvoie le nombre de fois qu’une valeur spécifiée apparaît dans la chaîne.
Paramètres: La méthode count() prend un seul paramètre:
value(Obligatoire) : La chaîne à rechercher.
start(Optionnel) : Un nombre indique la position où commencer la recherche. La valeur par défaut est 0.
end(Optionnel) : Un nombre indique la position où se termine la recherche. La valeur par défaut est la fin de la chaîne.

foin = "Le héron au long bec emmanché d'un long cou"
aiguille = 'long'
print(foin.count(aiguille))        #2

#string.lower() : convertit une chaîne en minuscules. La méthode lower() ne prend aucun paramètre.

phrase ="ATTENTION : Danger !"
print(phrase.lower())   #attention : danger !

#string.upper() : convertit une chaîne en majuscules. La méthode upper() ne prend aucun paramètre.Si aucun caractère minuscules n’existe, il renvoie la chaîne d’origine.

phrase = "Merci beaucoup"
print(phrase.upper())        #MERCI BEAUCOUP

#string.capitalize() : convertit en majuscule la première lettre d'une chaîne.La méthode capitalize() ne prend aucun paramètre.

phrase = "quel beau temps, aujourd'hui !"
print(phrase.capitalize())           #"Quel beau temps, aujourd'hui !"

#string.swapcase() : convertit toutes les majuscules en minuscules et vice-versa.La méthode swapcase() ne prend aucun paramètre.

phrase = "La CIGALE et la FOURMI"
print(phrase.swapcase())          #lA cigale ET LA fourmi

#string.strip() : enlève les espaces éventuels au début et à la fin de la chaîne (trime).
La méthode strip() supprime tous les caractères à droite et à gauche (l’espace est le caractère par défaut à supprimer).
Pour supprimer que les caractères à droite utiliser rstrip() et pour supprimer que les caractères à gauche utiliser lstrip().
Paramètres: La méthode strip() prend un seul paramètre:
characters (Optionnel) : une chaîne spécifiant le jeu de caractères à supprimer. Si l’argument characters n’est pas fourni,
tous les espaces au début et à la fin sont supprimés de la chaîne.
Valeur de retour: La méthode strip() retourne une copie de la chaîne avec les premiers et derniers caractères supprimés.
Toutes les caractères dans l’argument « characters » sont supprimées à gauche et à droite de la chaîne.

phrase = "   Monty Python   "
print(phrase.strip())        #'Monty Python'

#string.replace(old, new) : remplace tous les caractères old par des caractères new dans la chaîne.
La méthode replace() remplace une chaîne de caractères spécifiée par une autre chaîne de caractères spécifiée.
Syntaxe: string.replace(oldStr, newStr, count)
Paramètres: La méthode replace() prend trois paramètres:
oldStr(Obligatoire) : La chaîne à rechercher
newStr(Obligatoire) : La chaîne par laquelle remplacer l’ancienne chaîne
count(Optionnel) : Un nombre spécifiant le nombre d’occurrences de l’ancienne chaîne que vous souhaitez remplacer. La valeur par défaut est toutes les occurrences
La méthode replace() renvoie une copie de la chaîne dans laquelle l’ancienne chaîne est remplacée par la nouvelle chaîne . La chaîne d’origine ne change pas.
Si l’ancienne chaîne n’est pas trouvée, elle renvoie la copie de la chaîne d’origine.

phrase = "Si ce n'est toi c'est donc ton frère"
print(phrase.replace(" ","_"))             #Si_ce_n'est_toi_c'est_donc_ton_frère


#string.index()
La méthode index() recherche la première occurrence de la valeur spécifiée. Elle lève une exception si la valeur n’est pas trouvée.
La méthode index() est presque pareil à la méthode find(), la seule différence est que la méthode find() renvoie -1 si la valeur n’est pas trouvée.
Syntaxe: string.index(value, start, end)
Paramètres:
value(Obligatoire) : La valeur à rechercher
start(Optionnel) : Où commencer la recherche. La valeur par défaut est 0
end(Optionnel) : Où terminer la recherche. La valeur par défaut est à la fin de la chaîne
Valeur de retour: La méthode index() renvoie une valeur entière:
Si la sous-chaîne existe à l’intérieur de la chaîne, elle renvoie l’index le plus petit de la chaîne où se trouve la sous-chaîne.
Si la sous-chaîne n’existe pas à l’intérieur de la chaîne, elle déclenche une exception ValueError.
      
#Dans la plupart de ces méthodes, il est possible de préciser quelle portion de la chaîne doit être traitée, en ajoutant des arguments supplémentaires.
print(ch9.index("e"))		# cherche à partir du début de la chaîne 
4							# et trouve le premier 'e'
print(ch9.index("e",5))		# cherche seulement à partir de l'indice 5
8							# et trouve le second 'e'
print(ch9.index("e",15))		# cherche à partir du caractère n° 15
29							# et trouve le quatrième 'e'

#string.title() : convertit la string en casse du titre
text = 'jE conVERtis en Format tiTRe'
print(text.title())          #Je Convertis En Format Titre

#string.capitalize()	Converts the first character of the string to a capital (uppercase) letter
#string.casefold()	Implements caseless string matching, La méthode casefold() ne prend aucun paramètre.
La méthode casefold() renvoie une chaîne où tous les caractères sont en minuscules.
Cette méthode est similaire à la méthode lower(), mais la méthode casefold() est plus forte, plus agressive, ce qui signifie qu’elle convertira plus de caractères en
minuscules et trouvera plus de correspondances lors de la comparaison des deux chaînes et les deux sont convertis à l’aide de la méthode casefold().
"""
Implémente la correspondance de string sans casse
Elle est similaire à la méthode de chaîne lower() mais la casse supprime toutes les distinctions de casse présentes dans une chaîne.
c’est à dire ignorer les cas lors de la comparaison.
This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lower case,
and will find more matches when comparing two strings and both are converted using the casefold() method.
"""
string='JE TESTE MES STRINGS'         
print("After String is:",string.casefold())       #After String is: je teste mes strings

#string.center()	Pad the string with the specified character.crée et retourne une nouvelle chaîne qui est complétée avec le caractère spécifié.
La méthode center() alignera la chaîne au centre, en utilisant un caractère spécifié (espace par défaut) comme caractère de remplissage.
Syntaxe: string.center(length, char)
Paramètres:
length (Obligatoire) : La longueur de la chaîne retournée
char (Optional) : Le caractère pour remplir l’espace manquant de chaque côté. La valeur par défaut est " " (espace) 
Valeur de retour: La méthode center() renvoie une chaîne remplie avec char spécifié. Il ne modifie pas la chaîne d’origine.
    
string='je teste mes strings'       #la string a 20 caracteres
  
print("After padding String is:",string.center(24))           #After padding String is:   je teste mes strings  
print("After padding String is:",string.center(27,'*'))        #After padding String is: ****je teste mes strings***
print("After padding String is:",string.center(28,'*'))       #After padding String is: ****je teste mes strings****

#string.count()	        Returns the number of occurrences of a substring in the string.
La méthode count() renvoie le nombre de fois qu’une valeur spécifiée apparaît dans la chaîne.
Syntaxe: string.count(value, start, end)
Paramètres: La méthode count() prend un seul paramètre:
value(Obligatoire) : La chaîne à rechercher.
start(Optionnel) : Un nombre indique la position où commencer la recherche. La valeur par défaut est 0.
end(Optionnel) : Un nombre indique la position où se termine la recherche. La valeur par défaut est la fin de la chaîne.
      
str = "I like Python, Python are my favorite language"
n = str.count("Python")
print(n)         #2

str = "I like Python, Python are my favorite language"
n = str.count("Python", 12, 20)
print(n)         #1

#string.encode()	Encodes strings with the specified encoded scheme
La méthode encode() encode la chaîne, en utilisant l’encodage spécifié. Si aucun encodage n’est spécifié, UTF-8 sera utilisé.
Depuis Python 3.0, les chaînes sont stockées en Unicode, c’est-à-dire que chaque caractère de la chaîne est représenté par un code.
Ainsi, chaque chaîne n’est qu’une séquence de code.
Pour un stockage efficace de ces chaînes, la séquence de code est convertie en un ensemble d’octets. Le processus est connu sous le nom de codage. 
Il existe différents encodages qui traitent une chaîne différemment. Les encodages populaires étant utf-8, ascii, etc.
En utilisant la méthode encode(), vous pouvez convertir des chaînes non codées en n’importe quel encodage pris en charge par Python. Par défaut, Python utilise le codage utf-8.
Syntaxe: string.encode(encoding=encoding, errors=errors)
Paramètres: La méthode encode() prend les paramètres suivants :
encoding(Optionnel) : Une chaîne spécifiant l’encodage à utiliser. La valeur par défaut est UTF-8
errors(Optionnel) : Cela peut être donné pour définir une méthode de gestion des erreurs différent.
backslashreplace’ : utilise antislash « \ » au lieu du caractère qui n’a pas pu être encodé
‘ignore’ : ignore les caractères qui ne peuvent pas être encodés
‘namereplace’ : remplace le caractère par un texte expliquant le caractère
‘strict’ : c’est la valeur par défaut, déclenche une erreur en cas d’échec
‘replace’ : remplace le caractére par un point d’interrogation
‘xmlcharrefreplace’ : remplace le caractère par un caractère xml

"""
Les chaînes peuvent utiliser la fonction encode() qui renvoie la version codée de la chaîne selon le codage spécifié.
Syntaxe: encode (encodage, erreur)
Paramètres:
encoding: spécifie l’encodage sur la base duquel l’encodage doit être effectué.
error: Décide comment gérer les erreurs si elles se produisent, par exemple «strict» déclenche une erreur Unicode en cas d’exception
et «ignorer» ignore les erreurs survenues.
"""
string='je teste mes strings'
print ("la chaine codé en format utf8 est : ",)          #la chaine codé en format utf8 est : 
print (string.encode('utf8', 'ignore'))            #b'je teste mes strings'
      
#string.endswith()	Returns “True” if a string ends with the given suffix
La méthode endswith() renvoie True si une chaîne se termine par le suffixe donné sinon renvoie False.
Syntaxe: string.endswith(suffix, start, end)
Paramètres: La méthode endswith() prend trois paramètres:
suffixe: le suffixe n’est rien d’autre qu’une chaîne qui doit être vérifiée.
start: position de départ à partir de laquelle le suffixe doit être vérifié dans la chaîne.
end: position de fin à partir de laquelle le suffixe doit être vérifié dans la chaîne.

#string.expandtabs()	Specifies the amount of space to be substituted with the “\t” symbol in the string
La méthode expandtabs() définit la taille de tabulation sur le nombre spécifié d’espaces. 
Syntaxe: string.expandtabs(tabsize)
Paramètres: La méthode expandtabs() prend un seul paramètre:
tabsize(Optionnel) Un nombre spécifiant la taille de tabulation. La taille de tabulation par défaut est 8
Valeur de retour: La méthode expandtabs() renvoie une copie de la chaîne dans laquelle les caractères de tabulation, c’est-à-dire « \t »,
ont été étendu à l’aide des espaces.

"""
Parfois, il est nécessaire de spécifier l’espace dans la chaîne, mais la quantité d’espace à laisser est incertaine et dépend de l’environnement et des conditions.
Dans ces cas, la nécessité de modifier la chaîne, encore et encore, est une tâche fastidieuse.
Par conséquent, python dans sa bibliothèque a « expandtabs() » qui spécifie la quantité d’espace à remplacer par le symbole «\ t» dans la chaîne.
l’exception de cette méthode est qu’elle n’accepte pas le nombre à virgule flottante si nous voulons décider de la précision exacte de l’espace dont nous avons besoin.
"""
string = "je\tteste\tmes\tstring"
  
print("Modified string using default spacing: ", end ="")    #Modified string using default spacing: je      teste   mes     string
print(string.expandtabs()) 
  
print("Modified string using less spacing: ", end ="")           #Modified string using less spacing: je  teste mes string
print(string.expandtabs(2)) 
  
print("Modified string using more spacing: ", end ="")           #Modified string using more spacing: je         teste       mes         string
print(string.expandtabs(12)) 

#string.format_map()	Formats specified values in a string using a dictionary
"""
La fonction format_map() est une fonction intégrée en Python, qui est utilisée pour renvoyer la valeur d’une clé de dictionnaire.
input_dict : prend un seul paramètre qui est le dictionnaire d'entrée.
Renvoie les valeurs de clé du dictionnaire d'entrée.
"""
a = {'voiture':'Ferrari', 'couleur':'rouge'} 
print("Ma {voiture} est de couleur {couleur}".format_map(a))     #Ma Ferrari est de couleur rouge

profession = { 'name':['Barry', 'Bruce'], 
               'profession':['Engineer', 'Doctor'], 
               'age':[30, 31] } 
                       
print('{name[0]} is an {profession[0]} and he'
      ' is {age[0]} years old.'.format_map(profession))     #Barry is an Engineer and he is 30 years old.
        
print('{name[1]} is an {profession[1]} and he'
      ' is {age[1]} years old.'.format_map(profession))      #Bruce is an Doctor and he is 31 years old.

#string.index()	        Returns the position of the first occurrence of a substring in a string
"""
Remarque: La méthode index() est similaire à find() . La seule différence est que find() renvoie -1 si la chaîne recherchée n’est pas trouvée
et que index() lève une exception dans ce cas.
renvoie la position de la première occurrence de sous-chaîne dans une chaîne.
Syntaxe: ch.index (ch1, begp, endp)
Paramètres:
ch1: La chaîne à rechercher.
begp (par défaut: 0): Cette fonction spécifie la position à partir de laquelle la recherche doit être lancée.
endp (par défaut: string_len): Cette fonction spécifie la position à partir de laquelle la recherche doit se terminer.
Valeur de retour : renvoie la première position de la sous-chaîne trouvée.
"""
ch = "je teste mes strings dans mon fichier strings"
ch1 = "strings"
pos = ch.index(ch1,2)  
print ("The first position of strings after 2nd index : ",end="")    #The first position of strings after 2nd index : 13
print (pos) 
    
#string.isalnum()	Checks whether all the characters in a given string is alphanumeric or not.  ne prend aucun paramètre.
#string.isalpha()	Returns “True” if all characters in the string are alphabets.  ne prend aucun paramètre.
#string.isdecimal()	Returns true if all characters in a string are decimal renvoie true si tous les caractères d’une chaîne sont décimaux.et renvoie false sinon.
s = "12345"
print(s.isdecimal())   #True     ne prend aucun paramètre.
  
s = "12strings34"
print(s.isdecimal())   #False
  
s = "12 34"
print(s.isdecimal())   #False
      
#string.isdigit()	Returns “True” if all characters in the string are digits  .ne prend aucun paramètre.
"""
Il ne prend aucun argument, donc il renvoie une erreur si un paramètre est passé
Les exposants et les indices sont considérés comme des caractères numériques avec les caractères décimaux, par conséquent, isdigit() renvoie «True».
Les chiffres romains, les numérateurs de devises et les fractions ne sont pas considérés comme des chiffres. Par conséquent, isdigit() renvoie «False»
"""
string = '15460'
print(string.isdigit())    #True
 
string = '154tester60'
print(string.isdigit())       #False
      
#string.isidentifier()	Check whether a string is a valid identifier or not. ne prend aucun paramètre.
La méthode isidentifier() renvoie True si la chaîne est un identifiant valide, sinon renvoie False.
Une chaîne est considérée comme un identifiant valide si elle ne contient que des lettres alphanumériques (a-z) et (0-9) ou des tirets (_).
Un identifiant valide ne peut pas commencer par un nombre ou contenir des espaces.
"""
Cette fonction intégrée de Python est utilisée pour vérifier si une chaîne est un identifiant valide ou non.
La méthode renvoie True si la chaîne est un identifiant valide, sinon, False.

“An identifier is a name given to an entity”.
In very simple words, an identifier is a user-defined name to represent the basic building blocks of Python.
It can be a variable, a function, a class, a module, or any other object.
Now you know what exactly identifiers are. So, how do we use them? We can’t use anything,
there are some certain rules to keep in mind that we must follow while naming identifiers.

1. The Python identifier is made with a combination of lowercase or uppercase letters, digits or an underscore.
These are the valid characters. Lowercase letters (a to z), Uppercase letters (A to Z) ,Digits (0 to 9), Underscore (_)
Examples of a valid identifier: num1, FLAG, get_user_name, userDetails, _1234

2. An identifier cannot start with a digit. If we create an identifier that starts with a digit then we will get a syntax error.
3. We also cannot use special symbols in the identifiers name. Symbols like ( !, @, #, $, %, . ) are invalid.
4. A keyword cannot be used as an identifier. In Python, keywords are the reserved names that are built-in in Python.
They have a special meaning and we cannot use them as identifier names.
5. The length of the identifiers can be as long as you want. Of course, it can not be greater than the available memory,
however, the PEP-8 standards rule suggests not to exceed 79 characters in a line.
"""
print( 'name'.isidentifier() )     #true
print( '#today'.isidentifier() )    #false
print( '_12hello'.isidentifier() )  #true
print( '8cellos'.isidentifier() )   #false
print( 'today is me'.isidentifier() )    #false because of spacings
print( ''.isidentifier() )    #false
      
#string.islower()	Checks if all characters in the string are lowercase. ne prend aucun paramètre.
#string.isnumeric()	Returns “True” if all characters in the string are numeric characters , sinon elle renvoie «False». ne prend aucun paramètre.
#si elle contient tous les caractères numériques tels que: entiers, fractions, indice, exposant, chiffres romains etc. (tous écrits en unicode)
string = '15460'
print(string.isnumeric())    #True
  
string = '154tester60'
print(string.isnumeric())       #False

print('\ u00BD'.isnumeric())    #False

#string.isprintable()	Returns “True” if all characters in the string are printable or the string is empty. ne prend aucun paramètre.
#string.isspace()	Returns “True” if all characters in the string are whitespace characters. ne prend aucun paramètre.
a méthode isspace() est une méthode intégrée en Python qui renvoie True si tous les caractères d’une chaîne sont des espaces, sinon elle renvoie False.
Cette fonction est utilisée pour vérifier si l’argument contient tous les caractères d’espacement tels que:
    " " : Espace
    "\t" : Tabulation horizontale
    "\v" : Tabulation verticale
    "\n" : Saut de ligne
    "\f" : Flux
    "\r" : Retour chariot

#string.istitle()	Returns “True” if the string is a title cased string. ne prend aucun paramètre.
#string.isupper()	Checks if all characters in the string are uppercase. ne prend aucun paramètre.
#string.join()	        Returns a concatenated String
Transforme un liste en chaine en utilisant les caracteres de jointure.
La méthode join() renvoie une chaîne en joignant tous les éléments d’un itérable, séparés par un séparateur de chaîne.
La méthode join() permet de créer des chaînes à partir des objets itérables. Il joint chaque élément d’un itérable (comme une liste, une chaîne, tuple, etc…)
par un séparateur de chaîne (la chaîne sur laquelle la méthode join() est appelée) et renvoie la chaîne concaténée.
La méthode join() prend un seul paramètre:
iterable(Obligatoire) : Tout objet itérable où toutes les valeurs renvoyées sont des chaînes

list1 = ['1','2','3','4']
x='abcdef'
s ="-" .join(list1)
t ="*" .join(x)
print(s)       #1-2-3-4
print(t) #a*b*c*d*e*f     
      
#string.ljust()	        Left aligns the string according to the width specified
rallonge la chaine vers la droite par rapport au caracter specifie .
      """
The ljust() method will left align the string, using a specified character (space is default) as the fill character.
Syntax: string.ljust(length, character)
length 	: Required. The length of the returned string
character :Optional. A character to fill the missing space (to the right of the string). Default is " " (space).
La méthode ljust() prend deux paramètres:
length(Obligatoire) : La longueur de la chaîne retournée
character(Optionnel) : Un caractère pour remplir l’espace manquant (à droite de la chaîne). La valeur par défaut est " " (espace).
Valeur de retour:
La méthode ljust() renvoie la chaîne alignée à gauche dans la largeur minimale donnée.
Si le paramètre character est défini, il remplit également l’espace restant avec le caractère défini.

"""
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")    #banana               is my favorite fruit.

txt = "banane"
x = txt.ljust(20, "O")
print(x)   #bananeOOOOOOOOOOOOOO

#string.lower()	        Converts all uppercase characters in a string into lowercase
#string.lstrip()	Returns the string with leading characters removed
"""
lstrip()La méthode renvoie une copie de la chaîne avec les premiers caractères supprimés (en fonction de l’argument de chaîne passé).
Si aucun argument n’est passé, il supprime les espaces de début.
"""
string = "jemange" 
print(string.lstrip('je'))   #mange
string = "   jemange" 
print(string.lstrip())   #jemange

#string.maketrans()	 Returns a translation table
"""
The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.
Syntax: string.maketrans(x, y, z)

x 	Required. If only one parameter is specified, this has to be a dictionary describing how to perform the replace. If two or more parameters are specified,
this parameter has to be a string specifying the characters you want to replace.
y 	Optional. A string with the same length as parameter x. Each character in the first parameter will be replaced with the corresponding character in this string.
z 	Optional. A string describing which characters to remove from the original string.

La méthode maketrans() renvoie une table de traduction(table de translation ou de correspondance) qui mappe chaque caractère du str1 dans le caractère à la même position dans la chaîne str2.
Ensuite, cette table est passée à la fonction translate().
Remarque : str1 et str2 doivent avoir la même longueur.

Syntaxe: string.maketrans(str1, str2)
Paramètres: La méthode maketrans() prend deux paramètres:
str1 : Il s’agit d’une chaîne de caractères.
str2 : Il s’agit de la chaîne ayant le caractère de mappage correspondant.
Valeur de retour: La méthode maketrans() renvoie une table de traduction.
"""
#Create a mapping table, and use it in the translate() method to replace any "S" characters with a "P" character:
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))      #Hello Pam!

#The third parameter in the mapping table describes characters that you want to remove from the string:
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable))        #G i Joe!

#Use a mapping table to replace many characters:
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x, y)
print(txt.translate(mytable))           #Hi Joe!


#The maketrans() method itself returns a dictionary describing each replacement, in unicode:
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
print(txt.maketrans(x, y, z))      #{109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}

#L’exemple suivant montre l’utilisation de la méthode maketrans(). Chaque voyelle d’une chaîne est remplacée par sa position de voyelle
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
txt = "Welcome to WayToLearnX!"
print (txt.translate(trantab))       #W2lc4m2 t4 W1yT4L21rnX!
      
#string.partition()	Splits the string at the first occurrence of the separator
"""
La méthode partition() recherche une chaîne spécifiée et divise la chaîne en un tuple contenant trois éléments.
Le premier élément contient la partie avant la chaîne spécifiée.
Le deuxième élément contient la chaîne spécifiée. Le troisième élément contient la partie après la chaîne.
      
Syntaxe: string.partition(value) 
Paramètres: La méthode partition() prend un seul paramètre:
valeur(Obligatoire) : La chaîne à trouver
"""
#Recherchez le mot « Python » et renvoyez un tuple avec trois éléments: takes exactly one argument
str = "I love Python as a programming language"
res = str.partition("Python")
print(res)       #('I love ', 'Python', ' as a programming language')

str = "I love Python as a programming language"
res = str.partition("Java")
print(res)      # ('I love Python as a programming language', '', '')   on aura toujours trois compartiments d'ou ici les deux autres sont vides.
      
#string.replace()	Replaces all occurrences of a substring with another substring
#string.rfind()	        Returns the highest index of the substring
La méthode rfind() recherche la dernière occurrence de la valeur spécifiée et renvoie 1 si la valeur n’est pas trouvée.
La méthode rfind() est presque la même que la méthode rindex().
      
Syntaxe: string.rfind(value, start, end) 
Paramètres: La méthode rfind() prend trois paramètres:
value(Obligatoire) : La valeur à trouver
start(Optionnel) : Où commencer la recherche. La valeur par défaut est 0
end(Optionnel) : Où terminer la recherche. La valeur par défaut est à la fin de la chaîne
Valeur de retour: La méthode rfind() renvoie une valeur entière.
*Si la sous-chaîne existe dans la chaîne, elle renvoie l’index le plus élevé où la sous-chaîne est trouvée.
*Si la sous-chaîne n’existe pas dans la chaîne, elle renvoie -1.

#Où dans le texte se trouve la dernière occurrence de la chaîne « nice » ?
string = "He is nice, you are nice."
res = string.rfind("nice")
print(res)    #20

#Où dans le texte se trouve la dernière occurrence de la lettre « o » lorsque vous recherchez uniquement entre la position 6 et 10 ?
str = "Welcome to WayToLearnX"
res = str.rfind("o", 6, 10)
print(res)       #9

#string.rindex()	Returns the highest index of the substring inside the string,lève une exception si la valeur n’est pas trouvée.
"""
La méthode rindex() est presque la même que la méthode rfind().
Syntaxe: string.rindex(value, start, end)
Paramètres: La méthode rindex() prend trois paramètres:
value(Obligatoire) : La valeur à trouver
start(Optionnel) : Où commencer la recherche. La valeur par défaut est 0
end(Optionnel) : Où terminer la recherche. La valeur par défaut est à la fin de la chaîne
Valeur de retour: La méthode rindex() renvoie une valeur entière.
*Si la sous-chaîne existe dans la chaîne, elle renvoie l’index le plus élevé où la sous-chaîne est trouvée.
*Si la sous-chaîne n’existe pas dans la chaîne, elle lève une exception.
"""
string = "He is nice, you are nice."
res = string.rindex("nice")
print(res)    #20

str = "Welcome to WayToLearnX"
res = str.rindex("o", 6, 10)
print(res)       #9

#string.rjust()	        Right aligns the string according to the width specified
"""
La méthode rjust() alignera à droite la chaîne, en utilisant un caractère spécifié (espace par défaut) comme caractère de remplissage.
 
Syntaxe: string.rjust(length, character)
Paramètres: La méthode rjust() prend deux paramètres:
length(Obligatoire) : La longueur de la chaîne retournée
character(Optionnel) : Un caractère pour remplir l’espace manquant (à gauche de la chaîne). La valeur par défaut est " " (espace).
 
Valeur de retour: La méthode rjust() renvoie la chaîne alignée à droite dans la largeur minimale donnée.
Si le paramètre character est défini, il remplit également l’espace restant avec le caractère défini.
"""
str = "WayToLearnX:"
x = str.rjust(25)
print(x, "is the best platform for learning.")      #             WayToLearnX: is the best platform for learning.

#En utilisant le caractère « * » comme caractère de remplissage:
str = "WayToLearnX:"
x = str.rjust(25, "*")
print(x, "is the best platform for learning.")     #*************WayToLearnX: is the best platform for learning.


#string.rpartition()	Split the given string into three parts
ici quand la chaine nest pas trouve, la chaine est renvoye comme dernier element du tuple. pourtant avec la fonction partition ,il est le premier element.
"""
La méthode rpartition() recherche la dernière occurrence d’une chaîne spécifiée et divise la chaîne en un tuple contenant trois éléments.
Le premier élément contient la partie avant la chaîne spécifiée. Le deuxième élément contient la chaîne spécifiée.
Le troisième élément contient la partie après la chaîne.
La méthode rpartition() prend un seul paramètre.  valeur(Obligatoire) : La chaîne à trouver
"""
str = "I love Python as a programming language, Python is the best"
res = str.rpartition("Python")
print(res)     #('I love Python as a programming language, ', 'Python', ' is the best')

str = "I love Python as a programming language, Python is the best"
res = str.rpartition("Java")
print(res)      #('', '', 'I love Python as a programming language, Python is the best')


#string.rsplit()	Split the string from the right by the specified separator
"""
La méthode rsplit() divise une chaîne en une liste, en commençant par la droite. Vous pouvez spécifier le séparateur, le séparateur par défaut est un espace.
Cette méthode retournera la même chose que la méthode split().
La méthode rsplit() prend deux paramètres:
separator(Optionnel) : Spécifie le séparateur à utiliser lors de division de la chaîne. Par défaut, l’espace est un séparateur
maxsplit(Optionnel) : Spécifie le nombre de division à effectuer. La valeur par défaut est -1, qui signifier « toutes les occurrences »
Valeur de retour: La méthode rsplit() divise une chaîne, en commençant par la droite selon le séparateur spécifié et renvoie une liste de chaînes.
"""
#Diviser la chaîne en une liste où chaque mot est un élément de liste:
str = "je teste mes strings"
res = str.rsplit()
print(res)         #['je', 'teste', 'mes', 'strings']

#Diviser la chaîne en utilisant une virgule, suivie d’une étoile et d'un espace, comme séparateur:
str = "je,* teste mes,* strings"
res = str.rsplit(",* ")
print(res)           #['je', 'teste mes', 'strings']


#string.rstrip()	Removes trailing characters.
La méthode rstrip() supprime tous les dernières caractères (l’espace est le dernière caractère par défaut à supprimer).
Paramètres: La méthode rstrip() prend un seul paramètre:
characters (Optionnel) : une chaîne spécifiant le jeu de caractères à supprimer.
Si l’argument characters n’est pas fourni, tous les espaces à la fin sont supprimés de la chaîne.
Valeur de retour: La méthode rstrip() retourne une copie de la chaîne avec les dernières caractères supprimés.
Toutes les caractères dans l’argument « characters » sont supprimées à droite de la chaîne.

#Supprimez les espaces à droite de la chaîne:
str = "      je teste mes strings      "
res = str.rstrip()
print(res)     #'      je teste mes strings'

#Supprimez les dernières caractères:
str = "je teste mes strings"
res = str.rstrip("ings")
print(res)     #je teste mes str

#string.splitlines()	Split the lines at line boundaries
La méthode splitlines() divise une chaîne en une liste. La division se fait aux sauts de ligne.
Syntaxe: string.splitlines(linebreaks)
Paramètres: La méthode splitlines() prend un seul paramètre:
linebreaks(Optionnel) : Spécifie si les sauts de ligne doivent être inclus (True) ou non (False). La valeur par défaut est False.
Valeur de retour: La méthode splitlines() renvoie la liste de lignes dans la chaîne.
S’il n’y a pas le caractère de saut de ligne « \n », il renvoie une liste avec un seul élément (une seule ligne).

#Diviser une chaîne en une liste où chaque ligne est un élément de liste:
str = "Hello World\n testeur de strings"
res = str.splitlines()
print(res)      #['Hello World', ' testeur de strings']

#Divisez la chaîne, mais gardez le caractère de saut de ligne « \n »:
str = "Hello World\n testeur de string"
res = str.splitlines(True)
print(res)       #['Hello World\n', ' testeur de string']

#string.startswith()	Returns “True” if a string starts with the given prefix
La méthode startswith() renvoie True si la chaîne commence par la valeur spécifiée, sinon False.
Syntaxe: string.startswith(value, start, end)
La méthode startswith() prend trois paramètres:
value(Obligatoire) : La valeur, pour vérifier si la chaîne commence par celle-ci
start(Optionnel) : Un entier spécifiant à quelle position démarrer la recherche
end(Optionnel) : Un entier spécifiant à quelle position terminer la recherche
Valeur de retour: La méthode startswith() renvoie:

#string.swapcase()	Converts all uppercase characters to lowercase and vice versa
La méthode string swapcase() convertit tous les caractères majuscules en minuscules et vice versa de la chaîne donnée et la renvoie.
 Syntaxe: string.swapcase()
Paramètres: La méthode swapcase() ne prend aucun paramètre.
Valeur de retour: La méthode swapcase() renvoie la chaîne dans laquelle tous les caractères majuscules sont convertis en minuscules et les
caractères minuscules sont convertis en majuscules.
      
#string.title()	        Convert string to title case
La méthode title() renvoie une chaîne dans laquelle le premier caractère de chaque mot est en majuscule.
Comme un en-tête ou un titre. Si le mot contient un nombre ou un symbole, la première lettre qui suit sera convertie en majuscules.
Syntaxe: string.title()
Paramètres: La méthode title() ne prend aucun paramètre.
 
#string.translate()	Modify string according to given translation mappings
La méthode translate() renvoie une copie d’une chaîne dans laquelle tous les caractères ont été traduits à l’aide de la table (construite avec la fonction maketrans()
dans le module String),en supprimant éventuellement tous les caractères trouvés dans la chaîne donnée.
Syntaxe: string.translate(table)
Paramètres: La méthode translate() prend un seul paramètre:
table : une table de traduction contenant le mappage entre deux caractères; généralement créé par maketrans()
Valeur de retour: La méthode translate() renvoie une chaîne dans laquelle chaque caractère est mappé sur son caractère correspondant conformément à la table de traduction.

#L’exemple suivant montre l’utilisation de la méthode translate(). Chaque voyelle d’une chaîne est remplacée par sa position de voyelle
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
txt = "Welcome to WayToLearnX!"
print (txt.translate(trantab))       #W2lc4m2 t4 W1yT4L21rnX!
      
#string.upper()	        Converts all lowercase characters in a string into uppercase
La méthode upper() renvoie une chaîne où tous les caractères sont en majuscules. Les symboles et les nombres sont ignorés.
Syntaxe: string.upper()
Paramètres: La méthode upper() ne prend aucun paramètre.
Valeur de retour: La méthode upper() renvoie la chaîne en majuscules. Il convertit tous les caractères minuscules en majuscules.
Si aucun caractère minuscules n’existe, il renvoie la chaîne d’origine.
      
#string.zfill()	        Returns a copy of the string with ‘0’ characters padded to the left side of the string
La méthode zfill() ajoute des zéros (0) au début de la chaîne, jusqu’à ce qu’il atteigne la longueur spécifiée.
Si la valeur du paramètre ‘len’ est inférieure à la longueur de la chaîne, aucun remplissage n’est effectué.
Syntaxe: string.zfill(len)
Paramètres: La méthode zfill() prend un seul paramètre:
len(Obligatoire) : Un nombre spécifiant la position de l’élément que vous souhaitez supprimer.

#Remplissez la chaîne avec des zéros jusqu’à ce qu’elle contienne 10 caractères:
str = "20"
res = str.zfill(10)
print(res)          #0000000020
#Remplissez la chaîne avec des zéros jusqu’à ce qu’elle contienne 3 caractères:
str = "10"
res = str.zfill(3)
print(res)           #010  

str = "mange"
res = str.zfill(3)
print(res)        #mange

str = "mange"
res = str.zfill(9)
print(res)       #0000mange










































































