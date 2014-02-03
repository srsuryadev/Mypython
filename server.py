#server program
from decimal import *
import socket


def factorial(n):
	
	fact=1
	t=int(Decimal(n))
	t=t+1
	for i in range(1,t):
		fact*=i
	return fact

server=socket.socket()
host=socket.gethostname()
portnum=1729         #choose your port num to communicate
server.bind((host,portnum))
server.listen(2)
while True:
	con,address=server.accept()
	n=con.recv(256)
	output=factorial(n)
	con.send(str(output))
	con.close()

