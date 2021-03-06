import socket
import HTML
import psutil


HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

print 'Server HTTP on port %s ...' % PORT

while True:
	client_connection, client_address = listen_socket.accept()
	request = client_connection.recv(1024)
	
	http_status = "HTTP/1.1 200 OK \n"
	http_type = "Content-Type: text/html\n"
	temp = psutil.cpu_percent()
	temptable = HTML.Table(header_row=['Temp', 'Result'])
	#for temp(temp_readings):
	if temp > 70:
		color = 'Red'
		result = 'Fail'
	elif temp > 40:
		color = 'Yellow'
		result = 'Warning'
	else:
		color = 'Green'
		result = 'OK'
	colored_result = HTML.TableCell(result, bgcolor=color)
	temptable.rows.append([temp, colored_result])

	http_body = """
		<!doctype html>
		<html>
		<body>
		""" + str(temptable) + """
		</body>
		</html>"""

	client_connection.send(http_status)
	client_connection.send(http_type)
	client_connection.send(http_body)
	client_connection.close()
