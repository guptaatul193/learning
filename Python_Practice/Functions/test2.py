""" Lambda, Map, Filter and Reduce functions

	1. Lambda / Anonymous Functions:
	  	If a function can work on a single statement, we can create a Lambda
		function in stead of creating a complete conventional function.

	2. Map Functions
		If we've a list of values, and we want a common action to be perfomred
		on ALL the values (using a conventional function or a lambda function),
		and obtain equal number of calculated / output values, MAP function comes handy.

	3. Filter Functions:
		If for a given list of values, we've to get values filtered on the basis
		of a lamda / conventional function, filter functions can be used.

	4. Reduce Function:
		This has been discontinued to be a part of Python built-in functions from Python 3.x onwards,
		and is now currently a part of 'functools' module.
		Below is how this works -

		Data: [ a1, a2, ... an ]
		Function: f( x, y )

		reduce( f, data ) :
			step 1: val1 = f (a1, a2)
			step 2: val2 = f (val1, a3)
			step 3: val3 = f (val2, a4)
			.
			.
			step n-1: val(n-1) = f (val(n-2), an)
		"""

# LAMBDA FUNCTION
# Below 2 are lambda functions with single and multiple inputs respectively
square = lambda num: num**2
average = lambda x,y,z: (x+y+z)/3

def fibonacci( num ):
	out = 1
	for i in range(1,num+1):
		out *= i
	return out


print( square(2) ) # one way to call a lambda function
print( (lambda x,y,z: (x+y+z)/3) (5,6,7)) # another way to call lambda function

# MAP FUNCTION
# 'nos' is the list of inputs, we map them to the function 'lambda', which gives us 'map' object which is iterable in nature. We can however convert that into a list explicitly
nos = [1,3,4,11]
fib_nos = list( map( fibonacci, nos ) ) # PLEASE NOTE THAT although we're passing an iterable (list 'nos' in this case), to map with function 'fibonacci', the function will ACTUALLY receive 1 value at a time
print(fib_nos)

# FILTER FUNCTION
# nos is the list of input values, and using a filter values, we'll get a list of values among, which is divisible by 2 or 3.
nos = [4,6,3,9,111,153,33,89,91,55,71]
filter_div = list ( filter( lambda x: x%2==0 or x%3==0 , nos ) ) # the result of function must return eith TRUE or FALSE
print( filter_div )

# FILTER FUNCTION
# this is an INTERESTING and IMPORTANT example
vals = [ 'India', 'Germany', '', 'USA', {}, [], 0j, 1, 1.45, (), -10, 0.0, None, True, False, 0 ]
result = list( filter(None, vals ) ) # if we replace None with any other value like False, [], etc.. the code will fail, execute and see for yourself
print( result )
# note that all the empty entities, 0s, False have been filtered out.

# REDUCE FUNCTION
# map and filter take 2nd parameter as iterable, but compute one at a time. Reduce performs action on all, but 2 at a time
# in the below example, we'll multiply all the nos. in a list
from functools import reduce
nos = [4,6,3,9,111,153,33,89,91,55,71]
out = reduce( lambda x,y: x*y, nos  ) # PLEASE MIND THAT reduce doesn't return any iterable object, in stead it returns the finally processed value itself.
print(out)

# another example to find highest of all values, but without using max(). We'll use the same list
print( reduce( lambda x,y:x if x>y else y, nos ) )
