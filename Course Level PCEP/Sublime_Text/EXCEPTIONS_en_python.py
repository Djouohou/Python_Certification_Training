import os
"""
try:
    a=4
    b=0
    print(a/b)
except ZeroDivisionError:
   print("il y'a une erreur:Division par zero")
except TypeError:
    print("Erreur de type")
finally:
    print("s'execute toujours")
print("fin de la dividion")
"""
#Les fonctions natives python
print (abs (-1))
print("---------------------------------------------------------------")
liste=["True","True","True","1"]
print(all(liste))
print("---------------------------------------------------------------")
liste=["True","False","True"]
print(any(liste))
print("---------------------------------------------------------------")
print(bin(101))
print("---------------------------------------------------------------")
print(callable("A"))
print("---------------------------------------------------------------")
print(callable("int"))
print("---------------------------------------------------------------")
print("oLIvier".capitalize())
print("---------------------------------------------------------------")
import random
print(random.choice(["1","2","3","4","5"]))
print(random.choice(["1","2","3","4","5"]))
print("---------------------------------------------------------------")
print("olivier".count("i"))
print("---------------------------------------------------------------")
print(dir(int))
print("---------------------------------------------------------------")
a = "olivier"
print(a.endswith("r"))
print(a.endswith("er"))
print(a.endswith("é"))
print("---------------------------------------------------------------")
v = 101
print(eval('v+1'))
print("---------------------------------------------------------------")
print("olivier".find("i"))
print("---------------------------------------------------------------")
print(help(int))

"""Help on class int in module __builtin__:

class int(object)
 |  int(x=0) -> int or long
 |  int(x, base=10) -> int or long
 |  
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is floating point, the conversion truncates towards zero.
 |  If x is outside the integer range, the function returns a long instead.
 |  
 |  If x is not a number or if base is given, then x must be a string or
 |  Unicode object representing an integer literal in the given base.  The
 |  literal can be preceded by '+' or '-' and be surrounded by whitespace.
 |  The base defaults to 10.  Valid bases are 0 and 2-36.  Base 0 means to
 |  interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
"""
print("---------------------------------------------------------------")
print(hex(16))
print("---------------------------------------------------------------")
print("25".isalnum())
print("25b".isalnum())
print("25bé".isalnum())
print("25bé@".isalnum())
print("-".isalnum())
print("_".isalnum())
print("".isalnum())
print("---------------------------------------------------------------")
print("x".isalpha())
print("-".isalpha())
print("12".isalpha())
print("jean-claude".isalpha())
print("jean claude".isalpha())
print("élise".isalpha())
print("---------------------------------------------------------------")
print("1".isdigit())
print("1.5".isdigit())
print("1,5".isdigit())
print("3b".isdigit())
print(" ".isdigit())
print("---------------------------------------------------------------")
print("olivier".islower())
print("Olivier".islower())
print("---------------------------------------------------------------")
print(" ".isspace())
print("jean louis".isspace())
print("   ".isspace())
print("---------------------------------------------------------------")
print("Titre".istitle())
print("TitrE".istitle())
print("Titre de mon site".istitle())
print("Titre De Mon Site".istitle())
print("---------------------------------------------------------------")
print("OLIVIER".isupper())
print("Olivier".isupper())
print("OlivieR".isupper())
print("---------------------------------------------------------------")
print(":".join(["olivier", "engel"]))
print("---------------------------------------------------------------")
print(len([1,2,3]))
print(len("olivier"))
print("---------------------------------------------------------------")
print(locals())
print("---------------------------------------------------------------")
print("OLIVIER".lower())
print("---------------------------------------------------------------")
def add_one(x):
    return x + 1
print(map(add_one, [1,2,3]))
print("---------------------------------------------------------------")
print(max([1,3,2,6,99,1]))
print(min(1,4,6,12,1))
print("---------------------------------------------------------------")
import random
print(random.randint(1,11))
print("---------------------------------------------------------------")
import random
print(random.random())
print("---------------------------------------------------------------")
print("olivier".replace("i", "a"))
print("---------------------------------------------------------------")
x = [1,4,7]
x.reverse()
print(x)
print("---------------------------------------------------------------")
print(list(reversed([1,2,3,4])))
print("---------------------------------------------------------------")
print(round(1))
print(round(1.2))
print(round(1.5))
print(round(1.7))
print(round(-1.7))
print(round(-1.2))
print("---------------------------------------------------------------")
import random
x = [1,2,3,4,5]
random.shuffle(x)
print(x)
print("---------------------------------------------------------------")
print("olivier".startswith("ol"))
print("olivier".startswith(("ol", "eng")))
print("olivier".startswith(("xxx", "eng")))
print("olivier".startswith("OL"))
print("olivier".startswith("ol"))
print("---------------------------------------------------------------")
l = [5,1,4,2,10]
l.sort()
print(l)
print("---------------------------------------------------------------")
print(sorted([3,2,12,1]))
print("---------------------------------------------------------------")
print("olivier:engel".split(":"))
print("---------------------------------------------------------------")
print("olivier\n\n\engel\n\ndéveloppeur".splitlines())
print("olivier\nengel\ndéveloppeur".splitlines())
print("olivier\n\rengel\n\rdéveloppeur".splitlines())
print("olivier\r\nengel\r\ndéveloppeur".splitlines())
print("olivier\r\nengel\r\n\r\ndéveloppeur".splitlines())
print("olivier\r\nengel\r\n\r\ndéveloppeur".splitlines(True))
print("---------------------------------------------------------------")
print(sum([1,2,3]))
print("---------------------------------------------------------------")
print("Ceci est un titre".title())
print("---------------------------------------------------------------")
print("olivier".upper())
print("---------------------------------------------------------------")
a = ["olivier", "bruce", "john"]
b = ["engel", "wayne", "Wayne"]
print(zip(a,b))
print([i for i in zip(a,b)])



os.system("pause")
