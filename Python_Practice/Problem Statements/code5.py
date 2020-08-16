"""
There is a cube of height H, and there are 4 moving particles on the vertical edges of the cube.
Initially particles are at some height A, B, C and D respectively. These particles are moving in
different direction (Only upward or downward, no sideways movement) with different speed.
If the particle is moving upward or downward reaches the tip of the cube then it remain at the tip
only and will not move further. If other particles have not reach the tip they continue to move along
their respective edges in their respective direction till the last particle reaches the tip.
These 4 particles will make two triangles in a 3-D plane. Since the particles are moving, sum of
the area of these two triangles will change every moment.
Find out the maximum and minimum of the sum of the areas of these two triangles.
Refer the Examples section for better understanding.

Example 1
Input
10
5 5 5 5
1 1 1 1
U U D D
Output
80000 40000

MAXAREA = [4 * [Max (sum of area of triangle ABC and area of triangle ADC)]**2 ]
MINAREA = [4 * [Min (sum of area of triangle ABC and area of triangle ADC)]**2 ]



"""

import numpy as np

class Coordinates:
	def __init__( self, x,y,z, d, side ):
		self.x = x
		self.y = y
		self.z = z
		self.d = d
		self.side = side
		self.reached = (self.z>=side or self.z<=0)

	def __str__( self ):
		return('%d, %d, %d --> %d %r' %(self.x, self.y, self.z, self.d, self.reached))

	def move(self):
		if not self.reached:
			self.z += self.d
		if (self.z>=self.side or self.z<=0):
			self.z = self.side if self.d>0 else 0
			self.reached = True

	def get(self):
		return [self.x, self.y, self.z]

def direc(cr,st):
	return cr if st.strip().upper() == 'U' else (cr*-1)

def move_all():
	c1.move()
	c2.move()
	c3.move()
	c4.move()

def area_tri(crd):
	a,b,c = map( lambda x:np.array(x), crd )
	area_poly = np.linalg.norm( np.cross( b-a , c-a ) )
	return area_poly/2

side = int(input())
initial = list(map(int, input().split()))
mv = list(map(int,input().split()))
dir = input().split()

c1 = Coordinates(0,0,initial[0],direc(mv[0],dir[0]),side)
c2 = Coordinates(side,0,initial[1],direc(mv[1],dir[1]),side)
c3 = Coordinates(side,side,initial[2],direc(mv[2],dir[2]),side)
c4 = Coordinates(0,side,initial[3],direc(mv[3],dir[3]),side)

ar_sum = []

while not (c1.reached and c2.reached and c3.reached and c4.reached):
	i = [[c1.get(),c2.get(),c3.get()],[c1.get(),c2.get(),c4.get()]]
	ar_sum.append( sum( list(map( area_tri, i )) ) )
	move_all()
i = [[c1.get(),c2.get(),c3.get()],[c1.get(),c2.get(),c4.get()]]
ar_sum.append( sum( list(map( area_tri, i )) ) )

print( 'MaxArea --> %d' %int(4 * (max(ar_sum)**2)) )
print( 'MinArea --> %d' %int(4 * (min(ar_sum)**2)) )
