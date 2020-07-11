class Base:
	t2 = 0
	def __init__ (self,num):
		self.n1 = num

class Child(Base):
	def __init__(self,num):
		self.n2 = num
		self.t2 += 1

oc = Child(12)
print(oc.t2, oc.n2)

ob = Base(12)
print(ob.t2, ob.n1)