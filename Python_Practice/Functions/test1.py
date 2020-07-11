""" First-class functions """

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
var_func2 = func2()
var_func3 = func2()

var_func2()
var_func3()
