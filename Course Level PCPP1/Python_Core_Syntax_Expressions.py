#PYTHON CORE SYNTAX EXPRESSIONS AND THEIR MAGIC METHOD
print(dir(int)) #example 
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



#object.__new__(cls[, ...])

Called to create a new instance of class cls. __new__() is a static method that takes the class of which an instance was requested as its first argument.
The remaining arguments are those passed to the object constructor expression . The return value of __new__() should be the new object instance.

#object.__init__(self[, ...])
Called after the instance has been created (by __new__()), but before it is returned to the caller. The arguments are those passed to the class constructor expression.
__new__() and __init__() work together in constructing objects (__new__() to create it, and __init__() to customize it)


#object.__del__(self)
Called when the instance is about to be destroyed. This is also called a finalizer or (improperly) a destructor.
It is not guaranteed that __del__() methods are called for objects that still exist when the interpreter exits.

#object.__repr__(self)
Called by the repr() built-in function to compute the “official” string representation of an object.
The return value must be a string object. If a class defines __repr__() but not __str__(), then __repr__() is also used when an “informal” string representation
of instances of that class is required.

#object.__str__(self)
Called by str(object) and the built-in functions format() and print() to compute the “informal” or nicely printable string representation of an object.
The return value must be a string object.
This method differs from object.__repr__() in that there is no expectation that __str__() return a valid Python expression.

#object.__bytes__(self)
Called by bytes to compute a byte-string representation of an object. This should return a bytes object.

#object.__format__(self, format_spec)
Called by the format() built-in function, and by extension, evaluation of formatted string literals and the str.format() method, to produce a “formatted” string
representation of an object. The format_spec argument is a string that contains a description of the formatting options desired.
The return value must be a string object.

#object.__lt__(self, other)
#object.__le__(self, other)
#object.__eq__(self, other)
#object.__ne__(self, other)
#object.__gt__(self, other)
#object.__ge__(self, other)
These are the so-called “rich comparison” methods. The correspondence between operator symbols and method names is as follows: x<y calls x.__lt__(y),
x<=y calls x.__le__(y), x==y calls x.__eq__(y), x!=y calls x.__ne__(y), x>y calls x.__gt__(y), and x>=y calls x.__ge__(y).
A rich comparison method may return the singleton NotImplemented if it does not implement the operation for a given pair of arguments.
By convention, False and True are returned for a successful comparison.
By default, object implements __eq__() by using is, returning NotImplemented in the case of a false comparison: True if x is y else NotImplemented.
For __ne__(), by default it delegates to __eq__() and inverts the result unless it is NotImplemented.
There are no other implied relationships among the comparison operators or default implementations;
for example, the truth of (x<y or x==y) does not imply x<=y. 

#object.__hash__(self)
Called by built-in function hash() and for operations on members of hashed collections including set, frozenset, and dict.
The __hash__() method should return an integer. The only required property is that objects which compare equal have the same hash value;
The only required property is that objects which compare equal have the same hash value; it is advised to mix together the hash values of the components of
the object that also play a part in comparison of objects by packing them into a tuple and hashing the tuple. Example:

    def __hash__(self):
        return hash((self.name, self.nick, self.color))

#object.__bool__(self)
Called to implement truth value testing and the built-in operation bool(); should return False or True. When this method is not defined, __len__() is called,
if it is defined, and the object is considered true if its result is nonzero. If a class defines neither __len__() nor __bool__(), all its instances are
considered true.


#object.__getattr__(self, name)
Called when the default attribute access fails with an AttributeError . This method should either return the attribute value or raise an AttributeError exception.

#object.__getattribute__(self, name)
Called unconditionally to implement attribute accesses for instances of the class. This method should return the (computed) attribute value or raise an AttributeError exception. 

#object.__setattr__(self, name, value)
Called when an attribute assignment is attempted. name is the attribute name, value is the value to be assigned to it.

#object.__delattr__(self, name)
Like __setattr__() but for attribute deletion instead of assignment. This should only be implemented if del obj.name is meaningful for the object.

#object.__dir__(self)
Called when dir() is called on the object. A sequence must be returned. dir() converts the returned sequence to a list and sorts it.

#object.__get__(self, instance, owner=None)
Called to get the attribute of the owner class (class attribute access) or of an instance of that class (instance attribute access).
The optional owner argument is the owner class, while instance is the instance that the attribute was accessed through, or None when the attribute is accessed
through the owner.
This method should return the computed attribute value or raise an AttributeError exception.

#object.__set__(self, instance, value)
Called to set the attribute on an instance instance of the owner class to a new value, value.

#object.__delete__(self, instance)
Called to delete the attribute on an instance instance of the owner class.

#object.__slots__
This class variable can be assigned a string, iterable, or sequence of strings with variable names used by instances. __slots__ reserves space for the declared
variables and prevents the automatic creation of __dict__ and __weakref__ for each instance.

#object.__set_name__(self, owner, name)
Automatically called at the time the owning class owner is created. The object has been assigned to name in that class:
    class A:
        x = C()  # Automatically calls: x.__set_name__(A, 'x')
If the class variable is assigned after the class is created, __set_name__() will not be called automatically. If needed, __set_name__() can be called directly:
    class A:
       pass

    c = C()
    A.x = c                  # The hook is not called
    c.__set_name__(A, 'x')   # Manually invoke the hook


#class.__instancecheck__(self, instance)
Return true if instance should be considered a (direct or indirect) instance of class. If defined, called to implement isinstance(instance, class).

#class.__subclasscheck__(self, subclass)
Return true if subclass should be considered a (direct or indirect) subclass of class. If defined, called to implement issubclass(subclass, class).

#classmethod object.__class_getitem__(cls, key)
Return an object representing the specialization of a generic class by type arguments found in key.

#object.__call__(self[, args...])
Called when the instance is “called” as a function; if this method is defined, x(arg1, arg2, ...) roughly translates to type(x).__call__(x, arg1, ...).

#object.__len__(self)
Called to implement the built-in function len(). Should return the length of the object, an integer >= 0.
Also, an object that doesn’t define a __bool__() method and whose __len__() method returns zero is considered to be false in a Boolean context.

#object.__length_hint__(self)
Called to implement operator.length_hint(). Should return an estimated length for the object (which may be greater or less than the actual length).
The length must be an integer >= 0. The return value may also be NotImplemented, which is treated the same as if the __length_hint__ method didn’t exist at all.
This method is purely an optimization and is never required for correctness.

#object.__getitem__(self, key)
Called to implement evaluation of self[key]. For sequence types, the accepted keys should be integers and slice objects.

#object.__setitem__(self, key, value)
Called to implement assignment to self[key].

#object.__delitem__(self, key)
Called to implement deletion of self[key].

#object.__missing__(self, key)
Called by dict.__getitem__() to implement self[key] for dict subclasses when key is not in the dictionary.

#object.__iter__(self)
This method is called when an iterator is required for a container. This method should return a new iterator object that can iterate over all the objects in the
container.

#object.__reversed__(self)
Called (if present) by the reversed() built-in to implement reverse iteration. It should return a new iterator object that iterates over all the objects in the
container in reverse order.

#object.__contains__(self, item)
Called to implement membership test operators. Should return true if item is in self, false otherwise. 

#Emulating numeric types
The following methods can be defined to emulate numeric objects. Methods corresponding to operations that are not supported by the particular kind of number
implemented (e.g., bitwise operations for non-integral numbers) should be left undefined.

object.__add__(self, other)
object.__sub__(self, other)
object.__mul__(self, other)
object.__matmul__(self, other)
object.__truediv__(self, other)
object.__floordiv__(self, other)
object.__mod__(self, other)
object.__divmod__(self, other)
object.__pow__(self, other[, modulo])
object.__lshift__(self, other)
object.__rshift__(self, other)
object.__and__(self, other)
object.__xor__(self, other)
object.__or__(self, other)

These methods are called to implement the binary arithmetic operations (+, -, *, @, /, //, %, divmod(), pow(), **, <<, >>, &, ^, |).
If one of those methods does not support the operation with the supplied arguments, it should return NotImplemented.

object.__radd__(self, other)
object.__rsub__(self, other)
object.__rmul__(self, other)
object.__rmatmul__(self, other)
object.__rtruediv__(self, other)
object.__rfloordiv__(self, other)
object.__rmod__(self, other)
object.__rdivmod__(self, other)
object.__rpow__(self, other[, modulo])
object.__rlshift__(self, other)
object.__rrshift__(self, other)
object.__rand__(self, other)
object.__rxor__(self, other)
object.__ror__(self, other)

These methods are called to implement the binary arithmetic operations (+, -, *, @, /, //, %, divmod(), pow(), **, <<, >>, &, ^, |) with reflected (swapped) operands.
These functions are only called if the left operand does not support the corresponding operation 3 and the operands are of different types.

If the right operand’s type is a subclass of the left operand’s type and that subclass provides a different implementation of the reflected method for the operation,
this method will be called before the left operand’s non-reflected method. This behavior allows subclasses to override their ancestors’ operations.

object.__iadd__(self, other)
object.__isub__(self, other)
object.__imul__(self, other)
object.__imatmul__(self, other)
object.__itruediv__(self, other)
object.__ifloordiv__(self, other)
object.__imod__(self, other)
object.__ipow__(self, other[, modulo])
object.__ilshift__(self, other)
object.__irshift__(self, other)
object.__iand__(self, other)
object.__ixor__(self, other)
object.__ior__(self, other)

These methods are called to implement the augmented arithmetic assignments (+=, -=, *=, @=, /=, //=, %=, **=, <<=, >>=, &=, ^=, |=).
These methods should attempt to do the operation in-place (modifying self) and return the result (which could be, but does not have to be, self).

object.__neg__(self)
object.__pos__(self)
object.__abs__(self)
object.__invert__(self)

Called to implement the unary arithmetic operations (-, +, abs() and ~).

object.__complex__(self)
object.__int__(self)
object.__float__(self)

Called to implement the built-in functions complex(), int() and float(). Should return a value of the appropriate type.

object.__index__(self)

Called to implement operator.index(), and whenever Python needs to losslessly convert the numeric object to an integer object (such as in slicing, or in the built-in
bin(), hex() and oct() functions). Presence of this method indicates that the numeric object is an integer type. Must return an integer.

If __int__(), __float__() and __complex__() are not defined then corresponding built-in functions int(), float() and complex() fall back to __index__().

object.__round__(self[, ndigits])
object.__trunc__(self)
object.__floor__(self)
object.__ceil__(self)

Called to implement the built-in function round() and math functions trunc(), floor() and ceil(). Unless ndigits is passed to __round__() all these methods should
return the value of the object truncated to an Integral (typicban int).The built-in function int() falls back to __trunc__() if neither __int__() nor __index__() is defined.


#object.__enter__(self)
Enter the runtime context related to this object. The with statement will bind this method’s return value to the target(s) specified in the as clause of the statement,
if any.

#object.__exit__(self, exc_type, exc_value, traceback)
Exit the runtime context related to this object. The parameters describe the exception that caused the context to be exited. If the context was exited without an
exception, all three arguments will be None.
If an exception is supplied, and the method wishes to suppress the exception (i.e., prevent it from being propagated), it should return a true value.

#object.__match_args__
This class variable can be assigned a tuple of strings. When this class is used in a class pattern with positional arguments, each positional argument will be
converted into a keyword argument, using the corresponding value in __match_args__ as the keyword. The absence of this attribute is equivalent to setting it to ().

#object.__await__(self)
Must return an iterator. Should be used to implement awaitable objects. For instance, asyncio.Future implements this method to be compatible with the await expression.

#object.__aiter__(self)
Must return an asynchronous iterator object.

#object.__anext__(self)
Must return an awaitable resulting in a next value of the iterator. Should raise a StopAsyncIteration error when the iteration is over.

#object.__aenter__(self)
Semantically similar to __enter__(), the only difference being that it must return an awaitable.

#object.__aexit__(self, exc_type, exc_value, traceback)
Semantically similar to __exit__(), the only difference being that it must return an awaitable.




























































































































