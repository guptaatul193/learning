"""
A double underscore prefix causes the Python interpreter to rewrite the attribute name
in order to avoid naming conflicts in subclasses.

This is also called NAME MANGLING — the interpreter changes the name of the variable
in a way that makes it harder to create collisions when the class is extended later.
"""


class Test:
	__sum = 0
	def disp(self):
			self.__sum += 1
			print(self.__sum)

ob = Test()
ob.disp()
ob.disp()
print(ob._Test__sum)
