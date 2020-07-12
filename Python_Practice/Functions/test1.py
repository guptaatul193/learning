""" First-class functions 
A function is an instance of the Object type.
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists,
"""

def func1():
	msg = 'Hello'

	def inner_func():
		print(msg)

	return inner_func()

def func2():
	msg = 'There'

	def inner_func():
		print(msg)

	return inner_func

func1()
var_func2 = func2() # func2() is a first class function, and is stored liek an object in the variable var_func2
var_func3 = func2() # func2() is a first class function, and is stored liek an object in the variable var_func3

var_func2()
var_func3()
