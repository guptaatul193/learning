import schedule
import time

x = 1

def job(x=x):
	print('Yahoooooo !!! '+str(x))
	x += 1

schedule.every(1).seconds.do(job)

while 1:
	schedule.run_pending()
	time.sleep(1)
