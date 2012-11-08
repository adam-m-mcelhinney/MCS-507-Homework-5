# L-28 MCS 507 Fri 31 Oct 2012 : mc4pi_client.py

# This client applies Monte Carlo simulation to
# estimate Pi.  The first seed comes from the
# server in the program mc2pi2.py.

import random
from socket import *

hostname = 'localhost'  # on same host
number = 11267          # same port number
buffer = 80             # size of the buffer

server_address = (hostname, number)
client = socket(AF_INET, SOCK_STREAM)
client.connect(server_address)

print 'client is connected'
s = client.recv(buffer)
print 'client received %s' % s

random.seed(int(s))

N = 10**7
k = 0
for i in range(0,N):
   x = random.uniform(0,1)
   y = random.uniform(0,1)
   if x**2 + y**2 <= 1: k = k + 1
R = float(k)/N
print 'client computes %.12f' % R

client.send(str(R))

client.close()
