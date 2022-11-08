import platform

#platform.platform(aliased=0, terse=0)
"""
Renvoie une chaîne de caractère identifiant la plateforme avec le plus d’informations possible.
Si aliased est vrai, la fonction utilisera des alias pour certaines plateformes qui utilisent des noms de système qui diffèrent de leurs noms communs. Par exemple, SunOS sera reconnu comme Solaris. La fonction system_alias() est utilisée pour l’implémentation.
Si terse est vrai, la fonction ne renverra que l’information nécessaire à l’identification de la plateforme.
"""
print('Platform information:', platform.platform())  #Windows-10-10.0.19044-SP0

#platform.machine()       renvoie le type de machine et renvoie une chaine de caractere vide si la valeur ne peut etre determinee
print('Machine type:', platform.machine()) #Machine type: AMD64


#platform.processor()        Renvoie le (vrai) nom du processeur. 
print('Platform processor:', platform.processor())    #Intel64 Family 6 Model 78 Stepping 3, GenuineIntel

#platform.system()   renvoie le nom du systeme d'exploitation
print('Operating system:', platform.system())       #Windows

#platform.python_implementation()          Renvoie une chaîne de caractères identifiant l’implémentation de Python. Des valeurs possibles sont : CPython, IronPython, Jython, Pypy. 
print(platform.python_implementation())        #CPython

#platform.python_version()       Renvoie la version de Python comme une chaîne de caractères 'major.minor.patchlevel'.
print(platform.python_version())         #3.10.2

#platform.python_version_tuple()     Renvoie la version de Python comme un triplet de chaînes de caractères (major, minor, patchlevel).
print(platform.python_version_tuple())       #('3', '10', '2')
    
#platform.version()      Renvoie la version de déploiement du système.
print(platform.version())            #10.0.19044


#platform.architecture()  retourne le tuple (bits, linkage)
print(platform.architecture())  #('64bit', 'WindowsPE')


#platform.node()   renvoie le nom d'utilisateur sur le reseau
print("System's network name:", platform.node())  #DESKTOP-K75I9TV


#platform.python_build()         Renvoie une paire (buildno, builddate) de chaîne de caractères identifiant la version et la date de compilation de Python.
print(platform.python_build())        #('tags/v3.10.2:a58ebcc', 'Jan 17 2022 14:12:15')

#platform.python_compiler()    Renvoie une chaîne de caractères identifiant le compilateur utilisé pour compiler Python.
print(platform.python_compiler())      #MSC v.1929 64 bit (AMD64)

#platform.python_branch()    Renvoie la chaîne de caractères identifiant la branche du gestionnaire de versions de l’implémentation Python.
print(platform.python_branch())       #tags/v3.10.2


#platform.python_revision()     Renvoie la chaîne de caractères identifiant la révision du gestionnaire de versions de l’implémentation Python.
print(platform.python_revision())        #a58ebcc


#platform.release()        Renvoie la version de déploiement du système, par exemple, '2.2.0' ou 'NT'.
print(platform.release())          #10



#platform.system()   retourne le nom du systeme d'exploitation
print(platform.system())         #Windows

#platform.system_alias(system, release, version)         Renvoie (system, release, version) avec des alias pour les noms communs de certains systèmes.
print(platform.system_alias)          #<function system_alias at 0x000001B138E05000>


#platform.uname()       Renvoie un namedtuple() contenant six attributs : system, node, release, version, machine et processor.
print(platform.uname())           #uname_result(system='Windows', node='DESKTOP-K75I9TV', release='10', version='10.0.19044', machine='AMD64')

    
#Plateforme Java        Version de l’interface pour Jython. 
print(platform.java_ver())    #('', '', ('', '', ''), ('', '', ''))

#Plateforme Windows          Interroge le registre Windows pour de l’information supplémentaire et renvoie un triplet de (release, version, csd, ptype) faisant référence au numéro de version du SE, le numéro de version, le niveau de CSD (Service Pack) et le type de SE (monoprocesseur ou multiprocesseur).
print(platform.win32_ver())    #('10', '10.0.19044', 'SP0', 'Multiprocessor Free')

#Win95/98 specific
print(platform.popen())     #AttributeError: module 'platform' has no attribute 'popen'  donc la fct nexiste plus dans le module platform.

#Plateforme Mac OS       Renvoie les informations de version de Mac OS avec un triplet de (release, versioninfo, machine) 
print(platform.mac_ver())        #('', ('', '', ''), '')

#Plateformes Unix
print(platform.dist())
"""
This is another name for linux_distribution().

AttributeError: module 'platform' has no attribute 'dist'
"""

print(platform.linux_distribution())
"""
Tries to determine the name of the Linux OS distribution name.

AttributeError: module 'platform' has no attribute 'linux_distribution'
"""

print(platform.libc_ver((executable=sys.executable, lib='', version='', chunksize=16384)))         #('', '')
"""
Tente d’identifier la version de la bibliothèque standard C à laquelle le fichier exécutable (par défaut l’interpréteur Python) est lié.
Renvoie une paire de chaînes de caractères (lib, version). Les valeurs passées en paramètre seront retournées si la recherche échoue.
"""













    
