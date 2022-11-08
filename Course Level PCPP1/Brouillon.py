

'''
class TimeInterval:
    def __init__(self, hours, minutes, seconds ):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return str(self.hours)+' : '+str(self.minutes)+' : '+str(self.seconds)

    def addition (self):
        pass

    def subtraction (self):
        pass

    def multiplication(self, val):
        pass
'''

class Scanner:
    pass

    def scan(self):
        print('scan() method from Scanner class')

class Printer:
    pass

    def print(self):
        print('print() method from Printer class')

class Fax:
    pass

    def send(self):
        print('send() method from Fax class')

    def print(self):
        print('print() method from Fax class')

class MFD_SPF(Scanner, Printer, Fax):
    pass

class MFD_SFP(Scanner, Fax, Printer):
    pass

obj1 = MFD_SPF()
obj2 = MFD_SFP()

obj1.scan()
obj1.print()
obj1.send()

obj2.scan()
obj2.print()
obj2.send()











































































































































































