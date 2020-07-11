"""
WHY to use NumPy?
1. Faster than python lists.
2. A lot more calculative applications like MATLAB replacement, Matplotlib, Machine Learning
 """

import numpy as np

b = np.array([[1,2,3],[3,4,5]])

print('Array Dimention = ',b.ndim)
print('Array Shape = ',b.shape)
print('Data Type = ',b.dtype)
print('Size of each item = ',b.itemsize)
print('Number of items = ',b.size)
print('Total bytes occupied = ',b.nbytes) # basically ( b.size x b.itemsize )

print('\n----------------------------------------\n')

# Getting specific elements, rows, columns etc..
a = np.array([1,2,3])
print('a = ',a)
# print('a[1,3] = ', a[1,3])  # IndexError: a is 1-dimentional np array, but more than expected params have been passed
# print('b[1,3] = ', b[1,3])  # IndexError: index out of bounds for b
print('b[1,2] = ', b[1,2])
print('Get all comtents of 1st row in b = ',b[0,:])
print('Get all comtents of 1st col in b = ',b[:,0])
print('\n----------------------------------------\n')


# Changing np array elements
b[1,2] = 99
print('b = ',b)
b[:,0] = 121 # changes 'ALL' the 1st col values to 121
print('b = ',b)
print('\n----------------------------------------\n')

# All FIXED-VALUE metrics
temp = np.zeros( (4,5,6) ) # this creates an numpy array of the specified dimention, all values being 0
temp1 = np.ones( (4,5,6) ) # this creates an numpy array of the specified dimention, all values being 1
temp_n = np.full( (4,5,6) , 116 ) # this creates an numpy array of the specified dimention, all values being 116 (user specified)
# temp_n = np.full( temp.shape, 116 ) # this will work the same as the above statement
# temp_n = np.full_like( temp, 116 ) # this will work the same as the above statement
print(temp)
print('\n----------------------------------------\n')

#All RANDOM values metrics (decimals)
temp_rand = np.random.rand( 4,5,6 ) # please note that unlike previous cases, random.rand doesn't accept TUPLES as parameter, and we can pass in the dimensions directly
temp_rand1 = np.random.random_sample( temp.shape ) # this works the same as the above statement
print(temp_rand1)
print('\n----------------------------------------\n')

# All RANDOM values metrics (integers)
temp_rand_int = np.random.randint( -2,5, size=(2,2,2) ) # -2 is the start value, 5 is the max/end value (self-excluded)
print( temp_rand_int )
print('\n----------------------------------------\n')

# Identity Matrix
print(np.identity(5))
print('\n----------------------------------------\n')

# Repeat an Array.. observe outputs for difference between axis 1 and 2
arr = np.array( [ [ 1,2,3 ], [5,6,7] ] )
r1 = np.repeat( arr, 3, axis=1 )
r2 = np.repeat( arr, 3, axis=0 )
print( r1 )
print( r2 )
print('\n----------------------------------------\n')

# copy numpy metrics
a = np.array( [1,2,3] )
# b = a # avoid using this, as this points the objects to the same memory location
b = a.copy() # us this instead of using the above statement

print('\n----------------------------------------\n')

# using matehmatical operators with numpy arrays, can't be done the same way with python lists
a = [1,2]
b = np.array([1,2])
c = np.array([4,5])
# print( a + 2) # this gives TypeError: can only concatenate list (not "int") to list
print( b + 2) # this does the mathematical operation as per the operator, with each item in np array
b += 1 # increases every item value by 1
print(c + b) # mathematical operation on 2 diff np arrays work only if the dimensions are same
print('\n----------------------------------------\n')

# Using exclusive METRICS calculation (the way we did in Mathematics in school)

m1 = np.array( [ [1,2,3], [4,5,6] ] )
m2 = np.array( [ [1,2], [3,4], [5,6] ] )
print( np.matmul( m1,m2 ) ) # MATMUL multiplies the 2 arrays mathematically unlike element by element if we simply use '*'
# the above statement return error if dimentions of both the metrics are unsatisfactory

print(np.linalg.det( np.identity(6) )) # this prints determinant of the matrix
''' find more metrics calculative funcs in numpy.linalg'''
print('\n----------------------------------------\n')

# RESHAPE numpy arrays
before = np.array( [1,2,3,4,5,6] )
after  = before.reshape( (3,2) ) # select a dimension that may fit in all the items of the specified matrix
print( after )
print('\n----------------------------------------\n')

# STACKING in METRICS.. dimensions should match
v1 = np.array( [1,2,3,4] )
print(v1)
v2 = np.array( [5,6,7,8] )
print( np.vstack( [v1,v2] ) ) # VERTICAL STACKING
print( np.hstack( (v1,v2) ) ) # HORIZONTAL STACKING
print('\n----------------------------------------\n')
