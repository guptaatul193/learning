"""
An abstract class can be considered as a blueprint for other classes.
It allows you to create a set of methods that must be created within
any child classes built from the abstract class. A class which contains
 one or more abstract methods is called an abstract class. An abstract
 method is a method that has a declaration but does not have an
 implementation. While we are designing large functional units we
 use an abstract class. When we want to provide a common interface
 for different implementations of a component, we use an abstract class.
"""

# Python program showing
# abstract base class work

from abc import ABC, abstractmethod

class Polygon(ABC):

    # abstract method
    def noofsides(self):
        pass

class Triangle(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")

class Pentagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")

class Hexagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")

class Quadrilateral(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")

# Driver code
R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()
