"""
You are given two integer arrays, A and B of dimensions N X M.
Your task is to perform the following operations:

Add ( + )
Subtract ( - )
Multiply ( * )
Integer Division ( / )
Mod ( % )
Power ( ** )


Sample Input

1 4
1 2 3 4
5 6 7 8

Sample Output

[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]]
"""

import numpy as np

n, m = map(int, input().split())

a, b = (np.array([input().split() for _ in range(n)],
             dtype=int) for _ in range(2))

print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')
