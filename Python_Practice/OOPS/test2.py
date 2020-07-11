""" in the below complete code, please mind at all the steps that..
	'self' will always look for instance level attributes, if not present
	it'll look for the class attributes, if still not present
	it'll look for the parent class' attributes, if still not present
	we get exception error."""
class Demo:

	glob_var = 'Hello' #this is a static variable / class variable.. this becomes a part of class attributes
	glob_var2 = 'I am alone !!' #this is another static variable / class variable

	def __init__(self,st):
		self.glob_var = st
	""" the constructor creates new 'glob_var' ATTRIBUTE for every instance of class created
	 	Hence, the static / class 'glob_var' variable value remains intact"""

	def change_static(self,st):
		Demo.glob_var = st

	def change_ins(self,st):
		self.glob_var = st

	def prnt_static(self):
		print(Demo.glob_var)

	def prnt_ins (self):
		print(self.glob_var)

# create instance of class Demo.
# Please mind that constructor method is executed along the instance creation
obj1 = Demo('object created')

# the below set of PRINT statements will print STATIC 'glob_var' value
print(Demo.glob_var)
obj1.prnt_static()

print('--------------')

# the below set of PRINT statements will print the 'glob_var' value for the instance 'obj1'
print(obj1.glob_var) # if glob_var was not defined for this instance, the static / global 'glob_var' whould have been referred
obj1.prnt_ins()
print('--------------')

# will now pass an argument to change the value of 'glob_var'.
# Please mind that instance value is changed, and the static value remains intact.
# Will repeat print statements for instance after that
obj1.change_ins('new value passed') # this will act the same as " obj1.glob_var = 'new value passed' "
print(obj1.glob_var)
obj1.prnt_ins() # we get 'new value passed'
obj1.prnt_static() # we get the static value, i.e 'Hello'
print('--------------')

# will change the static value explicitly, and repeat the prints
Demo.glob_var = 'changing value explicitly'
obj1.prnt_static() # this will print 'chaning value explicitly'
obj1.prnt_ins() # this will print 'new value passed', which was the last modified value (obj1)
print('--------------')

# Alternate to above..
# will change the static value explicitly, and repeat the prints
obj1.change_static('changing value explicitly TWICE !!!')
obj1.prnt_static() # this will print 'chaning value explicitly'
obj1.prnt_ins() # this will print 'new value passed', which was the last modified value (obj1)
print('--------------')

# below prints value of STATIC glob_var2 as the instance itself doesn't have one for its own.
print(obj1.glob_var2)
""" priority is always given to instance attribute.. if not present, Python looks for
 	the same or inherited class' static static variable"""
print('--------------')

""" below statements converts classes into dictionaries, that provide us
 	all the attributes associated with a CLASS or IT'S OBJECT"""
print(Demo.__dict__)
print('--------------')
print(obj1.__dict__)
print('--------------')
