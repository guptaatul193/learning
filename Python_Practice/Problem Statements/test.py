"""
Problem Statement:
1. Get comma-separated user input
2. If there are 2 or more values that are equal to the avg of all nos collectively, print
	distance between them ( number of values lying amid ).
3. If 1 or none, print -1.

"""


import sys
from statistics import mean

try:
	num = [int(i) for i in input('Please enter values: ').strip().split(',')]
except:
	print(-1)
	sys.exit()

avg = mean(num)

if num.count(avg) <= 1:
	print(-1)
else:
	tmp = []
	for i,j in enumerate(num):
		if j == avg:
			tmp.append(i)
	print(max(tmp)-min(tmp))
