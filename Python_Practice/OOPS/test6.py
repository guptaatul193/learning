""" using class methods as ALTERNATIVE CONSTRUCTORS """

""" suppose we've a use case, where we want to provide inputs in a different format
	for example -
	obj = Employee( 'Test', 'User', 30000 ) --> we don't want this way
	obj = Employee( classmethod('Test-User-3000') ) --> values separated by '-'

	Achieving above isn't possible using default constructor __init__"""

class Employee:

	def __init__( self, first, last, pay ):
		self.first = first
		self.last = last
		self.pay = pay

	def fullname( self ): # regular method
		return self.first + ' ' + self.last

	@classmethod #class method
	def from_string (cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls( first, last, pay )

# emp1 = Employee( 'Atul', 'Gupta', 40000 )
#emp2 = Employee( 'Test', 'User', 10000 )

emp1 = Employee.from_string( 'Atul-Gupta-40000' )
emp2 = Employee.from_string( 'Test-User-10000' )

print( emp1.fullname() )
print( emp2.fullname() )
