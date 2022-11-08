import random

#RANDOM.SEED() initialise le generateur des nombres aleatoires.
for i in range(5): 
  
    random.seed(0) 
  
    print(random.randint(1, 1000))  


random.seed(3) 
  
print(random.randint(1, 1000)) 
  
random.seed(3)  
print(random.randint(1, 1000)) 
  
  
print(random.randint(1, 1000)) 


#random.GETSTATE()  renvoie un objet capturant l'etat interne actuel du generateur.ne prend aucun parametre
#random.SETSTATE(state)  restaure letat interne du generateur qui a ete recupere par getstate.
 
list1 = [1, 2, 3, 4, 5, 6] 
     
# Get the state
state = random.getstate()
 
# prints a random value from the list
print(random.choice(list1))
   
# Set the state
random.setstate(state)
 
# prints the same random value
# from the list
print(random.choice(list1))

 
#random.GETRANDBYTES(n)    Generate n random bytes. renvoi des valeurs non nul
# import the random module
import random
  
# a random number with 4 bits
print(random.getrandbits(4))
  
# a random number with 16 bits
print(random.getrandbits(16))

#New example
# 5 random number with 4 bits
for i in range(4):
    print(random.getrandbits(4))


#random.RANDRANGE(stop)
#random.randrange(start, stop[, step])

# Using randrange() to generate numbers from 0-100
print ("Random number from 0-100 is : ",end="")
print (random.randrange(100))
 
# Using randrange() to generate numbers from 50-100
print ("Random number from 50-100 is : ",end="")
print (random.randrange(50,100))
 
# Using randrange() to generate numbers from 50-100
# skipping 5
print ("Random number from 50-100 skip 5 is : ",end="")
print (random.randrange(50,100,5))


#RANDOM.RANDINT(a, b)  renvoie un entier aleatoire N tel que a<=N<=b d'ou a et b sont inclus

#RANDOM.CHOICE(seq)   Renvoie un élément aléatoire de la séquence non vide seq. Si seq est vide, lève IndexError.

#RANDOM.CHOICES(population, weights=None, *, cum_weights=None, k=1)  Renvoie une liste de taille k d'éléments choisis dans la population avec remise. Si la population
est vide, lève IndexError.

mylist = ["bonjour", "le", "monde"]
print(random.choices(mylist, weights = [10, 1, 1], k = 5))

mylist = ["apple", "banana", "mango"]
print(random.choices(mylist, weights = [10, 1, 1], k = 6))


#RANDOM.SHUFFLE(x[, random])     Mélange la séquence x sans créer de nouvelle instance (« sur place »).
# x cest une sequence et le deuxieme parametre est facultatif cest une fonction et par defaut on a la fonction random()
sample_list = ['A', 'B', 'C', 'D', 'E'] 
  
print("Original list : ") 
print(sample_list) 
  
random.shuffle(sample_list) 
print("\nAfter the first shuffle : ") 
print(sample_list) 
  
random.shuffle(sample_list) 
print("\nAfter the second shuffle : ") 
print(sample_list)
"""
Original list : 
['A', 'B', 'C', 'D', 'E']

After the first shuffle : 
['A', 'C', 'E', 'B', 'D']

After the second shuffle : 
['B', 'E', 'C', 'A', 'D']
"""


#RANDOM.SAMPLE(population, k, *, counts=None)
"""
Renvoie une liste de k éléments uniques choisis dans la séquence ou l'ensemble de la population. Utilisé pour un tirage aléatoire sans remise.
Renvoie une nouvelle liste contenant des éléments de la population tout en laissant la population originale inchangée. 
Si la taille de l'échantillon est supérieure à la taille de la population, une ValueError est levée.
k : Une valeur entière, elle spécifie la longueur d’un échantillon.
Renvoie: k longueur nouvelle liste d’éléments choisis dans la séquence.
"""
# import random 
from random import sample
  
# Prints list of random items of given length
list1 = [1, 2, 3, 4, 5] 
  
print(sample(list1,3))     #[5, 3, 2]

# Prints list of random items of
# length 3 from the given list.
list1 = [1, 2, 3, 4, 5, 6] 
print("With list:", random.sample(list1, 3))       #With list: [6, 3, 1]
  
# Prints list of random items of
# length 4 from the given string. 
string = "GeeksforGeeks"
print("With string:", random.sample(string, 4))      #With string: ['e', 'G', 'o', 'e']
  
# Prints list of random items of
# length 4 from the given tuple.
tuple1 = ("ankit", "geeks", "computer", "science",
                   "portal", "scientist", "btech")
print("With tuple:", random.sample(tuple1, 4))         #With tuple: ['computer', 'btech', 'ankit', 'science']


#RANDOM.RANDOM()   Renvoie le nombre aléatoire à virgule flottante suivant dans la plage [0.0, 1.0).(See the opening and closing brackets, it means including 0 but excluding 1).
from random import random
  
lst = []
 
for i in range(10):
  lst.append(random())
   
# Prints random items
print(lst)    #[0.9051679947311476, 0.9772129950307277, 0.16428951817016524, 0.21353399177221577, 0.1926884330498041, 0.506970437851253, 0.3065764887319766, 0.016388967980367708, 0.06752680608201089, 0.06918680253060738]


#RANDOM.UNIFORM(a, b)  Renvoie un nombre aléatoire à virgule flottante N tel que a <= N <= b pour a <= b et b <= N <= a pour b < a
# initializing bounds 
a = 4
b = 9
  
# printing the random number
print("The random number generated between 4 and 9 is : ", end ="")
print(random.uniform(a, b))    #The random number generated between 4 and 9 is : 5.384919291618486

# for using uniform()
import random, math
  
# initializing player numbers
player1 = 4.50
player2 = 3.78
player3 = 6.54
  
# generating winner random number
winner = random.uniform(2, 9)
  
# finding closest 
diffa = math.fabs(winner - player1)
diffb = math.fabs(winner - player2)
diffc = math.fabs(winner - player3)
  
# printing winner
if(diffa < diffb and diffa < diffc):
    print("The winner of game is : ", end ="")
    print("Player1")
  
if(diffb < diffc and diffb < diffa):
    print("The winner of game is : ", end ="")
    print("Player2")
      
if(diffc < diffb and diffc < diffa):
    print("The winner of game is : ", end ="")
    print("Player3")


#RANDOM.TRIANGULAR(low, high, mode)
"""Renvoie un nombre aléatoire en virgule flottante N tel que low <= N <= high et avec le mode spécifié entre ces bornes.
Les limites low et high par défaut sont zéro et un. L'argument mode est par défaut le point médian entre les bornes, ce qui donne une distribution symétrique.
if the parameters are (10, 100, 20) then due to the bias, most of the random numbers generated will be closer to 10 as opposed to 100.
 Un biais statistique peut résulter d'un échantillonnage déséquilibré d'une population, ou d'un procédé d'évaluation qui ne donne pas un résultat précis en moyenne. 
Donc ici le biais est en faveur de 10
Example 2: If we generate the number multiple times we can probably identify the bias.
"""

# determining the values of the parameters
low = 10
high = 100
mode = 20
  
# using the triangular() method
print(random.triangular(low, high, mode))

# determining the values of the parameters
low = 10
high = 100
mode = 20
  
# running the triangular method with the
# same parameters multiple times
for i in range(10):
    print(random.triangular(low, high, mode))


#RANDOM.BETAVARIATE(alpha,beta)     Distribution bêta. Les conditions sur les paramètres sont alpha > 0 et beta > 0. Les valeurs renvoyées varient entre 0 et 1.
# determining the values of the parameters
alpha = 5
beta = 10
  
# using the betavariate() method
print(random.betavariate(alpha, beta))     #0.46373340389198414


#RANDOM.EXPOVARIATE(lambd)   Distribution exponentielle. lambd est 1,0 divisé par la moyenne désirée. Ce ne doit pas être zéro.
#Les valeurs renvoyées vont de 0 à plus l'infini positif si lambd est positif, et de moins l'infini à 0 si lambd est négatif.
  
# determining the values of the parameter
lambdaa = 1.5
  
# using the expovariate() method
print(random.expovariate(lambdaa))     #0.20572158960759088

#RANDOM.GAMMAVARIATE(alpha,bata)       Distribution gamma. (Ce n'est pas la fonction gamma !) Les conditions sur les paramètres sont alpha > 0 et beta > 0.
# determining the values of the parameter
alpha = 100
beta = 2
  
# using the gammavariate() method
print(random.gammavariate(alpha, beta))     #184.7624854901278  renvoie un float


#RANDOM.GAUSS(mu, sigma) Normal distribution, also called the Gaussian distribution. mu is the mean, and sigma is the standard deviation(ecart type). 
mu = 100
sigma = 50
  
# using the gauss() method
print(random.gauss(mu, sigma))         #79.89555114332347


#RANDOM.LOGNORMAVARIATE(mu, sigma)   Logarithme de la distribution normale. mu peut avoir n'importe quelle valeur et sigma doit être supérieur à zéro.
u = 0
sigma = 0.25
  
# using the lognormvariate() method
print(random.lognormvariate(mu, sigma))     #1.2385886711533018



#RANDOM.NORMALVARIATE(mu, sigma)   Distribution normale. mu est la moyenne et sigma est l'écart type.
u = 100
sigma = 50
  
# using the normalvariate() method
print(random.normalvariate(mu, sigma))            #117.5005785505917


#RANDOM.VONMISESVARIATE(mu, kappa)    mu est l'angle moyen, exprimé en radians entre 0 et 2*pi, et kappa est le paramètre de concentration, qui doit être supérieur ou égal à zéro.
#Si kappa est égal à zéro, cette distribution se réduit à un angle aléatoire uniforme sur la plage de 0 à 2*pi.
mu = 0
kappa = 4
  
# using the vonmisesvariate() method
print(random.vonmisesvariate(mu, kappa))          #0.950297260336497


#RANDOM.PARETOVARIATE(alpha)   Distribution de Pareto. alpha est le paramètre de forme.
alpha = 3
  
# using the paretovariate() method
print(random.paretovariate(alpha))     #1.6892036573559923


#RANDOM.WEIBULLVARIATE (alpha, beta)    Distribution de Weibull. alpha est le paramètre de l'échelle et beta est le paramètre de forme.
alpha = 1
beta = 1.5
  
# using the weibullvariate() method  
print(random.weibullvariate(alpha, beta))        #1.6149741071388848























































































