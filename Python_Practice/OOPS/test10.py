"""
'new-style' vs 'classic' class in Python
Please obseve in the below code that we've made 'object' as a parameter to the class 'Base'.
In Python2 this declares a class to be a new-style class (as opposed to "classic" class).
In Python3 all classes are new-style classes, so this is no longer necessary.
New style classes have a few special attributes that classic classes lack.

Also, make sure to look into the last lines of code to understand inheritance in OOPS.

"""


class Base(object):
	t2 = 0
	def __init__ (self,num):
		self.n1 = num

class Child(Base):
	def __init__(self,num):
		self.n2 = num

oc = Child(12)
oc.t2 = 100
print(oc.t2, oc.n2)

ob = Base(12)
print(ob.t2, ob.n1)

Base.t2 = 1000
print(oc.t2, ob.t2, Base.t2, Child.t2)
