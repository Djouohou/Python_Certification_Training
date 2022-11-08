#Bytes, Bytearray
Python supports a range of types to store sequences. There are six sequence types: strings, byte sequences (bytes objects), byte arrays (bytearray objects), lists,
tuples, and range objects.

Strings contain Unicode characters. Their literals are written in single or double quotes : 'python', "data". Bytes and bytearray objects contain single bytes – the
former is immutable while the latter is a mutable sequence. Bytes objects can be constructed the constructor, bytes(), and from literals; use a b prefix with normal
string syntax: b'python'. To construct byte arrays, use the bytearray() function.

#Bytes literals
bytesliteral   ::=  bytesprefix(shortbytes | longbytes)
bytesprefix    ::=  "b" | "B" | "br" | "Br" | "bR" | "BR"
shortbytes     ::=  "'" shortbytesitem* "'" | '"' shortbytesitem* '"'
longbytes      ::=  "'''" longbytesitem* "'''" | '"""' longbytesitem* '"""'
shortbytesitem ::=  shortbyteschar | bytesescapeseq
longbytesitem  ::=  longbyteschar | bytesescapeseq
shortbyteschar ::=  <any ASCII character except "\" or newline or the quote>
longbyteschar  ::=  <any ASCII character except "\">
bytesescapeseq ::=  "\" <any ASCII character>

bytes() and bytearray() functions

bytes() function:
Return a new "bytes" object, which is an immutable sequence of small integers in the range 0 <= x < 256, print as ASCII characters when displayed.
bytes is an immutable version of bytearray – it has the same non-mutating methods and the same indexing and slicing behavior.

Syntax: bytes([source[, encoding[, errors]]])

bytearray() function :
Return a new array of bytes. The bytearray type is a mutable sequence of integers in the range 0 <= x < 256. It has most of the usual methods of mutable sequences,
described in Mutable Sequence Types, as well as most methods that the bytes type has, see Bytes and Byte Array Methods.

Syntax: bytearray([source[, encoding[, errors]]])
The optional source parameter can be used to initialize the array in a few different ways:

    If it is a string, you must also give the encoding (and optionally, errors) parameters; bytearray() then converts the string to bytes using str.encode().
    If it is an integer, the array will have that size and will be initialized with null bytes.
    If it is an object conforming to the buffer interface, a read-only buffer of the object will be used to initialize the bytes array.
    If it is iterable, it must be an iterable of integers in the range 0 <= x < 256, which are used as the initial contents of the array.

Without an argument, an array of size 0 is created.




# La Fonction BYTEARRAY() En Python
"""
La fonction bytearray() renvoie un objet bytearray qui est un tableau d’octets donnés. Il donne une séquence mutable d’entiers dans la plage 0 <= x < 256.
Si vous voulez la version immuable, utilisez la méthode bytes().
Syntaxe: bytearray([source[, encodage[, erreurs]]])
 
Paramètres: La fonction bytearray() prend trois paramètres facultatifs:
    source(facultatif) : Source pour initialiser le tableau d’octets.
    encodage(facultatif) : Si la source est une chaîne, l’encodage de la chaîne.
    erreurs(facultatif) : Si la source est une chaîne, l’action à entreprendre lorsque la conversion de codage échoue.
 
Valeur de retour: La fonction bytearray() renvoie un tableau d’octets.
"""
string = "je fais mes tests"
tableau = bytearray(string, 'utf-8')   #si on teste cette chaine sans encodage on aura une erreur:: TypeError: string argument without an encoding
print(tableau)    #bytearray(b'je fais mes tests')

#exemple: un Iterable (plage 0 <= x <256), utilisé comme contenu initial du tableau.
liste = [1, 2, 3]
tab = bytearray(liste)
print(tab)               #bytearray(b'\x01\x02\x03')        


#exemple: If a string, must provided encoding and errors parameters, bytearray() converts the string to bytes using str.encode()

string = "testeurs"
# encoding the string with unicode 8 and 16
array1 = bytearray(string, 'utf-8')
array2 = bytearray(string, 'utf-16')
  
print(array1)      #bytearray(b'testeurs')
print(array2)      #bytearray(b'\xff\xfet\x00e\x00s\x00t\x00e\x00u\x00r\x00s\x00')


#exemple: If an integer, creates an array of that size and initialized with null bytes.

# size of array
size = 3 
# will create an array of given size 
# and initialize with null bytes
array1 = bytearray(size)
  
print(array1)      #bytearray(b'\x00\x00\x00') 


#exemple: If an Object, read-only buffer will be used to initialize the bytes array.

# Creates bytearray from byte literal
arr1 = bytearray(b"abcd") 
# iterating the value
for value in arr1:
    print(value)
"""
97
98
99
100
"""
      
# Create a bytearray object
arr2 = bytearray(b"aaaacccc")
# count bytes from the buffer
print("Count of c is:", arr2.count(b"c"))         #Count of c is: 4


#exemple: If an Iterable(range 0<= x < 256), used as the initial contents of an array.

# simple list of integers
list = [1, 2, 3, 4] 
# iterable as source
array = bytearray(list)  
print(array)   #bytearray(b'\x01\x02\x03\x04')
print("Count of bytes:", len(array))    #Count of bytes: 4


#exemple: If No source, an array of size 0 is created.

# array of size o will be created 
# iterable as source
array = bytearray()  
print(array)     #bytearray(b'')



#LA FONCTION BYTES() en Python

La fonction bytes() renvoie un objet de type bytes. Il peut convertir des objets en objets de type bytes ou créer un objet vide de type bytes d’une taille spécifiée.
bytes() convertit un objet en objet représenté par octets immuable de taille et de données données.
#La différence entre bytes() et bytearray() est que bytes() renvoie un objet qui ne peut pas être modifié et bytearray() retourne un objet qui peut être modifié. 
Le type bytes fait partie des types dits de séquence. Il permet de traiter les chaines d’octets.

Syntaxe: bytes([source[, encodage[, erreurs]]])
Paramètres: La fonction bytes() prend trois paramètres facultatifs:
    source(facultatif) : Source pour initialiser le tableau d’octets.
    encodage(facultatif) : Si la source est une chaîne, l’encodage de la chaîne.
    erreurs(facultatif) : Si la source est une chaîne, l’action à entreprendre lorsque la conversion de codage échoue.

Valeur de retour: La fonction bytes() renvoie un objet de type bytes.
Renvoie: Byte objet immuable composé de caractères Unicode 0-256 selon le type source.
integer: retourne un tableau de taille initialisée à null
iterable: retourne un tableau de taille itérable avec des éléments égaux aux éléments itérables (0-256)
string: renvoie la chaîne codée acc. à enc et si le codage échoue, exécute l’action selon erreur spécifié.
aucun argument: renvoie un tableau de taille 0. 

#exemple: démonstration d’octet() sur les entiers, aucun argument et les itérables

a = 4
lis1 = [1, 2, 3, 4, 5] 
  
print ("Byte conversion with no arguments : " + str(bytes()))  #Byte conversion with no arguments : b''

print ("The integer conversion results in : "  + str(bytes(a)))   #The integer conversion results in : b'\x00\x00\x00\x00'
print ("The iterable conversion results in : "  + str(bytes(lis1)))   #The iterable conversion results in : b'\x01\x02\x03\x04\x05'

#Comportement des octets avec des chaînes

Les octets acceptent la chaîne comme argument et nécessitent un schéma de codage pour l’exécuter. L’aspect le plus important de ceci est la gestion des erreurs
en cas d’échec de codage, certains des schémas de gestion des erreurs définis sont:
    Gestionnaires d’erreurs de chaîne:
    strict: déclenche l’erreur UnicodeDecodeError par défaut en cas d’échec de l’encodage.
    ignore: ignore le caractère non codable et encode la chaîne restante.
    replace: remplace le caractère non codable par un «?».

#exemple: démonstration d’octets() en utilisant la chaîne

  
str1 = 'GeeksfÖrGeeks'
  
print ("Byte conversion with ignore error : " +
      str(bytes(str1, 'ascii', errors = 'ignore')))   #Byte conversion with ignore error : b'GeeksfrGeeks'  normalement ca genere une erreur car ascii ne reconnait pas
                                                      le Ö mais comme on a entree en parametre ignore lerreur, alors le resultat va juste ignorer ce caractere.
  
print ("Byte conversion with replace error : " +
      str(bytes(str1, 'ascii', errors = 'replace')))   #Byte conversion with replace error : b'Geeksf?rGeeks'
  
print ("Byte conversion with strict error : " +
      str(bytes(str1, 'ascii', errors = 'strict')))     Traceback (most recent call last):
                                                        File "C:\Users\Ingrid\Desktop\COURS PROGRAMME\Course Level PCAP\Prog.py", line 23, in <module>
                                                        str(bytes(str1, 'ascii', errors = 'strict')))
                                                        UnicodeEncodeError: 'ascii' codec can't encode character '\xd6' in position 6: ordinal not in range(128)


#exemple
string = "je fais mes tests"
tableau = bytes(string, 'utf-8')
print(tableau)        #b'je fais mes tests'

#exemple: Exemple 2: L’exemple suivant renvoie un tableau de 4 octets:
size = 4
tab = bytes(size)
print(tab)       #b'\x00\x00\x00\x00'



#LE MODULE IO EN PYTHON: Core tools for working with streams

"""
io est un module qui permet de gérer des flux d’entrées et de sorties, que ce soit pour écrire avec des données en byte(string) ou avec des données en binaire.
io est le module par défaut pour gérer les flux et les fichiers en python 3.


The io module provides Python’s main facilities for dealing with various types of I/O. There are three main types of I/O: text I/O, binary I/O and raw I/O.
These are generic categories, and various backing stores can be used for each of them. A concrete object belonging to any of these categories is called a file object.

Tous les flux sont attentifs au type de données que vous leur fournissez. Par exemple, si vous donnez un objet str à la méthode write() d'un flux\stream binaire, vous
obtiendrez un TypeError. Il en va de même pour un objet bytes à la méthode write() d'un flux\stream de texte.

Changed in version 3.3: Operations that used to raise IOError now raise OSError, since IOError is now an alias of OSError.
"""

#TEXT I/O        The text stream API is described in detail in TextIOBase.
L'E/S de texte attend et produit des objets str. Cela signifie que lorsque le backing store est nativement constitué d'octets (comme dans le cas d'un fichier),
l'encodage et le décodage des données sont effectués de manière transparente ainsi que la traduction optionnelle des caractères de nouvelle ligne spécifiques
à la plate-forme.
                                                                                                                               
The easiest way to create a text stream is with open(), optionally specifying an encoding:

f = open("fiche.txt", "r", encoding="utf-8")

In-memory text streams are also available as StringIO objects:

f = io.StringIO("some initial text data")

Accordingly, it is highly recommended that you specify the encoding explicitly when opening text files. If you want to use UTF-8, pass encoding="utf-8".
To use the current locale encoding, encoding="locale" is supported in Python 3.10.
                                                                                                                               

#BINARY I/O   The binary stream API is described in detail in BufferedIOBase
L'entrée/sortie binaire (également appelée entrée/sortie en mémoire tampon \buffered) attend des objets de type octet et produit des objets de type octet.
Aucun encodage, décodage ou traduction des nouvelles lignes n'est effectué. Cette catégorie de flux\stream peut être utilisée pour toutes sortes de données non text,
ainsi que lorsqu'un contrôle manuel de la manipulation des données text est souhaité.


The easiest way to create a binary stream is with open() with 'b' in the mode string:
                                                                                                                               
f = open("photo.jpg", "rb") #une image c'est aussi une sequence binaire.

In-memory binary streams are also available as BytesIO objects:

f = io.BytesIO(b"some initial binary data: \x00\x01")        #retourne un objet de type bytesIO. il existe stringIO et bytesIO qui sont des methode qui permettent de
                                                            manipuler les chaine de caracteres et les octets respectivement.
                                                                                                                       


#Raw I/O                  The raw stream API is described in detail in RawIOBase.

Raw I/O (also called unbuffered I/O) is generally used as a low-level building-block for binary and text streams; it is rarely useful to directly manipulate a
raw stream from user code. Nevertheless, you can create a raw stream by opening a file in binary mode with buffering disabled:

Les E/S brutes (également appelées E/S sans tampon) sont généralement utilisées comme un bloc de construction de bas niveau pour les flux binaires et textuels ;
il est rarement utile de manipuler directement un flux brut à partir du code utilisateur. Néanmoins, vous pouvez créer un flux brut en ouvrant un fichier en mode
binaire avec la mise en mémoire tampon désactivée :

f = open("myfile.jpg", "rb", buffering=0)



#HIGH-LEVEL MODULE INTERFACE
                                                                                                                               
NB: le fichier 'fiche.txt' pris dans les exemples contient le texte suivants:

Hello 
This is python 
This is my txt file
This is a test file

#io.DEFAULT_BUFFER_SIZE

    An int containing the default buffer size used by the module’s buffered I/O classes.
import io
print(io.DEFAULT_BUFFER_SIZE)    #8192                                                                                                                       
                                                                                                                               

#io.open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
"""
    This is an alias for the builtin open() function.
    This function raises an auditing event open with arguments path, mode and flags.
    The mode and flags arguments may have been modified or inferred(déduit) from the original call.
"""
import io
print(io.open("fiche.txt", mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None))  #<_io.TextIOWrapper name='fiche.txt' mode='r' encoding='cp1252'>

fichier=io.open("fiche.txt", mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
print(fichier.read())       #le contenu du fichier est effectivement lu


#io.open_code(path)
"""
    Ouvre le fichier fourni avec le mode 'rb'. Cette fonction doit être utilisée lorsque l'intention est de traiter le contenu comme un code exécutable.
    path should be a str and an absolute path.
"""
import io
f=io.open_code('fiche.txt')
print(f.read())          #b'Hello \r\nThis is python \r\nThis is my txt file\r\nThis is a test file\r\n'


#io.text_encoding(encoding, stacklevel=2, /)
"""
    This is a helper function for callables that use open() or TextIOWrapper and have an encoding=None parameter.
    This function returns encoding if it is not None and "locale" if encoding is None.
    This function emits an EncodingWarning if sys.flags.warn_default_encoding is true and encoding is None. stacklevel specifies where the warning is emitted. 
"""
import io
print(io.text_encoding('utf-8'))       #utf-8
print(io.text_encoding(None))        #locale


def read_text(path, encoding=None):
    encoding = io.text_encoding(encoding)  # stacklevel=2
    with open(path, encoding) as f:
        return f.read()                                  #In this example, an EncodingWarning is emitted for the caller of read_text().Car l'encoding est NONE.

read_text('fiche.txt', encoding)          Traceback (most recent call last):
                                            File "C:\Users\Ingrid\Desktop\COURS PROGRAMME\Course Level PCAP\Prog.py", line 21, in <module>
                                             read_text('fiche.txt')
                                            File "C:\Users\Ingrid\Desktop\COURS PROGRAMME\Course Level PCAP\Prog.py", line 18, in read_text
                                            with open(path, encoding) as f:
                                           ValueError: invalid mode: 'locale'



#exception io.BlockingIOError
"""
    This is a compatibility alias for the builtin BlockingIOError exception.
"""
import io
print(io.BlockingIOError)       #<class 'BlockingIOError'>



#exception io.UnsupportedOperation
"""
    An exception inheriting OSError and ValueError that is raised when an unsupported operation is called on a stream.
"""
import io
print(io.UnsupportedOperation)       #<class 'io.UnsupportedOperation'>



#CLASS HIERARCHY 
"""
The implementation of I/O streams is organized as a hierarchy of classes. First abstract base classes (ABCs), which are used to specify the various categories of
streams, then concrete classes providing the standard stream implementations.

Au sommet de la hiérarchie des E/S se trouve la classe de base abstraite IOBase. Elle définit l'interface de base d'un flux. Notez, cependant,
qu'il n'y a pas de séparation entre la lecture et l'écriture dans les flux ; 

L'ABC RawIOBase étend IOBase. Elle traite de la lecture et de l'écriture d'octets dans un flux. 

La BufferedIOBase ABC étend IOBase. Il traite de la mise en mémoire tampon sur un flux binaire brut (RawIOBase). 

La sous-classe TextIOBase ABC étend IOBase. Elle traite les flux dont les octets représentent du texte, et gère l'encodage et le décodage vers et depuis
des chaînes de caractères.

Les noms des arguments ne font pas partie de la spécification, et seuls les arguments de open() sont destinés à être utilisés comme arguments de mots-clés.
"""

#CLASS io.IOBase
"""
Cette classe fournit des implémentations abstraites vides pour de nombreuses méthodes que les classes dérivées peuvent surcharger sélectivement ;
les implémentations par défaut représentent un fichier qui ne peut pas être lu, écrit ou recherché.

Même si IOBase ne déclare pas read() ou write() parce que leurs signatures varient, les implémentations et les clients doivent considérer ces méthodes comme faisant
partie de l'interface. De plus, les implémentations peuvent soulever une ValueError (ou UnsupportedOperation) lorsque des opérations qu'elles ne supportent pas sont
appelées.

Le type de base utilisé pour les données binaires lues ou écrites dans un fichier est l'octet. D'autres objets de type octet sont également acceptés comme arguments
de méthode. Les classes d'E/S de texte fonctionnent avec des données de type str.
"""
with open('spam.txt', 'w') as file:
    file.write('Spam and eggs!')         #ici cree le fichier spam et ecrit le texte 'spam and eggs' à l'interieur

with open('fiche.txt', 'r') as inputStream:
    with open('output.txt', 'w') as op:
        op.write(inputStream.read(10))  #ici prend les 10 premier caractere du texte contenu dans 'fiche' et les copie dans 'output' qui s'est creé automatiquement.


IOBase provides these data attributes and methods:


#close()

    Flush and close this stream. This method has no effect if the file is already closed. Once the file is closed, any operation on the file (e.g. reading or writing)
    will raise a ValueError. As a convenience, it is allowed to call this method more than once; only the first call, however, will have an effect.

#closed         Returns True if the stream is closed.

   import io
f=open('fiche.txt', 'r')
print(f.closed)  #False

f=open('fiche.txt', 'r')
f.close
print(f.closed)  #True
 

#fileno()   Return the underlying file descriptor (an integer) of the stream if it exists. An OSError is raised if the IO object does not use a file descriptor.

#flush()     Vide le flux d’écriture, ne fait rien en lecture.

    Flush the write buffers of the stream if applicable. This does nothing for read-only and non-blocking streams.

#isatty()    Retourne True si le flux est connecté à un terminal.

    Return True if the stream is interactive (i.e., connected to a terminal/tty device).

#readable()   Retourne True si on peut lire depuis le flux. Si False, read() lève une exception OSError.

    Return True if the stream can be read from. If False, read() will raise OSError.

#readline(size=- 1, /)

    Read and return one line from the stream. If size is specified, at most size bytes will be read.
    The line terminator is always b'\n' for binary files; for text files, the newline argument to open() can be used to select the line terminator(s) recognized.

#readlines(hint=- 1, /)

    Read and return a list of lines from the stream. hint can be specified to control the number of lines read: no more lines will be read if the total
    size (in bytes/characters) of all lines so far exceeds hint.

    hint values of 0 or less, as well as None, are treated as no hint.

    Note that it’s already possible to iterate on file objects using for line in file: ... without calling file.readlines().

#seek(offset, whence=SEEK_SET, /)       Return the new absolute position.

    Change the stream position to the given byte offset. offset is interpreted relative to the position indicated by whence. The default value for whence is SEEK_SET. Values for whence are:

        SEEK_SET or 0 – start of the stream (the default); offset should be zero or positive

        SEEK_CUR or 1 – current stream position; offset may be negative

        SEEK_END or 2 – end of the stream; offset is usually negative


#seekable()

    Return True if the stream supports random access. If False, seek(), tell() and truncate() will raise OSError.

#tell()

    Return the current stream position.

#truncate(size=None, /)

    Resize the stream to the given size in bytes (or the current position if size is not specified). The current stream position isn’t changed. This resizing can extend or reduce the current file size. In case of extension, the contents of the new file area depend on the platform (on most systems, additional bytes are zero-filled). The new file size is returned.

    Changed in version 3.5: Windows will now zero-fill files when extending.

#writable() Retourne True si on peut écrire depuis le flux. Si False, write() lève une exception OSError.

    Return True if the stream supports writing. If False, write() and truncate() will raise OSError.

#writelines(lines, /)

    Write a list of lines to the stream. Line separators are not added, so it is usual for each of the lines provided to have a line separator at the end.

#__del__()

    Prepare for object destruction. IOBase provides a default implementation of this method that calls the instance’s close() method.



#CLASS io.RawIOBase
Base class for raw binary streams. It inherits IOBase.
RawIOBase provides these methods in addition to those from IOBase:


#read(size=- 1, /)

    Read up to size bytes from the object and return them. As a convenience, if size is unspecified or -1, all bytes until EOF are returned. Otherwise,
    only one system call is ever made. Fewer than size bytes may be returned if the operating system call returns fewer than size bytes.

    If 0 bytes are returned, and size was not 0, this indicates end of file. If the object is in non-blocking mode and no bytes are available, None is returned.

#readall()

    Read and return all the bytes from the stream until EOF(End Of File), using multiple calls to the stream if necessary.

#readinto(b, /)

    Read bytes into a pre-allocated, writable bytes-like object b, and return the number of bytes read. For example, b might be a bytearray.
    If the object is in non-blocking mode and no bytes are available, None is returned.

#write(b, /)

    Write the given bytes-like object, b, to the underlying raw stream, and return the number of bytes written. This can be less than the length of b in bytes,
    depending on specifics of the underlying raw stream, and especially if it is in non-blocking mode. None is returned if the raw stream is set not to block and
    no single byte could be readily written to it. 



#CLASS io.BufferedIOBase

    Base class for binary streams that support some kind of buffering. It inherits IOBase.

    The main difference with RawIOBase is that methods read(), readinto() and write() will try (respectively) to read as much input as requested or to consume all
    given output, at the expense of making perhaps more than one system call.

    In addition, those methods can raise BlockingIOError if the underlying raw stream is in non-blocking mode and cannot take or give enough data; unlike
    their RawIOBase counterparts, they will never return None.

    BufferedIOBase provides or overrides these data attributes and methods in addition to those from IOBase:
        
#raw

    The underlying raw stream (a RawIOBase instance) that BufferedIOBase deals with.
    This is not part of the BufferedIOBase API and may not exist on some implementations.

#detach()

    Separate the underlying raw stream from the buffer and return it.
    After the raw stream has been detached, the buffer is in an unusable state.
    Some buffers, like BytesIO, do not have the concept of a single raw stream to return from this method. They raise UnsupportedOperation.

#read(size=- 1, /)

    Read and return up to size bytes. If the argument is omitted, None, or negative, data is read and returned until EOF is reached.
    An empty bytes object is returned if the stream is already at EOF.
    If the argument is positive, and the underlying raw stream is not interactive, multiple raw reads may be issued to satisfy the byte count
    (unless EOF is reached first). But for interactive raw streams, at most one raw read will be issued, and a short result does not imply that EOF is imminent.
    A BlockingIOError is raised if the underlying raw stream is in non blocking-mode, and has no data available at the moment.

#read1(size=- 1, /)

    Read and return up to size bytes, with at most one call to the underlying raw stream’s read() (or readinto()) method.
    If size is -1 (the default), an arbitrary number of bytes are returned (more than zero unless EOF is reached).

#readinto(b, /)
    Read bytes into a pre-allocated, writable bytes-like object b and return the number of bytes read. For example, b might be a bytearray.
    Like read(), multiple reads may be issued to the underlying raw stream, unless the latter is interactive.
    A BlockingIOError is raised if the underlying raw stream is in non blocking-mode, and has no data available at the moment.

#readinto1(b, /)

    Read bytes into a pre-allocated, writable bytes-like object b, using at most one call to the underlying raw stream’s read() (or readinto()) method.
    Return the number of bytes read.
    A BlockingIOError is raised if the underlying raw stream is in non blocking-mode, and has no data available at the moment.

#write(b, /)
    Write the given bytes-like object, b, and return the number of bytes written (always equal to the length of b in bytes, since if the write fails an OSError
    will be raised). Depending on the actual implementation, these bytes may be readily written to the underlying stream, or held in a buffer for performance and
    latency reasons.
    When in non-blocking mode, a BlockingIOError is raised if the data needed to be written to the raw stream but it couldn’t accept all the data without blocking.



#RAW FILE I/O

class io.FileIO(name, mode='r', closefd=True, opener=None)

    A raw binary stream representing an OS-level file containing bytes data. It inherits RawIOBase.
    
    The mode can be 'r', 'w', 'x' or 'a' for reading (default), writing, exclusive creation or appending. The file will be created if it doesn’t exist when opened
    for writing or appending; it will be truncated when opened for writing. FileExistsError will be raised if it already exists when opened for creating.
    Opening a file for creating implies writing, so this mode behaves in a similar way to 'w'. Add a '+' to the mode to allow simultaneous reading and writing.

    The read() (when called with a positive argument), readinto() and write() methods on this class will only make one system call.
    The newly created file is non-inheritable.

    FileIO provides these data attributes in addition to those from RawIOBase and IOBase:

#mode   The mode as given in the constructor.

#name   The file name. This is the file descriptor of the file when no name is given in the constructor.



#BUFFERED STREAMS 

Buffered I/O streams provide a higher-level interface to an I/O device than raw I/O does.

#CLASS io.BytesIO(initial_bytes=b'')

    A binary stream using an in-memory bytes buffer. It inherits BufferedIOBase. The buffer is discarded(la mémoire tampon est rejetée) when the close() method is called.
    The optional argument initial_bytes is a bytes-like object that contains initial data.

    BytesIO provides or overrides these methods in addition to those from BufferedIOBase and IOBase:

#getbuffer()   Note :As long as the view exists, the BytesIO object cannot be resized or closed.
Return a readable and writable view over the contents of the buffer without copying them. Also, mutating the view will transparently update the contents of the buffer:

import io
b = io.BytesIO(b"abcdef")
view = b.getbuffer()
view[2:4] = b"56"
print(b.getvalue())     #b'ab56ef'

#getvalue()    Return bytes containing the entire contents of the buffer.

#read1(size=- 1, /)        In BytesIO, this is the same as read().

#readinto1(b, /)            In BytesIO, this is the same as readinto().



#CLASS io.BufferedReader(raw, buffer_size=DEFAULT_BUFFER_SIZE)

    A buffered binary stream providing higher-level access to a readable, non seekable RawIOBase raw binary stream. It inherits BufferedIOBase.

    When reading data from this object, a larger amount of data may be requested from the underlying raw stream, and kept in an internal buffer.
    The buffered data can then be returned directly on subsequent reads.
    The constructor creates a BufferedReader for the given readable raw stream and buffer_size. If buffer_size is omitted, DEFAULT_BUFFER_SIZE is used.

    BufferedReader provides or overrides these methods in addition to those from BufferedIOBase and IOBase:

#peek(size=0, /)
Return bytes from the stream without advancing the position. At most one single read on the raw stream is done to satisfy the call. The number of bytes returned
may be less or more than requested.

#read(size=- 1, /)         Read and return size bytes, or if size is not given or negative, until EOF or if the read call would block in non-blocking mode.

#read1(size=- 1, /)
Read and return up to size bytes with only one call on the raw stream. If at least one byte is buffered, only buffered bytes are returned. Otherwise, one raw stream
read call is made.


 
#CLASS io.BufferedWriter(raw, buffer_size=DEFAULT_BUFFER_SIZE)

    A buffered binary stream providing higher-level access to a writeable, non seekable RawIOBase raw binary stream. It inherits BufferedIOBase.

    When writing to this object, data is normally placed into an internal buffer. The buffer will be written out to the underlying RawIOBase object under various
    conditions, including:

        when the buffer gets too small for all pending data;

        when flush() is called;

        when a seek() is requested (for BufferedRandom objects);

        when the BufferedWriter object is closed or destroyed.

    The constructor creates a BufferedWriter for the given writeable raw stream. If the buffer_size is not given, it defaults to DEFAULT_BUFFER_SIZE.

    BufferedWriter provides or overrides these methods in addition to those from BufferedIOBase and IOBase:

#flush()     Force bytes held in the buffer into the raw stream. A BlockingIOError should be raised if the raw stream blocks.

#write(b, /)
Write the bytes-like object, b, and return the number of bytes written. When in non-blocking mode, a BlockingIOError is raised if the buffer needs to be written out
but the raw stream blocks.



#CLASS io.BufferedRandom(raw, buffer_size=DEFAULT_BUFFER_SIZE)

    A buffered binary stream providing higher-level access to a seekable RawIOBase raw binary stream. It inherits BufferedReader and BufferedWriter.
    The constructor creates a reader and writer for a seekable raw stream, given in the first argument. If the buffer_size is omitted itdefaults to DEFAULT_BUFFER_SIZE.
    BufferedRandom is capable of anything BufferedReader or BufferedWriter can do. In addition, seek() and tell() are guaranteed to be implemented.



#CLASS io.BufferedRWPair(reader, writer, buffer_size=DEFAULT_BUFFER_SIZE, /)
A buffered binary stream providing higher-level access to two non seekable RawIOBase raw binary streams—one readable, the other writeable.It inherits BufferedIOBase.
reader and writer are RawIOBase objects that are readable and writeable respectively. If the buffer_size is omitted it defaults to DEFAULT_BUFFER_SIZE.




#TEXT I/O

#CLASS io.TextIOBase
    Base class for text streams. This class provides a character and line based interface to stream I/O. It inherits IOBase.

    TextIOBase provides or overrides these data attributes and methods in addition to those from IOBase:

    #encoding     The name of the encoding used to decode the stream’s bytes into strings, and to encode strings into bytes.

    #errors     The error setting of the decoder or encoder.

    #newlines     A string, a tuple of strings, or None, indicating the newlines translated so far. 

    #buffer   The underlying binary buffer (a BufferedIOBase instance) that TextIOBase deals with.

    #detach()    Separate the underlying binary buffer from the TextIOBase and return it.

    #read(size=- 1, /)      Read and return at most size characters from the stream as a single str. If size is negative or None, reads until EOF.

    #readline(size=- 1, /)
    Read until newline or EOF and return a single str. If the stream is already at EOF, an empty string is returned.
    If size is specified, at most size characters will be read.

    #seek(offset, whence=SEEK_SET, /     Return the new absolute position as an opaque number.
    Change the stream position to the given offset. Behaviour depends on the whence parameter. The default value for whence is SEEK_SET.

        SEEK_SET or 0: seek from the start of the stream (the default); offset must either be a number returned by TextIOBase.tell(), or zero. Any other offset
        value produces undefined behaviour.

        SEEK_CUR or 1: “seek” to the current position; offset must be zero, which is a no-operation (all other values are unsupported).

        SEEK_END or 2: seek to the end of the stream; offset must be zero (all other values are unsupported).

    #tell()     Return the current stream position as an opaque number. The number does not usually represent a number of bytes in the underlying binary storage.

    #write(s, /)    Write the string s to the stream and return the number of characters written.


#CLASS io.TextIOWrapper(buffer, encoding=None, errors=None, newline=None, line_buffering=False, write_through=False)

    A buffered text stream providing higher-level access to a BufferedIOBase buffered binary stream. It inherits TextIOBase.

    encoding gives the name of the encoding that the stream will be decoded or encoded with. It defaults to locale.getpreferredencoding(False).
    encoding="locale" can be used to specify the current locale’s encoding explicitly. See Text Encoding for more information.

    errors is an optional string that specifies how encoding and decoding errors are to be handled. Pass 'strict' to raise a ValueError exception if there is
    an encoding error (the default of None has the same effect), or pass 'ignore' to ignore errors. (Note that ignoring encoding errors can lead to data loss.)
    'replace' causes a replacement marker (such as '?') to be inserted where there is malformed data. 'backslashreplace' causes malformed data to be replaced by
    a backslashed escape sequence. When writing, 'xmlcharrefreplace' (replace with the appropriate XML character reference) or 'namereplace'
    (replace with \N{...} escape sequences) can be used. Any other error handling name that has been registered with codecs.register_error() is also valid.

    newline controls how line endings are handled. It can be None, '', '\n', '\r', and '\r\n'. It works as follows:

    If line_buffering is True, flush() is implied when a call to write contains a newline character or a carriage return.

    If write_through is True, calls to write() are guaranteed not to be buffered: any data written on the TextIOWrapper object is immediately handled to
    its underlying binary buffer.


    TextIOWrapper provides these data attributes and methods in addition to those from TextIOBase and IOBase:

    #line_buffering   Whether line buffering is enabled.

    #write_through     Whether writes are passed immediately to the underlying binary buffer.

    #reconfigure(*[, encoding][, errors][, newline][, line_buffering][, write_through])

        Reconfigure this text stream using new settings for encoding, errors, newline, line_buffering and write_through.
        Parameters not specified keep current settings, except errors='strict' is used when encoding is specified but errors is not specified.
 It is not possible to change the encoding or newline if some data has already been read from the stream. On the other hand, changing encoding after write is possible.


#CLASS io.StringIO(initial_value='', newline='\n')

    A text stream using an in-memory text buffer. It inherits TextIOBase.
    The text buffer is discarded when the close() method is called.
    The initial value of the buffer can be set by providing initial_value. If newline translation is enabled, newlines will be encoded as if by write().
    The stream is positioned at the start of the buffer.
    The newline argument works like that of TextIOWrapper, except that when writing output to the stream, if newline is None, newlines are written as \n on all platforms.

    StringIO provides this method in addition to those from TextIOBase and IOBase:

    #getvalue()    Return a str containing the entire contents of the buffer. Newlines are decoded as if by read(), although the stream position is not changed.


#CLASS io.IncrementalNewlineDecoder
    A helper codec that decodes newlines for universal newlines mode. It inherits codecs.IncrementalDecoder.





















































                             
