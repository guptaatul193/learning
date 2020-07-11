""" INHERITANCE - creating subclasses
	Employee class has properties that is common among the classes
	Developer and Manager. So we're inheriting Employee into both."""

class Employee:

	raise_amt = 1.04

	def __init__( self, first, last, pay ):
		self.first = first
		self.last = last
		self.pay = pay

	def fullname( self ):
		return self.first + ' ' + self.last

	def applyRaise(self):
		self.pay *= self.raise_amt
"""please mind that for child classes that DON'T have this method, the blow approach will be followed for 'self.raise_amt'
	1. instance variable present? (NO in case of Manager)
	2. class variable present? (NO in case of manager)
	3. parent class has any class variable with the same name? (yes, in class EMPLOYEE)"""

class Manager(Employee):
	def fullname(self):
		return '%s, %s' %(self.last, self.first)

class Developer(Employee):
	raise_amt = 1.1

	def __init__( self, first, last, pay , language):
		# self.first = first
		# self.last = last
		# self.pay = pay
		super().__init__(first, last, pay) # 'super()' forces python to use the parent class level attributes
								# hence we can skip using the above 3 commands as they've already been used in the parent class
		self.language = language


dev1 = Developer( 'Atul', 'Gupta', 40000, 'python' ) # this uses __init__ in the Developer class itself, since it's there for the class
manager1 = Manager( 'Test', 'User', 10000 ) # no __init__ for this class, hence it'll use the one present in the parent class Employee


# priority is always given to the same class methods, but if not present, inherited classes are looked for
# this is applicable for magic methods mike '__init__' as well
print( dev1.fullname() ) # fullname() isn't in classes Developer, but gets inherited from the parent class Employee
print( manager1.fullname() ) # fullname() present in classes Manager, hence THAT method comes into action

dev1.applyRaise() # applyRaise() used from parent class Employee, but raise_amt used from the Developer class' attribute 
manager1.applyRaise() # applyRaise and raise_amt attributes used from the parent class Employee
print('-----------')
print(manager1.pay)
print(dev1.pay)
print(dev1.language)
print('-----------')
print(isinstance(manager1, Manager)) # true, obviously
print(isinstance(manager1, Employee)) # true, since manager1 being instance of Manager class, is indirectly instance of the parent class Employee
print(isinstance(manager1, Developer)) # False, obviously
print('-----------')
print(issubclass(Manager, Employee)) # true
print(issubclass(Developer, Employee)) # true
print(issubclass(Manager, Developer)) # false
