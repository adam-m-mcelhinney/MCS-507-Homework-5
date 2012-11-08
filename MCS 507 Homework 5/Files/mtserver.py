# L-28 MCS 507 Wed 31 Oct 2012 : mtserver.py

# Illustration of multithreaded server.

from socket import *
from threading import *

class Handler(Thread):
   """
   Defines handler threads.
   """
   def __init__(self,n,s,b):
      """
      Name of handler is n, server
      socket is s, buffer size is b.
      """
      Thread.__init__(self,name=n)
      self.sv = s
      self.bf = b

   def run(self):
      """
      Handler accepts connection,
      prints message received from client.
      """
      n = self.getName()
      server = self.sv
      buffer = self.bf
      client, client_address = server.accept()
      print n + ' accepted request from ',\
         client_address
      print n + ' waits for data'
      data = client.recv(buffer)
      print n + ' received ', data

def connect(n,b):
   """
   Connects a server to listen to n clients,
   buffer size is b.  Returns the socket.
   """
   hostname = ''   # to use any address
   number = 11267  # number for the port
   buffer = b      # size of the buffer
   server_address = (hostname, number)
   server = socket(AF_INET, SOCK_STREAM)
   server.bind(server_address)
   server.listen(n)
   return server

def main():
   """
   Prompts for number of connections,
   starts the server and handler threads.
   """
   n = input('give #clients : ')
   b = 80; server = connect(n,b)
   print 'server is ready for %d clients' % n
   T = []
   for i in range(0,n):
      T.append(Handler(str(i),server,b))
   print 'server starts %d threads' % n
   for t in T: t.start()
   server.close()

if __name__ == "__main__": main()
