"""
Inheritance is a way of creating a new class for using details of an
existing class without modifying it. The newly formed class is a
derived class (or child class). Similarly, the existing class is a
base class (or parent class).
"""
class Grandfather:
	def lastName(self):
		print('Gupta')

class Father(Grandfather):
	def __init__(self):
		print('Father Object Created !!')
	def address(self):
		print('Pune, Maharashtra, India.')

class Daughter(Father):
	def __init__(self):
		print('daughter Object Created !!')
	def schoolName(self):
		print('DAV Public School')

class Son(Father):
	def __init__(self):
		print('Son Object Created !!')
	def schoolName(self):
		print('DPS')

f = Father()
d = Daughter()
s = Son()

s.address()
d.lastName()
