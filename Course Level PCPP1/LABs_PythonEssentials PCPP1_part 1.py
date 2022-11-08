#LAB 1:
Scenario

    create a class representing a mobile phone;
    your class should implement the following methods:
        __init__ expects a number to be passed as an argument; this method stores the number in an instance variable self.number
        turn_on() should return the message 'mobile phone {number} is turned on'. Curly brackets are used to mark the place to insert the object's number variable;
        turn_off() should return the message 'mobile phone is turned off';
        call(number) should return the message 'calling {number}'. Curly brackets are used to mark the place to insert the object's number variable;
    create two objects representing two different mobile phones; assign any random phone numbers to them;
    implement a sequence of method calls on the objects to turn them on, call any number. Print the methods' outcomes;
    turn off both mobiles.
class MobilePhone:
    def __init__(self, number):
        self.number = number

    def turn_on(self):
        return f'mobile phone {self.number} is turned on'

    def turn_off(self):
        return 'mobile phone is turned off'

    def call(self, number):
        return f'calling {number}'

mobile1 = MobilePhone(3698521478)
mobile2 = MobilePhone(5697139823)

print(mobile1.turn_on())
print(mobile2.turn_on())
print(mobile1.call(6874165462))
print(mobile1.turn_off())
print(mobile2.turn_off())



#LAB 2
Scenario

Imagine that you receive a task description of an application that monitors the process of apple packaging before the apples are sent to a shop.

A shop owner has asked for 1000 apples, but the total weight limitation cannot exceed 300 units.

Write a code that creates objects representing apples as long as both limitations are met. When any limitation is exceeded, than the packaging process is stopped, and your application should print the number of apple class objects created, and the total weight.

Your application should keep track of two parameters:

    the number of apples processed, stored as a class variable;
    the total weight of the apples processed; stored as a class variable. Assume that each apple's weight is random, and can vary between 0.2 and 0.5 of an imaginary weight unit;

Hint: Use a random.uniform(lower, upper) function to create a random number between the lower and upper float values.
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


#LAB
Scenario

    Your task is to build a multifunction device (MFD) class consisting of methods responsible for document scanning, printing, and sending via fax.
    The methods are delivered by the following classes:
        scan(), delivered by the Scanner class;
        print(), delivered by the Printer class;
        send() and print(), delivered by the Fax class.
    Each method should print a message indicating its purpose and origin, like:
        'print() method from Printer class'
        'send() method from Fax class'
    create an MFD_SPF class ('SPF' means 'Scanner', 'Printer', 'Fax'), then instantiate it;
    create an MFD_SFP class ('SFP' means 'Scanner', 'Fax', 'Printer'), then instantiate it;
    on each object call the methods: scan(), print(), send();
    observe the output differences. Was the Printer class utilized each time?



#LAB 3        
Scenario A

    Create a class representing a time interval;
    the class should implement its own method for addition, subtraction on time interval class objects;
    the class should implement its own method for multiplication of time interval class objects by an integer-type value;
    the __init__ method should be based on keywords to allow accurate and convenient object initialization, but limit it to hours, minutes, and seconds parameters;
    the __str__ method should return an HH:MM:SS string, where HH represents hours, MM represents minutes and SS represents the seconds attributes of the time
    interval object;
    check the argument type, and in case of a mismatch, raise a TypeError exception.


hint1: just before doing the math, convert each time interval to a corresponding number of seconds to simplify the algorithm;
    for addition and subtraction, you can use one internal method, as subtraction is just ... negative addition.

Test data:

    the first time interval (fti) is hours=21, minutes=58, seconds=50
    the second time interval (sti) is hours=1, minutes=45, seconds=22
    the expected result of addition (fti + sti) is 23:44:12
    the expected result of subtraction (fti - sti) is 20:13:28
    the expected result of multiplication (fti * 2) is 43:57:40


hint2: you can use the assert statement to validate if the output of the __str__ method applied to a time interval object equals the expected value.






Scenario B

    Extend the class implementation prepared in the previous lab to support the addition and subtraction of integers to time interval objects;
    to add an integer to a time interval object means to add seconds;
    to subtract an integer from a time interval object means to remove seconds.


hint: in the case when a special method receives an integer type argument, instead of a time interval object, create a new time interval object based on the integer value.

Test data:

    the time interval (tti) is hours=21, minutes=58, seconds=50
    the expected result of addition (tti + 62) is 21:59:52
    the expected result of subtraction (tti - 62) is 21:57:48























