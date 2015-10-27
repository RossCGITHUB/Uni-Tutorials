import socket

port = 8000
remoteServer = "localhost"
remoteServerIP = socket.gethostbyname(remoteServer)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((remoteServerIP, port))
print "response = " +str(result)

if result == 0:
	print "Connection on port " + str(port) + " is a success"

elif result != 0: 
	print "Connection on port " + str(port) + " is not a success"


sock.close()