class Test:
	__sum = 0
	def disp(self):
			self.__sum += 1
			print(self.__sum)

ob = Test()
ob.disp()
ob.disp()
print(ob._Test__sum)
