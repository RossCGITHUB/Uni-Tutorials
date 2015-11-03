import psutil
x=0
for x in range(3):	
	print psutil.cpu_percent(interval=1, percpu=True)
	print 'cpus: ' + str(psutil.cpu_count())        #tells you the cpu amount and the load