# L-28 MCS 507 Wed 31 Oct 2012 : mtclient.py

# Code for the multiple clients connecting to
# multithreaded server in mtserver.py.

from socket import *

hostname = 'localhost'  # on same host
number = 11267          # same port number
buffer = 80             # size of the buffer

server_address = (hostname, number)
client = socket(AF_INET, SOCK_STREAM)
client.connect(server_address)

print 'client is connected'
data = raw_input('Give message : ')
client.send(data)

client.close()
