# PYTHON DOESN'T SUPPORT ABSTRACTION DIRECTLY WE HAVE TO IMPORT ABSTRACTION BASE CLASS (ABC)

from abc import ABC, abstractmethod
# Abstraction also prevent user to create an object of that class.

class vehicle(ABC):  

    @abstractmethod
    def go(self):
        pass

class car(vehicle):
    def go(self):
        print("you are driving a car")

class motocycle(vehicle):
    def go(self):
        print("your are driving a Motorcycle")

#v1 = vehicle()
car1 = car()
mc = motocycle()

#v1.go()
car1.go()
mc.go()