""" What is the meaning of '_' and '__' in Python variable names? """
""" Encapsulation used here """

class Test:
	__sum = 0

	def __init__ (self):
		self.var1 = 11
		self._var2 = 23
		self.__var3 = 34 # python interpreter perform an action on double underscores.

	def disp(self):
			self.__sum += 1
			print(self.__sum)

class Test1(Test):
	pass

t = Test()
print( dir(t) )
""" In the list returned by dir(t), you'll see the list containing the attributes 'var1' and '_var2' as it is,
	but for '__var3', it'll be sufficed as '_Test__var3'
	This is a kind of a weak, but a way to protect the accidental variable value to change in the course of inheritance.
	"""
t1 = Test1()
print('---------------')
print(t1.var1) # this'll work as 'var1' is inherited from parent class 'Test'
print(t1._var2) # this'll work as '_var2' is inherited from parent class 'Test'
# print(t1.__var3) # this'll NOT work as '__var3' in the parent class 'Test' has it defined as '_Test__var3'. Name changed, value saved from accidental change
print(t1._Test__var3) # finally, instead of the above statement, this'll work as we're giving the exact attribute name '_Test__var3'


ob = Test()
ob.disp()
ob.disp()
print(ob._Test__sum)
#print(ob.__sum) # this will give error
