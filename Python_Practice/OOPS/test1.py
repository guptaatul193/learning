# below code uses constructor, string representation, and destructor
class demo:
	#var = None
	def __init__(self, val):
		print('------object created-----%s-----  ' %'')
		self.var = val
	def __str__(self):
		out = ['value = '+self.var]
		out.append( 'class_name = '+self.__class__.__name__ )
		return ('\n').join(out)+'\n'
	def __del__(self):
		print('-----object destroyed-------')

p1 = demo('bunny')

# different ways to get string representation values
print( demo.__str__(p1) )
print( p1 ) # this will print the same output as above
print (p1.__str__()) # this will print the same output as above
