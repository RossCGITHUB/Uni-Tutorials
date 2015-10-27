import socket
import sys
import datetime


# Ask for input
remoteServer = "localhost"
remoteServerIP = socket.gethostbyname(remoteServer)

#print a nice banner with info on which host we are about to scan
print "-" * 60
print "Please wait, scanning remote host", remoteServerIP
print "-" * 60

port = 0

#We also put in some error handling for catching errors 

try:
	for port in range (7000, 8005):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			print "Port {}: \t Open".format(port)
		sock.close


except socket.gaierror:
	print "Hostname could not be resolved. Exiting"
	sys.exit()

except socket.error:
	print "Couldn't connect to server"
	sys.exit()


