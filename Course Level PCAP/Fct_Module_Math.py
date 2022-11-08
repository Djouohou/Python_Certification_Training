#LES FONCTIONS DU MODULE MATH

import math

#math.ceil(x)       il correspond a l'arrondi plafond. si on a un entier en parametre , la valeur de retour ne change pas.
Renvoie la fonction plafond de x, le plus petit entier grand ou egal à x. il renvoi un entier .

value = 4.7
print("Math.ceil( %.1f ) == %d" % (value, math.ceil(value)))

value = 4.1
print("Math.ceil( %.1f ) == %d" % (value, math.ceil(value)))

value = 4.0
print("Math.ceil( %.1f ) == %d" % (value, math.ceil(value)))

value = 0
print("Math.ceil( %.1f ) == %d" % (value, math.ceil(value)))

value = -1.3
print("Math.ceil( %.1f ) == %d" % (value, math.ceil(value)))

value = -1.9
print("Math.ceil( %.1f ) == %d" % (value, math.ceil(value)))

value = -2
print("Math.ceil( %.1f ) == %d" % (value, math.ceil(value)))
"""
Math.ceil( 4.7 ) == 5
Math.ceil( 4.1 ) == 5
Math.ceil( 4.0 ) == 4
Math.ceil( 0.0 ) == 0
Math.ceil( -1.3 ) == -1
Math.ceil( -1.9 ) == -1
Math.ceil( -2.0 ) == -2
"""

#math.trunc(x)    il arrondi vers zéro. il est comme un milieu entre la fonction plancher floor() et la fonction plafond ceil().renvoi un entier
math.floor(-3.5)   #-4
math.trunc(-3.5)   #-3
math.ceil(-3.5)     #-3

print(math.trunc(-3.2) )  #-3
print(math.trunc(7.8) )  #7
print(math.trunc(0.0) )  #0


#math.floor(x)      il correspond a l'arrondi plancher. si on a un entier en parametre , la valeur de retour ne change pas.
Renvoie la valeur plancher de x, le plus grand entier plus petit ou egal à x. il renvoi un entier .

value = 4.7
print("Math.floor( %.1f ) == %d" % (value, math.floor(value)))

value = 4.1
print("Math.floor( %.1f ) == %d" % (value, math.floor(value)))

value = 4.0
print("Math.floor( %.1f ) == %d" % (value, math.floor(value)))

value = 0
print("Math.floor( %.1f ) == %d" % (value, math.floor(value)))

value = -1.3
print("Math.floor( %.1f ) == %d" % (value, math.floor(value)))

value = -1.9
print("Math.floor( %.1f ) == %d" % (value, math.floor(value)))

value = -2
print("Math.floor( %.1f ) == %d" % (value, math.floor(value)))
"""
Math.floor( 4.7 ) == 4
Math.floor( 4.1 ) == 4
Math.floor( 4.0 ) == 4
Math.floor( 0.0 ) == 0
Math.floor( -1.3 ) == -2
Math.floor( -1.9 ) == -2
Math.floor( -2.0 ) == -2
Math.floor( 4) == 4
"""

#math.factorial(x)      renvoie le factorielle de x. leve une erreur si x est negatif ou n'est pas entier
print(math.factorial(7))   #5040
print(math.factorial(0))  #1

#math.pow(x, y)   renvoie x élevé à la puissance y.
print(math.pow(-10, 2.56))
print(math.pow(100, 10))
print(math.pow(7))
"""
print(math.pow(-10, 2.56))
ValueError: math domain error

1e+20

print(math.pow(7))
TypeError: pow expected 2 arguments, got 1
"""

#math.sqrt(x)  revoie la racine carrée de x.
print(math.sqrt(25))
print(math.sqrt(0))
print(math.sqrt(-25))
"""
5.0
0.0
print(math.sqrt(-25))
ValueError: math domain error
"""
#math.hypot(x, y)   renvoie la longueur du vecteur allant de l'origine au point (x, y) en flottant. renvoie la norme euclidienne sqrt(x*x + y*y)
print(math.hypot(3, 4))
print(math.hypot(-3, -4))
print(math.hypot(-3, 4))
print(math.hypot(6, 6))
print(math.hypot(3))
print(math.hypot(0, 0))
"""
5.0
5.0
5.0
8.48528137423857
3.0
0.0
"""


#math.copysign(x,y)      renvoie un flottant contenant la magnitude(valeur absolu) de x mais avec le signe de y.
print(math.copysign(1.0, -0.0))   #result : - 1.0
print(math.copysign(2.3, -5.0))   #-2.3
print(math.copysign(2, -3.0))    #-2.0

#math.fabs(x)    renvoie la valeur absolue de x (renvoie un flottant)
print(math.fabs(-5))        #result(5.0)  different de abs(-5)=5 un entier


#math.fmod(x,y)   renvoie sous forme de flottant le modulus de x et y donnee. if x et y ==0 et si y==0 alors valueError. et typeError si x et y different de digit.
fmod est prefere pour manipuler les flottants .
print(math.fmod(4, 5))   #result 3.0
print(math.fmod(43.50, 4.5))   #result 4.0

#math.frexp(x)  
print(math.frexp(3))
print(math.frexp(15.7))
print(math.frexp(-15))
"""
renvoie la mantisse m et l'exposant e de x sous forme de tuple tel que X==m*2**e
sortie
(0.75, 2)
(0.98125, 4)
(-0.9375, 4)
"""
#math.fsum(itérable)  renvoie une somme flottante des valeurs dans l'iterable avec exactitude. fsum() est plus precis et exacte contrairement a sum().
print(math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))   #result 1.0   mais   sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])==0.999999999999

#math.gcg(*integers)  c'est le pgcd
print(math.gcd(44, 12))
print(math.gcd(69, 23))

#math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0) renvoie True si les valeurs a et b sont proches et False sinon. reltol>0 et abstol>=0
math.isclose(8.005, 8.450, abs_tol=0.4) 
math.isclose(8.005, 8.450, abs_tol=0.5)
"""
sortie1==> False because the two numbers have an absolute difference of 0.445, while threshold mentioned is 0.4
sortie2==> True because here the threshold given is 0.5
"""
#math.isfinite(x) renvoie true si x est fini et false sinon .0 est considere comme fini
print(math.isfinite(100))    #True
print(math.isfinite(10.05))    #True
print(math.isfinite(-14))         #True      
print(math.isfinite(float('inf')))    #False

#math.comb(n, k) . formule mathematique: n!/(k! * (n-k)!)
print(math.comb(5, 3))       #result 10

#math.isinf(x)     renvoie true si x vaut l'infini positif ou negatif et false sinon.                  
print(math.isinf(100))            #False

#math.isnan(x)       renvoie true si x is NaN(not a number) et false sinon.
print(math.isnan(100))         #False

#math.isqrt(n)      elle prend uniquement des entiers en paramètre et renvoie la partie entiere de la racine carree du parametre.
print(math.isqrt(100))         #result 10
print(math.isqrt(10))           #result 3

#math.lcm(*integers)      c'est le ppcm
print(math.lcm())
print(math.lcm(0, 23))
print(math.lcm(44, 12))
print(math.lcm(-69, 23))
print(math.lcm(0, 0))
"""
sortie:
1
0
132
69
0
 
"""
#math.ldexp(x, i)  renvoie x*(2**i): c'est l'inverse de la fonction frexp()
print(math.ldexp(3, 4))     #result 48

#math.modf(x) : renvoie la partie entiere et fractionnelle de x dans un tuple.les deux valeurs sont des flottants et ont le signe de x. la partie fractionelle <1.
print(math.modf(100.12))
print(math.modf(2))
print(math.modf(-100.72))
"""
sortie
(0.12000000000000455, 100.0)
(0.0, 2.0)
(-0.7199999999999989, -100.0)
"""

#math.nextafter(x, y)       renvoie la valeur flottante consecutive à x dans la direction de y. si x=y,renvoie y
print(math.nextafter(100, math.inf))
print(math.nextafter(100, -math.inf))
print(math.nextafter(100, 0.0))
"""
sortie
100.00000000000001
99.99999999999999
99.99999999999999
"""
#math.perm(n, k) n et k doivent etre entiers et positifs
print(math.perm(23, 86))
print(math.perm(23, 12))
print(math.perm(23))
print(math.perm(23, None))
"""
si k<=n, renvoie n!/(n-k)! et si k>n renvoie zéro
si k=none ou n'est pas defini, la fonction renvoie n!
sortie:
0
4151586700800
25852016738884976640000
25852016738884976640000
"""
#math.prod(iterable,*,start=1)  renvoie le produit de tous les elements de l'iterable
print(math.prod([4,5,6,9], start=1)) #1080     #la valeur de depart par defaut vaut 1
print(math.prod([], start=1))  #1  quand l'iterable est vide, renvoie la valeur de depart
print(math.prod([4,5,6,9]))   #1080
print(math.prod([4,5,6,9], start=5))  #5400

#math.remainder(x, y) # renvoie le reste de la division sous forme de flottant
print(math.remainder(23, 56))     #23.0
print(math.remainder(100, 12))        #4.0        


#math.ulp(x)
x = float('nan') 
print(math.ulp(x)) 
  
x = float('inf') 
print(math.ulp(x))  
print(math.ulp(-x)) 
  
x = 0.0
print(math.ulp(x)) 
  
x = 5
print(math.ulp(x)) 
  
x = -5
print(math.ulp(x)) 
"""
sortie:
nan
inf
inf
5e-324
8.881784197001252e-16
8.881784197001252e-16
"""
#math.exp(x)   renvoie e (e==2.718281) à la puissance x.
print(math.exp(4))
print(math.exp(-3))
print(math.exp(0.00))
"""
54.598150033144236
0.049787068367863944
1.0
"""

#math.expm1(x)
print(math.expm1(4))
print(math.expm1(-3))
print(math.expm1(0.00))
"""
53.598150033144236
-0.950212931632136
0.0
"""

#math.log(x[,base]) renvoie log de x en base e.
print(math.log(10))
print(math.log(100, 10))
print(math.log(0.00))
"""
2.302585092994046
2.0
print(math.log(0.00))
ValueError: math domain error
"""

#math.log1p(x)  renvoie log de 1+x en base e.
print(math.log1p(4))
print(math.log1p(-3))
print(math.log1p(0))
"""
1.6094379124341003
print(math.log2(0))
ValueError: math domain error

print(math.log1p(-3))
ValueError: math domain error
"""

#math.log2(x)   renvoie log de x en base 2.
print(math.log2(4))
print(math.log2(-3))
print(math.log2(0))
"""
2.0
print(math.log2(-3))
ValueError: math domain error

print(math.log2(0))
ValueError: math domain error

"""

#math.log10(x)  renvoie log de x en base 10.
print(math.log10(4))
print(math.log10(-3))
print(math.log10(0))
"""
0.6020599913279624
print(math.log10(-3))
ValueError: math domain error
"""


#math.acos(x)
print(math.acos(1))
print(math.acos(180))
"""
0.0

print(math.acos(180))
ValueError: math domain error
"""

#math.asin(x)
print(math.asin(1))   #1.5707963267948966

#math.atan(x)
print(math.atan(1))  #0.7853981633974483

#math.atan2(x, y)  renvoie atan(x/y)
print(math.atan2(1, 0))
print(math.atan2(-1, -1))
print(math.atan2(1, 1))
"""
1.5707963267948966
-2.356194490192345
0.7853981633974483
"""

#math.cos(x)
print(math.cos(180))   #-0.5984600690578581

#math.dist(p, q)   renvoie la distance entre les deux points p et q, ces points ayant la meme dimension.
print(math.dist([3, 4],[-3, 4]))
print(math.dist([-3, -4], [6, 6]))

"""
p et q sont des sequences ou itérables
6.0
13.45362404707371
"""

#math.sin(x)
print(math.sin(180))   # -0.8011526357338304

#math.tan(x)
print(math.tan(180))    #1.3386902103511544

#math.acosh(x)
print(math.acosh(1))    #0.0

#math.asinh(x)
print(math.asinh(1))     #0.8813735870195429

#math.atanh(x)
print(math.atanh(0.5))
print(math.atanh(1))
"""
0.5493061443340549
print(math.atanh(1))
ValueError: math domain error
"""

#math.cosh(x)
print(math.cosh(180))    #7.446921003909191e+77

#math.sinh(x)
print(math.sinh(180))          #7.446921003909191e+77

#math.tanh(x)
print(math.tanh(180))    #1.0

#math.degress(x)   convertit l'angle x de radians à degrees
print(math.degrees(0.58))     #33.231552117587746

#math.radians(x)        convertit l'angle x de degrees en radians
print(math.radians(180))    #3.141592653589793

#math.erf(x)
print(math.erf(0.67))
print(math.erf(180))
print(math.erf(-6))
"""
0.6566277023003051
1.0
-1.0
"""

#math.erfc(x)
print(math.erfc(0.67))
print(math.erfc(180))
print(math.erfc(-6))
"""
0.3433722976996949
0.0
2.0
"""


#math.gamma(x)    #renvoie la fonction gamma en x.
#math.lgamma(x)    #renvoie le logarithme de la valeur absolue de la fonction gamma en x.

#math.pi    renvoie la constante pi.
print(math.pi)    #3.141592653589793

#math.e         renvoie la constante e.
print(math.e)   #2.718281828459045

#math.inf  or  -math.inf       renvoie un flottant positif infini ou negatif infini
print(math.inf)   #inf
print(-math.inf)   -inf

#math.nan   renvoie un flottant valant NaN
print(math.nan)    #nan



#AUTRES EXEMPLES
import math
from math import *
#Que faut-il mettre à la place des ... pour que s'affiche le sinus de 30 degré ? 
angle=30
print(math.sin(angle))        #-0.9880316240928618
print(sin(radians(angle)))     #0.49999999999999994

#Que faut-il mettre à la place des ... pour que s'affiche pi arrondi à 0.000001 près
a=round(pi,6)
print(a)

#Créez un programme qui calcule pi carree et 2 puissance pi(même si vous ne savez pas comment on le calcule, Python sait) et affiche le plus grand deimport math
x=math.pi**2
print(x)        #9.869604401089358 

y=2**(math.pi)
print(y)      #8.824977827076287










































