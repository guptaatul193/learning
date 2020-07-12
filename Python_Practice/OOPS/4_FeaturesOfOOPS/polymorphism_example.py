"""
Polymorphism is an ability (in OOP) to use a common interface for multiple
forms (data types).
Suppose, we need to color a shape, there are multiple shape
options (rectangle, square, circle).
However we could use the same method to color any shape.
This concept is called Polymorphism.
"""

class Yamaha:

    def fly(self):
        print("Manufacturers don't make flying products")

    def wheels(self):
        print("Has 2 wheels")

class Airbus:

    def fly(self):
        print("Manufacturers make aircrafts")

    def wheels(self):
        print("Has more than 2 wheels")

# common interface
def flying_test(company):
    company.fly()

#instantiate objects
fzs = Yamaha()
a320 = Airbus()

# passing the object
flying_test(fzs)
flying_test(a320)
