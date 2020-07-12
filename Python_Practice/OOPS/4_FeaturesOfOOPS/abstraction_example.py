"""
An abstract class can be considered as a blueprint for other classes.
In simple terms, the child class' skeleton must have all the methods
names similar to the skeleton of methods of an abrstract class.
The code doesn't compile if there's a skeleton difference.

Python doesn't support abstract classes and methods, so 
class abc (Abstract Base Class) needs to be imported explicitally to achieve the same.


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

# ABC class is imported in this class, hence this is an abstract class, and atleast 1 abstract method must be defined within.
class Polygon(ABC):

    @abstractmethod
    def noofsides(self): # the decorator makes it the abstract method. We cannot make any object for this class at it's an Abstract class now.
        pass            # Also, all the child classes now MUST have a function with a similar name

class Triangle(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")
    def test(self): # we can have more methods in addition to an abstract method, but having all abstract methods as in the parent/abstract class is important
        print('this is a test statement in Triangle class')

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
R.test()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()
