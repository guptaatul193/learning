"""
x,y,z --> dimensions of a cuboid
n --> another integer user input
Task:
Find all the coordinates whose sum is NOT equal to n.

"""
from itertools import permutations, product

if _name_ == '_main_':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())


    maxi = int(''.join( [str(i) for i in  max(permutations([x,y,z],3))] ))

    lst = valid( product( range(maxi+1) , repeat = 3 ) , x,y,z )

    print( [ list(i) for i in lst if sum(i) != n ] )
