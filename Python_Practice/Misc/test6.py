"""
1. Get number of machines from user
2. Get Speed and Efficiency of all machines,
3. Now, Get max number of machines that can be used simultaneously.
4. Calculate performance by sum(speed)/min(efficiency).
5. Get highest performance among all the combinations of machines, or a standalone machine.

Example:
speed --> 40,50,60
effic. --> 2,4,1
max number of machines --> 3

Max Performance --> 200 from machine 2 alone
"""

from itertools import combinations

def maxPerformance(speed, efficiency, maxmachines):
	combs = []
	out = {}
	for i in range(1,maxmachines+1):
		combs.extend( combinations( list(range(len(speed))), i ) )
	for i in combs:
		s = [ j for ind,j in enumerate(speed) if ind in i ]
		e = [ j for ind,j in enumerate(efficiency) if ind in i ]
		# if len(s)==0 or len(e)==0:
			# continue
		out[sum(s)*min(e)] = i

	return (max(out), out[max(out)])

if __name__ == '__main__':

	n = int( input('Please Enter Number of Machine: ') )
	s = []
	e = []
	for i in range(n):
		print('\nMachine %d - \n------------' %(i+1))
		s.append( int(input('Enter Speed: ')) )
		e.append( int(input('Enter Efficiency: ')) )

	maxi = int( input('\nPlease Enter Maximum Machine Limit: ') )
	if maxi > n:
		print('\n*********  Max Limit Cannot Exceed Total Machine, considering all machines for performance calculation !! ******\n')

	machine = maxPerformance( s, e, maxi )

	print('Maximum Performance = ', machine[0])
	print('Machines giving max Performance = ' , ','.join([ str(i+1) for i in machine[1]]))
