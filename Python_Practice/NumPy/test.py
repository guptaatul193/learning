"""
The first line contains the space separated values of N and M.
The next N lines contains the space separated elements of M columns.
First, print the transpose array and then print the flatten.

Sample Input

2 2
1 2
3 4
Sample Output

[[1 3]
 [2 4]]
[1 2 3 4]

"""

import numpy as np

n,m = map(int,input().split())

ar = np.array( [input().split() for i in range(n)] )

print(ar.transpose())
print(ar.flatten())
