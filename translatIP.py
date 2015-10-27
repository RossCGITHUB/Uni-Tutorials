import socket

ipname = raw_input("Enter an IP address ")

hostname = socket.getfqdn(ipname)

print hostname