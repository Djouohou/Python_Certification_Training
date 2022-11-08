import sys

#sys.path
"""Une liste de chaînes de caractères spécifiant les chemins de recherche des modules, initialisée à partir de la variable d'environnement PYTHONPATH et
d'une valeur par défaut dépendante de l'installation.
"""
print(sys.path)
"""
['C:\\Users\\Ingrid\\Desktop\\COURS PROGRAMME\\Course Level PCAP', 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip',
'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\DLLs', 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib',
'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310', 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages']
"""

#sys.implementation           Un objet contenant des informations sur l'implémentation de la version actuelle de l'interpréteur Python.
print(sys.implementation)        #namespace(name='cpython', cache_tag='cpython-310', version=sys.version_info(major=3, minor=10, micro=2, releaselevel='final', serial=0), hexversion=50987760)


#(sys.executable)
"""
Renvoie une chaîne donnant le chemin absolu vers l'interpréteur Python, un fichier binaire exécutable, sur les système sur lesquels ça à du sens.
Si Python n'est pas capable de récupérer le chemin réel de son exécutable, sys.executable sera une chaîne vide ou None.
Renvoie donc la localisation du fichier python EXEcutable d'ou l'extention EXE à la fin du resultat sortie.
"""
print(sys.executable)  #C:\Users\Ingrid\AppData\Local\Programs\Python\Python310\pythonw.exe

#sys.exit([arg])      Raise a SystemExit exception, signaling an intention to exit the interpreter.

#sys.flags      renvoie la named tuple flags exposant l'état des options de ligne de commande
"""
sys.flags(debug=0, inspect=0, interactive=0, optimize=0, dont_write_bytecode=0, no_user_site=0, no_site=0, ignore_environment=0, verbose=0, bytes_warning=0,
quiet=0, hash_randomization=1, isolated=0, dev_mode=False, utf8_mode=0, warn_default_encoding=0)
"""


#sys.abiflags
print(sys.abiflags)  #AttributeError: module 'sys' has no attribute 'abiflags'

#sys.addaudithook(hook)

#sys.argv
"""
permet d'executer un script en indice de commande de windows.
permet de gerer les arguments de la ligne de commande
"""
print(sys.argv)      #['C:\\Users\\Ingrid\\Desktop\\COURS PROGRAMME\\Course Level PCAP\\Prog.py']
print(sys.argv[0])                     #C:\Users\Ingrid\Desktop\COURS PROGRAMME\Course Level PCAP\Prog.py
print(sys.argv[1])          #renvoie l'argument de l'index 1

#sys.audit(event, *args)

#sys.base_exec_prefix     
print(sys.base_exec_prefix)        #C:\Users\Ingrid\AppData\Local\Programs\Python\Python310
    
#sys.base_prefix
print(sys.base_prefix)           #C:\Users\Ingrid\AppData\Local\Programs\Python\Python310
    
#sys.byteorder
print(sys.byteorder)   #little

#sys.builtin_module_names
print(sys.builtin_module_names)
"""
('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_codecs_cn', '_codecs_hk', '_codecs_iso2022', '_codecs_jp', '_codecs_kr', '_codecs_tw', '_collections', '_contextvars',
'_csv', '_datetime', '_functools', '_heapq', '_imp', '_io', '_json', '_locale', '_lsprof', '_md5', '_multibytecodec', '_opcode', '_operator', '_pickle', '_random', '_sha1',
'_sha256', '_sha3', '_sha512', '_signal', '_sre', '_stat', '_statistics', '_string', '_struct', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', '_winapi',
'_xxsubinterpreters', 'array', 'atexit', 'audioop', 'binascii', 'builtins', 'cmath', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'math', 'mmap', 'msvcrt',
'nt', 'sys', 'time', 'winreg', 'xxsubtype', 'zlib')
"""
    
#sys.call_tracing(func, args)

#sys.copyright
print(sys.copyright)
"""
Copyright (c) 2001-2022 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.
"""
    
#sys._clear_type_cache() vide le cache interne de type
print( sys._clear_type_cache())

#sys._current_frames()
print(sys._current_frames())
"""
{2604: <frame at 0x000001B6252F2EC0, file 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\rpc.py', line 355, code pollpacket>,
4348: <frame at 0x000001B6252F2CD0, file 'C:\\Users\\Ingrid\\Desktop\\COURS PROGRAMME\\Course Level PCAP\\Prog.py', line 16, code <module>>}
"""
    
#sys._current_exceptions()
print(sys._current_exceptions())       #{8368: (None, None, None), 3896: (None, None, None)}

#sys.breakpointhook()
print(sys.breakpointhook())
"""
--Call--
> c:\users\ingrid\appdata\local\programs\python\python310\lib\idlelib\run.py(462)write()
-> def write(self, s):
(Pdb) 
"""

#sys._debugmallocstats()
print(sys._debugmallocstats())         #None

#sys.dllhandle
print(sys.dllhandle)             #140708019175424

#sys.displayhook(value)

#sys.dont_write_bytecode
print(sys.dont_write_bytecode)       #False

#sys.pycache_prefix
print(sys.pycache_prefix)             #None

#sys.excepthook(type, value, traceback)

#sys.exc_info()
print(sys.exc_info())    #(None, None, None) :on a ce resultat car il n'y avait pas d'exception en cours de traitement

#sys.exec_prefix        Renvoie la localisation du fichier python
print(sys.exec_prefix)       #C:\Users\Ingrid\AppData\Local\Programs\Python\Python310


#sys.float_info     renvoie un named tuple contenant des informations à propos du type float. Il contient des informations de bas niveau à propos de la précision et de la représentation interne
"""
sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53,
epsilon=2.220446049250313e-16, radix=2, rounds=1)
"""

#sys.float_repr_style             Une chaîne indiquant comment la fonction repr() se comporte avec les nombres à virgule flottante
print(sys.float_repr_style)    #short 

#sys.getallocatedblocks()        Renvoie le nombre de blocs mémoire actuellement alloués par l'interpréteur, peu importe leur taille. 
print(sys.getallocatedblocks())    #68947

#sys.getandroidapilevel()           Renvoie la version de l'API Android utilisée pour compiler sous forme d'un entier.
print(sys.getandroidapilevel())    #AttributeError: module 'sys' has no attribute 'getandroidapilevel'

#sys.getdefaultencoding()      Renvoie le nom du codage par défaut actuellement utilisé par l'implémentation Unicode pour coder les chaînes.
print(sys.getdefaultencoding())       #utf-8

#sys.getdlopenflags()         Renvoie la valeur actuelle des drapeaux utilisés par les appels de dlopen()
print(sys.getdlopenflags())          #AttributeError: module 'sys' has no attribute 'getdlopenflags'

#sys.getfilesystemencoding()
print(sys.getfilesystemencoding())         #utf-8

# sys.getfilesystemencodeerrors()
print(sys.getfilesystemencodeerrors())      #surrogatepass

#sys.getrefcount(object)       Donne le nombre de référence de l'objet object
print(sys.getrefcount())

#sys.getrecursionlimit()      Donne la limite actuelle de la limite de récursion, la profondeur maximum de la pile de l'interpréteur.
print(sys.getrecursionlimit())        #1000

#sys.getsizeof(object[, default])    Donne la taille d'un objet en octets. L'objet peut être de n'importe quel type. Le résultat sera correct pour tous les objets natifs, mais le résultat peut ne pas être toujours vrai pour les extensions, la valeur étant dépendante de l'implémentation.
print(sys.getsizeof())

#sys.getswitchinterval()      Renvoie la valeur du thread switch interval de l'interpréteur,
print(sys.getswitchinterval())       #0.005

#sys._getframe([depth])
print(sys._getframe())    #<frame at 0x0000014FBDE72CD0, file 'C:\\Users\\Ingrid\\Desktop\\COURS PROGRAMME\\Course Level PCAP\\Prog.py', line 25, code <module>>
"""
Renvoie une frame de la pile d'appels. Si le nombre entier optionnel depth est donné, la frame donnée sera de depth appels depuis le haut de la pile.
Si c'est plus profond que la hauteur de la pile, une exception ValueError est levée. La profondeur par défaut est zéro, 
"""

# sys.getprofile()              Renvoie la fonction de profilage tel que défini par setprofile().
print( sys.getprofile())      #None

#sys.gettrace()      Renvoie la fonction de traçage tel que définie par settrace().
print(sys.gettrace())        #None

#sys.getwindowsversion()         Renvoie un n-uplet nommé décrivant la version de Windows en cours d'exécution.
print(sys.getwindowsversion())       #sys.getwindowsversion(major=10, minor=0, build=19044, platform=2, service_pack='')

#sys.get_asyncgen_hooks()
print(sys.get_asyncgen_hooks())      #asyncgen_hooks(firstiter=None, finalizer=None)

# sys.get_coroutine_origin_tracking_depth()
print(sys.get_coroutine_origin_tracking_depth())     #0

#sys.hash_info              Un named tuple donnant les paramètres de l'implémentation de la fonction de hachage de nombres. 
print(sys.hash_info)     #sys.hash_info(width=64, modulus=2305843009213693951, inf=314159, nan=0, imag=1000003, algorithm='siphash24', hash_bits=64, seed_bits=128, cutoff=0)

#sys.hexversion                 Le numéro de version codé sous forme d'un seul nombre entier. Ce numéro augmente avec chaque version, y compris pour les versions hors production.
print(sys.hexversion)        #50987760


#sys.int_info       Un named tuple qui contient des informations sur la représentation interne des entiers de Python. 
print(sys.int_info)      #sys.int_info(bits_per_digit=30, sizeof_digit=4)

# sys.__interactivehook__     Lorsque cet attribut existe, sa valeur est automatiquement appelée (sans argument) par l'interpréteur lors de son démarrage en mode interactif.
print(sys.__interactivehook__)        #<function enablerlcompleter.<locals>.register_readline at 0x0000020B40342C20>

#sys.intern(string)          Ajoute string dans le tableau des chaînes "internées" et renvoie la chaîne internée -- qui peut être string elle-même ou une copie.
print(sys.intern("string"))     #string

#sys.is_finalizing()               Donne True si l'interpréteur Python est en train de s'arrêter, et False dans le cas contraire.
print(sys.is_finalizing())     #False

# sys.last_type         
#sys.last_value         
#sys.last_traceback        
"""
Ces trois variables ne sont pas toujours définies. Elles sont définies lorsqu'une exception n'est pas gérée et que l'interpréteur affiche un message d'erreur
et une stacktrace.
"""
print(sys.last_type)          #AttributeError: module 'sys' has no attribute 'last_type'
print(sys.last_value)          #AttributeError: module 'sys' has no attribute 'last_value'
print(sys.last_traceback)         #AttributeError: module 'sys' has no attribute 'last_traceback'

#sys.maxsize
print(sys.maxsize)       #9223372036854775807

#sys.maxunicode       Un entier donnant la valeur du plus grand point de code Unicode, c'est-à-dire 1114111 
print(sys.maxunicode)           #1114111

#sys.meta_path         
print(sys.meta_path)           #[<class '_frozen_importlib.BuiltinImporter'>, <class '_frozen_importlib.FrozenImporter'>, <class '_frozen_importlib_external.PathFinder'>]

#sys.modules         dictionnaire qui associe les noms de modules aux modules qui deja èteè chargés.
print(sys.modules)
"""
{'sys': <module 'sys' (built-in)>, 'builtins': <module 'builtins' (built-in)>, '_frozen_importlib': <module '_frozen_importlib' (frozen)>,
'_imp': <module '_imp' (built-in)>, '_thread': <module '_thread' (built-in)>, '_warnings': <module '_warnings' (built-in)>,
'_weakref': <module '_weakref' (built-in)>, '_io': <module '_io' (built-in)>, 'marshal': <module 'marshal' (built-in)>,
'nt': <module 'nt' (built-in)>, 'winreg': <module 'winreg' (built-in)>, '_frozen_importlib_external': <module '_frozen_importlib_external' (frozen)>,
'time': <module 'time' (built-in)>, 'zipimport': <module 'zipimport' (frozen)>, '_codecs': <module '_codecs' (built-in)>,
'codecs': <module 'codecs' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\codecs.py'>,
'encodings.aliases': <module 'encodings.aliases' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\encodings\\aliases.py'>,
'encodings': <module 'encodings' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\encodings\\__init__.py'>,
'encodings.utf_8': <module 'encodings.utf_8' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\encodings\\utf_8.py'>,
'encodings.cp1252': <module 'encodings.cp1252' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\encodings\\cp1252.py'>,
'_signal': <module '_signal' (built-in)>, '_abc': <module '_abc' (built-in)>,
'abc': <module 'abc' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\abc.py'>,
'io': <module 'io' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\io.py'>,
'__main__': <module '__main__' (built-in)>, '_stat': <module '_stat' (built-in)>,
'stat': <module 'stat' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\stat.py'>,
'_collections_abc': <module '_collections_abc' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\_collections_abc.py'>,
'genericpath': <module 'genericpath' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\genericpath.py'>,
'ntpath': <module 'ntpath' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\ntpath.py'>,
'os.path': <module 'ntpath' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\ntpath.py'>,
'os': <module 'os' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\os.py'>,
'_sitebuiltins': <module '_sitebuiltins' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\_sitebuiltins.py'>,
'site': <module 'site' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site.py'>,
'idlelib': <module 'idlelib' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\__init__.py'>,
'itertools': <module 'itertools' (built-in)>, 'keyword': <module 'keyword' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\keyword.py'>,
'_operator': <module '_operator' (built-in)>, 'operator': <module 'operator' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\operator.py'>,
'reprlib': <module 'reprlib' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\reprlib.py'>,
'_collections': <module '_collections' (built-in)>,
'collections': <module 'collections' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\collections\\__init__.py'>,
'types': <module 'types' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\types.py'>,
'_functools': <module '_functools' (built-in)>, 'functools': <module 'functools' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\functools.py'>,
'contextlib': <module 'contextlib' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\contextlib.py'>,
'enum': <module 'enum' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\enum.py'>,
'_sre': <module '_sre' (built-in)>, 'sre_constants': <module 'sre_constants' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\sre_constants.py'>, 'sre_parse': <module 'sre_parse' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\sre_parse.py'>, 'sre_compile': <module 'sre_compile' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\sre_compile.py'>, '_locale': <module '_locale' (built-in)>, 'copyreg': <module 'copyreg' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\copyreg.py'>, 're': <module 're' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\re.py'>, 'token': <module 'token' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\token.py'>, 'tokenize': <module 'tokenize' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\tokenize.py'>, 'linecache': <module 'linecache' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\linecache.py'>, '_weakrefset': <module '_weakrefset' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\_weakrefset.py'>, 'threading': <module 'threading' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\threading.py'>, '_heapq': <module '_heapq' (built-in)>, 'heapq': <module 'heapq' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\heapq.py'>, '_queue': <module '_queue' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\DLLs\\_queue.pyd'>, 'queue': <module 'queue' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\queue.py'>, 'textwrap': <module 'textwrap' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\textwrap.py'>, 'traceback': <module 'traceback' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\traceback.py'>, 'warnings': <module 'warnings' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\warnings.py'>, '_string': <module '_string' (built-in)>, 'string': <module 'string' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\string.py'>, 'errno': <module 'errno' (built-in)>, 'signal': <module 'signal' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\signal.py'>, 'msvcrt': <module 'msvcrt' (built-in)>, '_winapi': <module '_winapi' (built-in)>, 'subprocess': <module 'subprocess' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\subprocess.py'>, 'platform': <module 'platform' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\platform.py'>, '_tkinter': <module '_tkinter' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\DLLs\\_tkinter.pyd'>, 'tkinter.constants': <module 'tkinter.constants' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\tkinter\\constants.py'>, 'tkinter': <module 'tkinter' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\tkinter\\__init__.py'>, 'idlelib.multicall': <module 'idlelib.multicall' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\multicall.py'>, 'idlelib.autocomplete_w': <module 'idlelib.autocomplete_w' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\autocomplete_w.py'>, 'collections.abc': <module 'collections.abc' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\collections\\abc.py'>, 'configparser': <module 'configparser' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\configparser.py'>, 'idlelib.config': <module 'idlelib.config' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\config.py'>, 'idlelib.pyparse': <module 'idlelib.pyparse' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\pyparse.py'>, 'idlelib.hyperparser': <module 'idlelib.hyperparser' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\hyperparser.py'>, 'idlelib.autocomplete': <module 'idlelib.autocomplete' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\autocomplete.py'>, '_ast': <module '_ast' (built-in)>, 'ast': <module 'ast' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\ast.py'>, '_opcode': <module '_opcode' (built-in)>, 'opcode': <module 'opcode' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\opcode.py'>, 'dis': <module 'dis' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\dis.py'>, 'importlib._bootstrap': <module '_frozen_importlib' (frozen)>, 'importlib._bootstrap_external': <module '_frozen_importlib_external' (frozen)>, 'importlib': <module 'importlib' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\importlib\\__init__.py'>, 'importlib.machinery': <module 'importlib.machinery' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\importlib\\machinery.py'>, 'inspect': <module 'inspect' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\inspect.py'>, 'idlelib.tooltip': <module 'idlelib.tooltip' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\tooltip.py'>, 'idlelib.calltip_w': <module 'idlelib.calltip_w' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\calltip_w.py'>, 'idlelib.calltip': <module 'idlelib.calltip' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\calltip.py'>, 'posixpath': <module 'posixpath' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\posixpath.py'>, 'fnmatch': <module 'fnmatch' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\fnmatch.py'>, 'bdb': <module 'bdb' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\bdb.py'>, 'binascii': <module 'binascii' (built-in)>, 'math': <module 'math' (built-in)>, '_datetime': <module '_datetime' (built-in)>, 'datetime': <module 'datetime' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\datetime.py'>, '_struct': <module '_struct' (built-in)>, 'struct': <module 'struct' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\struct.py'>, 'xml': <module 'xml' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\xml\\__init__.py'>, 'xml.parsers': <module 'xml.parsers' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\xml\\parsers\\__init__.py'>, 'pyexpat.errors': <module 'pyexpat.errors'>, 'pyexpat.model': <module 'pyexpat.model'>, 'pyexpat': <module 'pyexpat' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\DLLs\\pyexpat.pyd'>, 'xml.parsers.expat.model': <module 'pyexpat.model'>, 'xml.parsers.expat.errors': <module 'pyexpat.errors'>, 'xml.parsers.expat': <module 'xml.parsers.expat' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\xml\\parsers\\expat.py'>, 'plistlib': <module 'plistlib' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\plistlib.py'>, 'idlelib.macosx': <module 'idlelib.macosx' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\macosx.py'>, 'idlelib.scrolledlist': <module 'idlelib.scrolledlist' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\scrolledlist.py'>, 'idlelib.window': <module 'idlelib.window' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\window.py'>, 'idlelib.debugger': <module 'idlelib.debugger' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\debugger.py'>, 'idlelib.debugger_r': <module 'idlelib.debugger_r' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\debugger_r.py'>, '_compat_pickle': <module '_compat_pickle' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\_compat_pickle.py'>, '_pickle': <module '_pickle' (built-in)>, 'pickle': <module 'pickle' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\pickle.py'>, 'select': <module 'select' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\DLLs\\select.pyd'>, '_socket': <module '_socket' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\DLLs\\_socket.pyd'>, 'selectors': <module 'selectors' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\selectors.py'>, 'socket': <module 'socket' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\socket.py'>, 'socketserver': <module 'socketserver' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\socketserver.py'>, 'idlelib.rpc': <module 'idlelib.rpc' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\rpc.py'>, 'idlelib.debugobj_r': <module 'idlelib.debugobj_r' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\debugobj_r.py'>, 'shlex': <module 'shlex' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\shlex.py'>, 'zlib': <module 'zlib' (built-in)>, '_compression': <module '_compression' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\_compression.py'>, '_bz2': <module '_bz2' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\DLLs\\_bz2.pyd'>, 'bz2': <module 'bz2' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\bz2.py'>, '_lzma': <module '_lzma' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\DLLs\\_lzma.pyd'>, 'lzma': <module 'lzma' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\lzma.py'>, 'shutil': <module 'shutil' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\shutil.py'>, '_bisect': <module '_bisect' (built-in)>, 'bisect': <module 'bisect' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\bisect.py'>, '_random': <module '_random' (built-in)>, '_sha512': <module '_sha512' (built-in)>, 'random': <module 'random' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\random.py'>, 'weakref': <module 'weakref' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\weakref.py'>, 'tempfile': <module 'tempfile' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\tempfile.py'>, 'idlelib.iomenu': <module 'idlelib.iomenu' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\iomenu.py'>, 'idlelib.zoomheight': <module 'idlelib.zoomheight' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\zoomheight.py'>, 'idlelib.tree': <module 'idlelib.tree' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\tree.py'>, 'idlelib.debugobj': <module 'idlelib.debugobj' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\debugobj.py'>, 'idlelib.stackviewer': <module 'idlelib.stackviewer' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\stackviewer.py'>, 'idlelib.run': <module 'idlelib.run' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\run.py'>, 'importlib._abc': <module 'importlib._abc' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\importlib\\_abc.py'>, 'importlib.util': <module 'importlib.util' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\importlib\\util.py'>, 'pkgutil': <module 'pkgutil' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\pkgutil.py'>, 'sysconfig': <module 'sysconfig' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\sysconfig.py'>, 'urllib': <module 'urllib' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\urllib\\__init__.py'>, 'urllib.parse': <module 'urllib.parse' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\urllib\\parse.py'>, 'pydoc': <module 'pydoc' from 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\pydoc.py'>}
"""


#sys.orig_argv
print(sys.orig_argv)   #['C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\pythonw.exe', '-c', "__import__('idlelib.run').run.main(True)", '55107']


# sys.path_hooks     Une liste d'appelables d'un argument, path, pour essayer de créer un finder pour ce chemin. Si un finder peut être créé, il doit être renvoyé par l'appelable, sinon une ImportError doit être levée.
print( sys.path_hooks)        #[<class 'zipimport.zipimporter'>, <function FileFinder.path_hook.<locals>.path_hook_for_FileFinder at 0x00000246F8530B80>]

#sys.path_importer_cache        Un dictionnaire faisant office de cache pour les objets finder
print(sys.path_importer_cache)
"""
{'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip': None,
'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\DLLs': FileFinder('C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\DLLs'),
'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib': FileFinder('C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib'),
'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\encodings': FileFinder('C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\encodings'), 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310': FileFinder('C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310'), 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages': FileFinder('C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages'), 'C:\\Users\\Ingrid\\Desktop\\COURS PROGRAMME\\Course Level PCAP': FileFinder('C:\\Users\\Ingrid\\Desktop\\COURS PROGRAMME\\Course Level PCAP'), 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib': FileFinder('C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib'), 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\tkinter': FileFinder('C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\tkinter'), 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\collections': FileFinder('C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\collections'), 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\importlib': FileFinder('C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\importlib'), 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\xml': FileFinder('C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\xml'), 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\xml\\parsers': FileFinder('C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\xml\\parsers'), 'C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\urllib': FileFinder('C:\\Users\\Ingrid\\AppData\\Local\\Programs\\Python\\Python310\\lib\\urllib')}
"""

# sys.platform        Cette chaîne contient un identificateur de plateforme qui peut être typiquement utilisé pour ajouter des composants spécifiques à sys.path.    
print( sys.platform)         #win32

#sys.platlibdir           Nom du répertoire de la bibliothèque spécifique à la plate-forme. Il est utilisé pour construire le chemin de la bibliothèque standard et les chemins des modules d'extension installés.
print(sys.platlibdir)       #lib

# sys.prefix     Une chaîne indiquant le préfixe du répertoire spécifique au site dans lequel les fichiers Python indépendants de la plate-forme sont installés.
print( sys.prefix)        #C:\Users\Ingrid\AppData\Local\Programs\Python\Python310

# sys.ps1
#sys.ps2
"""
Chaînes spécifiant l'invite primaire et secondaire de l'interpréteur. Celles-ci ne sont définies que si l'interpréteur est en mode interactif.
"""
print(sys.ps1)     #AttributeError: module  'sys' has no attribute 'ps1'
print(sys.ps2)      #AttributeError: module 'sys' has no attribute 'ps2'



# sys.setdlopenflags(n)      Définit les options utilisées par l'interpréteur lors des appels à dlopen(), typiquement utilisé par l'interpréteur pour charger des modules d'extension
print( sys.setdlopenflags())      #AttributeError: module 'sys' has no attribute 'setdlopenflags'

# sys.setprofile(profilefunc)      Définit la fonction de profilage du système, qui vous permet d'implémenter un profileur de code source Python en Python.
print( sys.setprofile())

#sys.stdin
#sys.stdout
#sys.stderr

"""objets fichiers utilisés par l'interpréteur pour l'entrée standard, la sortie standard et la sortie d'erreurs :

stdin est utilisé pour toutes les entrées interactives (y compris les appels à input())

 stdout est utilisé pour la sortie de print(), des expression et pour les invites de input() ;

Les invites de l'interpréteur et ses messages d'erreur sont écrits sur stderr.
"""

#sys.version
"""Une chaîne contenant le numéro de version de l'interpréteur Python, ainsi que d'autres informations comme le numéro de compilation et le compilateur utilisé.
Cette chaîne est affichée lorsque l'interpréteur est démarré en mode interactif. N'essayez pas d'en extraire des informations de version,
utilisez plutôt version_info et les fonctions fournies par le module platform.
"""
print(sys.version)     #3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)]


#sys.api_version   La version de l'API C pour cet interpréteur. Les développeurs peuvent trouver cette information utile en déboguant des conflits de versions entre Pythonet des modules d'extension.
print(sys.api_version)       #1013


#sys.version_info   Un quintuplet contenant les composants du numéro de version : major, minor, micro, releaselevel et serial. Toutes les valeurs sauf releaselevel sont des nombres entiers. releaselevel peut valoir 'alpha', 'beta', 'candidate', ou 'final'.
print(sys.version_info)        #sys.version_info(major=3, minor=10, micro=2, releaselevel='final', serial=0)

#sys.warnoptions                   C'est une spécificité de l'implémentation de la gestion des avertissements. Ne modifiez pas cette valeur. 
print(sys.warnoptions)        #[]






