import socket

hostname = raw_input("Enter a hostname ")

hostIP = socket.gethostbyname(hostname)

print hostIP