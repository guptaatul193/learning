""" Using concepts from test4.py
	Count the number of objects created for a class"""

class Demo:

	cnt = 0 # declared a variable / static variable

	def __init__ (self):
		Demo.cnt += 1

a1 = Demo()
a2 = Demo()
a3 = Demo()
a4 = Demo()

print('Objects created = %s' %Demo.cnt)
# since we've created 4 objects, we'll get 4 0
