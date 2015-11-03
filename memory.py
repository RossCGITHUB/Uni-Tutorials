import psutil 
import time

x=0
for x in range(10):
	print psutil.virtual_memory().percent
	time.sleep(10)
