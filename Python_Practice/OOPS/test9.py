""" Property Decorators --> Getters, Setters and Deleters"""

class Employee:

	def __init__( self, first, last ):
		self.first = first
		self.last = last
		self.email = "%s.%s@email.com" %(first,last)

	def fullname( self ):
		return self.first + ' ' + self.last

	@property #getter
	def fullname2( self ):
		return "%s, %s" %(self.last, self.first)

	@fullname2.setter # setter
	def fullname2( self, name ):
		last, first = name.split(', ')
		self.first = first
		self.last = last

	@fullname2.deleter # deleter. PLease mind that we can perform this using SETTER as well, but since it was already defined for the other task, we use a deleter, plus it doesn't make sense not to use a deleter for this purpose.
	def fullname2( self ):
		print( 'Delete Name !' )
		self.first = None
		self.last = None

emp1 = Employee( 'Test', 'User' )

print( emp1.first )
print( emp1.email )
print( emp1.fullname() )

emp1.first = 'Jack'
print('---------------')
print( emp1.first )
print( emp1.email ) # we've changed emp1.first, but email still reflects with previous name.
print( emp1.fullname() )

""" To handle this, we can get email in the way similar to 'fullname', but that's a method.
	Using these conventions, we'll have to remember what's variable and what's method.
	Using GETTERS and SETTERS (concept used in other programming languages like Java) help us in this case """

print('--------------')
print(emp1.fullname2) # we call getters similar to the way referring to a class/instance variable

print('--------------')
emp1.fullname2 = 'Sparrow, Jack' # will call setter, and change the class attribute appropriately.. please mind that this works just like referring to a class/instance variable
print( emp1.first )
print( emp1.fullname() )

print('--------------')
del emp1.fullname2
print(emp1.first)
print(emp1.last)
print(emp1.email) # this'll print 'Test.User@email.com' since it was already was set in the VERY beginning, and it never reffers to any class attribute thereafter
# print(emp1.fullname()) # this'll give error as fullname() performs action on strings, and it's getting 'None' instead
