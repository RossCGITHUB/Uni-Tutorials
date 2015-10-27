import socket

ipname = raw_input("Enter an IP address ")

hostnam = socket.getfqdn(ipname)

print hostnam