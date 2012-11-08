# L-28 MCS 507 Wed 31 Oct 2012 : tcp_server.py

# Illustration of sockets in a server using TCP.

from socket import *

hostname = ''   # blank so any address can be used
number = 41267  # number for the port
buffer = 80     # size of the buffer

server_address = (hostname, number)
server = socket(AF_INET, SOCK_STREAM)
server.bind(server_address)
server.listen(1)

print 'server waits for connection'
client, client_address = server.accept()
print 'server accepted connection request from ',\
   client_address
print 'server waits for data'
data = client.recv(buffer)
print 'server received ', data

server.close()
