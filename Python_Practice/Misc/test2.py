""" get a list of nos. from user and refine it with perfect squares.
	Calculate fibonacci of the refined list.
	If a number doesn't end with 0, print as it is, else remove all zeros from end and extract the last 3 digits. """

import sys
from math import modf

try: num = [int(i) for i in input('Please enter numbers : ').strip().split(',')]
except:
	print(-1)
	sys.exit()

def fac(nm):
	fac = 1
	for j in range (1,nm+1): fac *= j
	return fac

facs = list (map( fac, filter( lambda x: modf(x**0.5)[0]==0, num ) ) )

out = list (map( lambda x: x if (x % 10) != 0 else int(str(x).strip('0'))%1000, facs ) )

print( -1 if len(out)==0 else out )
