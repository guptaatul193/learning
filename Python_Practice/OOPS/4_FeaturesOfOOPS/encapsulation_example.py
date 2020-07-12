"""
Encapsulation is achieved when each object keeps its state private,
inside a class. Other objects don’t have direct access to this state.
Instead, they can only call a list of public functions — called methods.
So, the object manages its own state via methods — and no other class
can touch it unless explicitly allowed. If you want to communicate with
the object, you should use the methods provided.
But (by default), you can’t change the state.
"""

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1200)
c.sell()
