# L-28 MCS 507 Wed 31 Oct 2012 : mc4pi2.py

# Implements server for Monte Carlo method for pi,
# with two clients.  Server dispatches the seeds
# and collects results.

from socket import *

hostname = ''   # blank so any address can be used
number = 11267  # number for the port
buffer = 80     # size of the buffer

server_address = (hostname, number)
server = socket(AF_INET, SOCK_STREAM)
server.bind(server_address)
server.listen(2)

print 'server waits for connections...'

first, first_address = server.accept()
second, second_address = server.accept()

first.send('1'); second.send('2')

print 'server waits for results...'

r1 = first.recv(buffer)
r2 = second.recv(buffer)

result = 2*(float(r1)+float(r2))
print 'approximation for pi =', result

server.close()
