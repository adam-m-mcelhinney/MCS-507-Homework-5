# L-28 MCS 507 Wed 31 Oct 2012 : clockclient.py

# Code for client corresponding to clockserver.py.
# It prints the data received from the server.

from socket import *

hostname = 'localhost'  # on same host
number = 12091          # same port number
buffer = 25             # size of the buffer

server_address = (hostname, number)
client = socket(AF_INET, SOCK_STREAM)
client.connect(server_address)

print 'client is connected'
data = 'What is the time?'
client.send(data + (buffer-len(data))*' ')
data = client.recv(buffer)
print data

client.close()
