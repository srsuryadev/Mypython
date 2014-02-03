#client program

import socket

client=socket.socket()
host=socket.gethostname()
portnum=1729
client.connect((host,portnum))
print("ENTER THE NUMBER TO FIND THE FACTORIAL:")
n=input()
client.send(str(n))

result=client.recv(256)
print("THE FACTORIAL IS :"+result)
client.close()
