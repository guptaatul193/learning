# illustration of MGIC METHODS in classes.. __init__, __str__, __del__, __add__

''' MAGIC methods or DUNDER methods have their own functionality by default, but can over-rided
	in the class '''

class Demo:

# over-riding '__init__' / constructor method is optional only if
# 'NO' arguments is passed while creating an object of a class
	def __init__(self): # '__init__' is magic method for constructor
		print('-----object created------')

# over-riding '__str__'. If not over-rided, the 'str' related print statements will
# print something like '<__main__.Demo object at 0x000001D7F59F2208>'
	def __str__ (self):
		return 'Hello %s !!' %self.name

# over-riding '__del__'. If not over-rided, the del( <obj name> ) related print
# statements will delete the specified object and we have no feedback.
	def __del__(self):
		print('------object deleted-------')

	def getVal(self, name, marks1, marks2):
		self.name = name
		self.marks1 = marks1
		self.marks2 = marks2

	def __add__(self,o2):
		return self.marks1 + self.marks2 + o2.marks1 + o2.marks2


o1 = Demo()
o2 = Demo()
# please note that passing arguments to the above statements will fail the code
# reason being '__init__' doesn't accept any arguments
# even if '__init__' wasn't over-rided, the code will fail as it doesn't accept any arguments by default

o1.getVal('Atul',10,20)
o2.getVal('Test',30,40)

# below prints will works alike, it's just the object names are different, hence diff. O/P
print( o1.__str__() )
print( str(o2) )

# '__add__' (corresponding to '+' operator) is over-loaded to add marks1 and marks2 of the 2 objects specified
# exception 'TypeError: unsupported operand type(s) for +: 'Demo' and 'Demo' ' is obtained if __add__ not defined
print( o1 + o2 )

""" BONUS explanation on '__add__'
When we execute 'print( 3 + 2 )', we get 5 as output, but
when we execute 'print( 'a' + 'b' )', we get 'ab' as output
Same operator, different functionality. but WHY ?????

'print( 3 + 2)' can alternatively be represented as 'int.__add__(1,2)' where it does obvious integer operation
this is something pre-defined in the BUILT-IN class int

similarly, 'print( 'a' + 'b' )' calls 'str.__add__('a', 'b')', where again, it concatenates the string values

This is OPERATOR OVERLOADING with the operator '+' """
