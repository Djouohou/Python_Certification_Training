#La fonction OPEN() en python

La fonction open() ouvre un fichier et le renvoie en tant qu’objet fichier.
Elle renvoie un objet file qui peut être utilisé pour lire, écrire et modifier le fichier.Si le fichier n’existe pas, en fonction du mode d'ouverture il peut soit
creer le fichier soit il déclenche l’exception FileNotFoundError.
Syntaxe: open(file, mode)

Paramètres:
file : Le chemin et le nom du fichier(l'emplacement du fichier)
mode : définissez le mode dans lequel vous souhaitez ouvrir le fichier

    « r » – Read : Valeur par défaut. Ouvre un fichier en lecture, erreur si le fichier n’existe pas
    « a » – Append : Ouvre un fichier à ajouter, crée le fichier s’il n’existe pas(mode douverture en ecriture qui conserve le contenu du fichier)
    « w » – Write : Ouvre un fichier pour l’écriture, crée le fichier s’il n’existe pas(mode douverture en ecriture qui écrase/supprime le contenu du fichier)
    « x » – Create : Crée le fichier spécifié, renvoie une erreur si le fichier existe et sinon il va creer un erreur
    « t » : Ouvrir le fichier en mode texte.#ce mode n'existe plus actuellement
    « b » : Ouvrir le fichier en mode binaire.#ce mode n'existe plus actuellement
    « + » : Ouvrir un fichier pour mise à jour (lecture et écriture) #ce mode n'existe plus actuellement

# spécifiant le chemin complet
fichier = open('fiche.txt', 'r')
print(fichier.read())

with open('fiche.txt') as fichier:
    for l in fichier:
        print(l)
                                    

#Ouvrir deux fichiers avec l'instruction with

On peut avec l'instruction with ouvrir deux fichiers (ou plus) en même temps. Voyez l'exemple suivant :

with open("zoo.txt", "r") as fichier1, open("zoo2.txt", "w") as fichier2:
    for ligne in fichier1:
        fichier2.write("* " + ligne)

Si le fichier zoo.txt contient le texte suivant :

souris
girafe
lion
singe

alors le contenu de zoo2.txt sera :

* souris
* girafe
* lion
* singe

Dans cet exemple, with permet une notation très compacte en s'affranchissant de deux méthodes .close().



#la fonction CLOSE() en python. No parameters
La méthode close() referme le fichier. Celui-ci est désormais disponible pour tout usage.
Comme tout élément ouvert, il faut le refermer une fois les instructions terminées. Pour cela on utilise la syntaxe #fichier.close()
Python file method close() closes the opened file. A closed file cannot be read or written any more. Any operation, which requires that the file be opened will
raise a ValueError after the file has been closed. Calling close() more than once is allowed.
Python automatically closes a file when the reference object of a file is reassigned to another file. It is a good practice to use the close() method to close a file.

fichier = open("fiche.txt", "r")
print(fichier)                            #<_io.TextIOWrapper name='fiche.txt' mode='r' encoding='UTF-8'>
print( fichier.readlines())          #['girafe\n', 'tigre\n', 'singe\n', 'souris\n']

fichier.close()
print(fichier.readlines())      Traceback (most recent call last):
                                File "C:\Users\Ingrid\Desktop\COURS PROGRAMME\Course Level PCAP\Prog.py", line 20, in <module>
                                print(fichier.readlines())
                                ValueError: I/O operation on closed file.

Remarque: lorsqu'on applique la méthode .close() sur l'objet fichier, ce qui, vous vous en doutez, ferme le fichier (ceci correspondrait à fermer le livre).
Vous remarquerez que la méthode .close() ne renvoie rien mais modifie l'état de l'objet fichier en fichier fermé. Ainsi, si on essaie de lire à nouveau les lignes
du fichier, Python renvoie une erreur car il ne peut pas lire un fichier fermé .

#Il existe une autre syntaxe plus courte qui permet de s'emanciper du problème de fermeture du fichier: le mot clé with .
Voici la syntaxe:

with open("fiche.txt", "r") as fichier:
    print (fichier.read())

with open("fiche.txt", 'r') as fichier:
    lignes = fichier.readlines()
    for ligne in lignes:
        print(ligne)            #Une fois sorti du bloc d'indentation, Python fermera automatiquement le fichier.



#ECRIRE DANS UN FICHIER
    
Il existe deux manières d’écrire dans un fichier.

#write(): insère la chaîne str1 sur une seule ligne dans le fichier texte.

    File_object.write (str1)

#writelines(): pour une liste d’éléments de chaîne, chaque chaîne est insérée dans le fichier texte.Utilisé pour insérer plusieurs chaînes à la fois.

    File_object.writelines (L) pour L = [str1, str2, str3] 

file1 = open("fiche.txt","w") 
L = ["manger Banane \n","couper Pasteque \n","boire eau \n"]  
  
file1.write("Hello \n")  
file1.writelines(L) 
file1.close() 

#LIRE A PARTIR D'UN FICHIER

Python lit le contenu d'un fichier sous forme de chaînes de caractères .
Il existe trois façons de lire des données à partir d’un fichier texte:

#read(): renvoie les octets lus sous forme de chaîne. Lit n octets, si aucun n n’est spécifié, lit le fichier entier.

    File_object.read ([n])

#readline(): Lit une ligne du fichier et retourne sous la forme d’une chaîne. Pour n spécifié, lit au plus n octets. Cependant, ne lit pas plus d’une ligne, même si n dépasse la longueur de la ligne.

    File_object.readline ([n])

Pour lire toutes les ligne ligne par ligne dans un fichier j'usqu'a la fin en utilsant readline() on peut faire:
fichier = open('fiche.txt', 'r')
ligne=fichier.readline()
while ligne:
    print(ligne)
    ligne=fichier.readline()

#readlines(): Lit toutes les lignes et les renvoie comme chaque ligne un élément de chaîne dans une liste.

      File_object.readlines()
file1 = open("fiche.txt","r")  
print ("Output of Read function is ")
print (file1.read())
  
file1.seek(0)  
print ("Output of Readline function is ")
print (file1.readline()) 
  
file1.seek(0)   
print ("Output of Read(9) function is ")
print (file1.read(9))
  
file1.seek(0)  
print ("Output of Readline(9) function is ")
print (file1.readline(9)) 
  
file1.seek(0) 
print ("Output of Readlines function is ")
print (file1.readlines()) 

file1.close()  



#LA METHODE SEEK en python()

En Python, la seek()fonction est utilisée pour changer la position du descripteur de fichier à une position spécifique donnée.
La poignée de fichier est comme un curseur, qui définit à partir de laquelle les données doivent être lues ou écrites dans le fichier.

    Syntaxe: f.seek (offset, from_what), où f est le pointeur de fichier
Paramètres:
    Offset: nombre de positions à partir de quoi avancer: il définit le point de référence.
    Renvoie: ne renvoie aucune valeur

Le point de référence est sélectionné par l’ argument from_what . Il accepte trois valeurs:

    0: définit le point de référence au début du fichier
    1: définit le point de référence à la position actuelle du fichier
    2: définit le point de référence à la fin du fichier

Par défaut, l’argument from_what est défini sur 0.

Noter: point de référence à la position actuelle / à la fin du fichier ne peut pas être défini en mode texte sauf lorsque le décalage est égal à 0.

#Exemple 1: Supposons que nous devions lire un fichier nommé «data.txt» :
f = open("fiche.txt", "r") 
  
f.seek(10) 
  
print(f.tell()) 
  
print(f.readline())  
f.close() 

#TELL() méthode:

Les modes d’accès régissent le type d’opérations possibles dans le fichier ouvert. Il fait référence à la manière dont le fichier sera utilisé une fois ouvert.
Ces modes définissent également l’emplacement du descripteur de fichier dans le fichier. Le descripteur de fichier est comme un curseur,
qui définit d’où les données doivent être lues ou écrites dans le fichier. Parfois, il devient important pour nous de connaître la position du fichier Hanlde.
tell() peut être utilisée pour obtenir la position du descripteur de fichier. tell()La méthode retourne la position actuelle de l’objet fichier.
Cette méthode ne prend aucun paramètre et renvoie une valeur entière.
Initialement, le pointeur de fichier pointe vers le début du fichier (s’il n’est pas ouvert en mode ajout). Ainsi, la valeur initiale de tell()est zéro.

syntaxe: file_object.tell()
f = open("fiche.txt", "r") 
  
f.seek(10) 
  
print(f.readline())  
f.close() 

#LA FONCTION TRUNCATE()
La méthode tronque la taille du fichier. Si l’argument de taille facultatif est présent, le fichier est tronqué à (au plus) cette taille.
La taille par défaut est la position actuelle. La position actuelle du fichier n’est pas modifiée. Notez que si une taille spécifiée dépasse la taille actuelle
du fichier, le résultat dépend de la plate-forme: les possibilités incluent que le fichier peut rester inchangé, augmenter jusqu’à la taille spécifiée comme s’il
était rempli de zéro ou augmenter jusqu’à la taille spécifiée avec un nouveau contenu non défini.
Pour tronquer le fichier, vous pouvez ouvrir le fichier en mode ajout ou en mode écriture.

Syntaxe: fileObject.truncate (taille)

#Exemple: soit le fichier de taille suivante:

size: 4.01 kb (4,113 bytes)
size on disk: 8.00 kb (8,192 bytes)

Modifions la taille du fichier à 100 octets.
fp = open('file1.txt', 'w')

fp.truncate(100)         #size: 4.01 kb (4,113 bytes)
                         #size on disk: 8.00 kb (8,192 bytes)
fp.close()

# we can use truncate() to delete the entire context of texte file
with open ('file1.txt' , 'w') as fichier:
    fichier.write("python")

fichier=open('file1.txt','r+')
print(fichier.truncate())

fichier=open('test.txt','r')

#w+ , a+ , r+ sont des modes d'ouverture de le fonction open . the + adds either reading or writing to an existing open mode, so all means reading and writing file.














