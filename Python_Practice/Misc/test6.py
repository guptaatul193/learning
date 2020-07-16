"""
1. Get number of machines from user
2. Get Speed and Efficiency of all machines,
3. Now, Get max number of machines that can be used simultaneously.
4. Calculate performance by sum(speed)/min(efficiency).
5. Get highest performance among all the combinations of machines, or a standalone machine.

Example:
speed --> 40,50,60
effic. --> 2,4,1


"""

from itertools import combinations

def maxPerformance(speed, efficiency, maxmachines):
	combs = []
	out = {}
	for i in range(1,maxmachines+1):
		combs.extend( combinations( list(range(len(speed))), i ) )
	for i in combs:
		s = [ j for j in speed if speed.index(j) in i ]
		e = [ j for j in efficiency if efficiency.index(j) in i ]
		if len(s)==0 or len(e)==0:
			continue
		out[sum(s)*min(e)] = i

	return (max(out), out[max(out)])

if __name__ == '__main__':

	n = int( input('Please Enter Number of Machine: ') )
	s = []
	e = []
	for i in range(n):
		print('\nMachine %d - ' %(i+1))
		s.append( int(input('Enter Speed: ')) )
		e.append( int(input('Enter Efficiency: ')) )

	maxi = int( input('Please Enter Maximum Machine Limit: ') )

	machine = maxPerformance( s, e, maxi )

	print('Maximum Performance = ', machine[0])
	print('Machines giving max Performance = ' , ','.join([ str(i+1) for i in machine[1]]))
