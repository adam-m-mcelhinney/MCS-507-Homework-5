#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import Cookie
import os

def GetCookie():
   """
   Retrieves cookie, either initializes counter,
   or increments the counter by one.
   """
   if os.environ.has_key('HTTP_COOKIE'):
      c = Cookie.Cookie(os.environ['HTTP_COOKIE'])
   else:
      c = Cookie.SmartCookie()
   if not c.has_key('counter'):
      c['counter'] = 0
   else:
      c['counter'] = c['counter'].value + 1
   return c

def main():
   """
   Retrieves a cookie and writes
   the value of counter to the page.
   """
   c = GetCookie()
   print c
   print "Content-Type: text/plain\n"
   print "counter: %d" % c['counter'].value

main()
