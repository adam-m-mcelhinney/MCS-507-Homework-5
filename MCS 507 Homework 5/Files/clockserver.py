# L-28 MCS 507 Wed 31 Oct 2012 : clockserver.py

# Illustration of using SocketServer module.
# The server will send the time to clients.

from SocketServer import StreamRequestHandler
from SocketServer import TCPServer
from time import ctime

port = 12091

class ServerClock(StreamRequestHandler):
   """
   The server tells the clients the time.
   """
   def handle(self):
      """
      Handler sends time to client.
      """
      print "connected at", self.client_address
      data = self.rfile.read(25)
      print 'read \"' + data + '\" from client'
      now = ctime()
      print 'writing \"' + now + '\" to client'
      self.wfile.write(now)

ss = TCPServer(('',port),ServerClock)
print 'server is listening to', port
# ss.handle_request() # ss.serve_forever()
try:
   print 'press ctrl c to stop server'
   ss.serve_forever()
except KeyboardInterrupt:
   print ' ctrl c pressed, closing server'
   ss.socket.close()
