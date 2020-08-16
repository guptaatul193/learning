"""
Example 1: Input numbers: 2 4
The numbers are directly connected as follows on the graph. 2 is the largest factor of 4, other than itself.
We can also see that there is only on edge between them.
4 <--> 2
Hence the number of edges in shortest path is 1.
Output: 1

Example 2: Input numbers: 18 19
The graph for number 18 and 19 will look like this. Here we have 4 edges in the path.
18 <--> 9 <--> 3 <--> 1 <--> 19
Output: 4

Example 3: Input numbers: 9 9
The number of edges in shortest path is zero since the numbers correspond to the same node.
Output: 0

"""

n,m = map(int,sorted(input().strip().split()))

def getfactor(nm):
	for i in range(nm-1,1,-1):
		if nm % i == 0:
			return i
	return 1

def faclist(n):
	n_facs = [n]
	while n != 1:
		n_facs.append( getfactor(n) )
		n = n_facs[-1]
	return n_facs

n = (faclist(n))

if m in n:
	n = [i for i in n if i>=m]
	m = []
else:
	m = (faclist(m))

print(len(set(n).union(set(m)))-1 if n!=m else 0)
