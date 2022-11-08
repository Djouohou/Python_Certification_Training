#ici la classe fille utilise le constructeur de la classe mere a cause de l'heritage
class Vehicule:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicule):
    pass

school_bus = Bus("school Volvo", 12, 50)

print(school_bus.name)  #school Volvo

#ici la classe fille a son propre constructeur
class Vehicule:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicule):
    def __init__(self):
        pass           

school_bus = Bus("school Volvo", 12, 50)

print(school_bus.name)       #File "C:/Users/Ingrid/Desktop/COURS PROGRAMME/Course Level PCPP1/Advanced_OOP.py", line 11, in <module>
                             #school_bus = Bus("school Volvo", 12, 50)
                             #TypeError: Bus.__init__() takes 1 positional argument but 4 were given

#Si on veut que la classe mere soit prise en consideration dans la classe fille, on doit utiliser le polymorphisme:
class Vehicule:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicule):
    def __init__(self, name, mileage, capacity):
        super().__init__(name, mileage, capacity)
school_bus = Bus("school Volvo", 12, 50)

print(school_bus.name)  #school Volvo


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def __init__(self, name, mileage, capacity, couleur):
        super().__init__(name, mileage, capacity)
        self.couleur = couleur

    def fare(self, val):
        fare = super().fare()
        total_fare = fare + (fare * val)
        return total_fare

school_bus = Bus("school Volvo", 12, 50, "rouge")

print(school_bus.name)   #school Volvo
print("total bus fare is: ", school_bus.fare(0.10))  #total bus fare is:  5500.0

print(isinstance(school_bus, Vehicle)) #True
print(issubclass(Bus, Vehicle))   #True



#Utilisation d'un conteneur (liste, tuple, dict...) pour la creation d'un nombre infini d'objet

class Person:
    def __init__(self, name):
        self.name = name

persons = {}

while True:
    name = input("Entrer un nom : ")
    if not name:
        break
    persons[name] = Person(name)


import random

class ApplePack:
    number = 0
    weight = 0
    def __init__(self):
        ApplePack.number += 1
        ApplePack.weight += random.uniform(0.2 , 0.5)
        


liste=[]
for i in range (1000):
    apples = ApplePack()
    liste.append(apples)
    if ApplePack.weight >= 300 :
        break
print(ApplePack.number)
print(ApplePack.weight)

#PYTHON CORE SYNTAX EXPRESSIONS AND THEIR MAGIC METHOD
print(dir(int))
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__',
 '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__',
 '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__',
 '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__',
 '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__',
 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

#Comparison methods
Function or operator	         Magic method               	  Implementation meaning or purpose
==	                         __eq__(self, other)	            equality operator
!=	                         __ne__(self, other)	            inequality operator
<	                         __lt__(self, other)	            less-than operator
>	                         __gt__(self, other)	            greater-than operator
<=	                         __le__(self, other)	            less-than-or-equal-to operator
>=	                         __ge__(self, other)	            greater-than-or-equal-to operator

#Numeric methods
Unary operators and functions
Function or operator	         Magic method	                   Implementation meaning or purpose
+	                        __pos__(self)	                     unary positive, like a = +b
-	                        __neg__(self)	                     unary negative, like a = -b
abs()	                        __abs__(self)	                     behavior for abs() function
round(a, b)	                __round__(self, b)	             behavior for round() function

#Common, binary operators and functions
Function or operator	         Magic method	                   Implementation meaning or purpose
+	                         __add__(self, other)	             addition operator
-	                         __sub__(self, other)	             subtraction operator
*	                         __mul__(self, other)	             multiplication operator
//	                         __floordiv__(self, other)	     integer division operator
/	                         __div__(self, other)	             division operator
%	                         __mod__(self, other)	             modulo operator
**	                         __pow__(self, other)	             exponential (power) operator

#Augumented operators and functions
By augumented assignment we should understand a sequence of unary operators and assignments like a += 20

Function or operator	          Magic method	                    Implementation meaning or purpose
+=	                         __iadd__(self, other)	              addition and assignment operator
-=	                         __isub__(self, other)	              subtraction and assignment operator
*=	                         __imul__(self, other)	              multiplication and assignment operator
//=	                         __ifloordiv__(self, other)	      integer division and assignment operator
/=	                         __idiv__(self, other)	              division and assignment operator
%=	                         __imod__(self, other)	              modulo and assignment operator
**=	                         __ipow__(self, other)	              exponential (power) and assignment operator

#Type conversion methods
Python offers a set of methods responsible for the conversion of built-in data types.

Function	                  Magic method	                    Implementation meaning or purpose
int()	                          __int__(self)	                      conversion to integer type
float()	                          __float__(self)	              conversion to float type
oct()	                          __oct__(self)	                      conversion to string, containing an octal representation
hex()	                          __hex__(self)	                      conversion to string, containing a hexadecimal representation

#Object introspection
Python offers a set of methods responsible for representing object details using ordinary strings.

Function	                  Magic method	                     Implementation meaning or purpose
str()	                          __str__(self)	                       responsible for handling str() function calls
repr()	                          __repr__(self)	               responsible for handling repr() function calls
format()	                  __format__(self, formatstr)	       called when new-style string formatting is applied to an object
hash()	                          __hash__(self)	               responsible for handling hash() function calls
dir()	                          __dir__(self)	                       responsible for handling dir() function calls
bool()	                          __nonzero__(self)	               responsible for handling bool() function calls

#Object retrospection
Following the topic of object introspection, there are methods responsible for object reflection.

Function	                      Magic method	                          Implementation meaning or purpose
isinstance(object, class)	      __instancecheck__(self, object)	           responsible for handling isinstance() function calls
issubclass(subclass, class)	      __subclasscheck__(self, subclass)	           responsible for handling issubclass() function calls

#Object attribute access
Access to object attributes can be controlled via the following magic methods

Expression example	                  Magic method	                              Implementation meaning or purpose
object.attribute	                  __getattr__(self, attribute)	               responsible for handling access to a non-existing attribute
object.attribute	                  __getattribute__(self, attribute)	       responsible for handling access to an existing attribute
object.attribute = value	          __setattr__(self, attribute, value)	       responsible for setting an attribute value
del object.attribute	                  __delattr__(self, attribute)	               responsible for deleting an attribute

#Methods allowing access to containers
Containers are any object that holds an arbitrary number of other objects; containers provide a way to access the contained objects and to iterate over them.
Container examples: list, dictionary, tuple, and set.

Expression example	                  Magic method	                           Implementation meaning or purpose
len(container)	                          __len__(self)	                            returns the length (number of elements) of the container
container[key]	                          __getitem__(self, key)	            responsible for accessing (fetching) an element identified by the key argument
container[key] = value	                  __setitem__(self, key, value)	            responsible for setting a value to an element identified by the key argument
del container[key]	                  __delitem__(self, key)	            responsible for deleting an element identified by the key argument
for element in container	          __iter__(self)	                    returns an iterator for the container
item in container	                  __contains__(self, item)	            responds to the question: does the container contain the selected item?









