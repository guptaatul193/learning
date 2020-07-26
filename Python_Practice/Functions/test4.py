"""
******* FUNCTION OVERLOADING CODE ********

METHOD OVERLOADING
* methods or functions must have the same name and different signatures.
* inheritance may or may not be required.
* there is no need of more than one class

METHOD OVERRIDING
* methods or functions must have the same name and same signatures.
* inheritance always required
* there is need of at least of two classes


Refer to -
https://www.geeksforgeeks.org/difference-between-method-overloading-and-method-overriding-in-python/

"""

class Test:

	def test(self,*a):
		if len(a) == 0:
			print(a)
		else: print( sum(a) )

t = Test()

t.test(1,2)
t.test(1,2,3)
