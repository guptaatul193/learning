""" difference between
	1. REGULAR METHODS - these accept OBJECT names as the first parameter by default
	2. CLASS METHODS - these accept CLASS names as the first parameter by default.
				We use the decorator '@classmethod' for this just before the method declaration.
	3. STATIC METHODS - they don't pass anything automatically.. they just behave like
				any regular/normal function, except that it's inside a class
				and don't operate on class or instance.
				We use '@staticmethod' for this just before the method declaration"""

class Employee:

	raise_amt = 1.04

	def __init__( self, first, last, pay ):
		self.first = first
		self.last = last
		self.pay = pay

	def fullname( self ): # regular method
		return self.first + ' ' + self.last # 'self' here stores the instance details

	@classmethod # class method
	def set_raise_amt (cls, amount): # 'cls' here will have the class details
		cls.raise_amt = 1.05

	@staticmethod
	def printValue(): # this method doesn't need CLASS or INSTANCE details as 1st parameter. In fact, passing any parameter to this is optional.
		print('Static method executed')

	@staticmethod
	def printValue2(val):
		print(val)


emp1 = Employee( 'Atul', 'Gupta', 40000 )
emp2 = Employee( 'Test', 'User', 10000 )

# print( emp1.fullname() )
print(Employee.fullname(emp1)) # altername way to achieve as the above command

#print( 'Raise amount BEFORE : %s' %emp1.raise_amt )
#print( 'Raise amount BEFORE : %s' %emp2.raise_amt )
print('Raise amount BEFORE : %s' %Employee.raise_amt) #above 2 command will do the same thing, since none of the instances of class Employee has any attrib names 'raise_amt'

# Employee.raise_amt = 1.05
Employee.set_raise_amt(1.05) # the above command will do the same thing as this statement

# alternate to above statement, we can use the below statements, but it doesn't make much sense, and people don't usually do it.
#emp1.set_raise_amt( 1.05 )
#emp2.set_raise_amt( 1.05 )

print('Raise amount AFTER : %s' %Employee.raise_amt)
print('-----------------------')

Employee.printValue() # below statements will do the same as this statement, but again, calling class or static method with help of instance variable doesn't make sense
#emp1.printValue()
#emp2.printValue()


Employee.printValue2('2nd Static method with parameter passed')
