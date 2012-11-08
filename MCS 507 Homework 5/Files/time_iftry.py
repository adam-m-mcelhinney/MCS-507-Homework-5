# L-8 MCS 507 Fri 14 Sep 2012 : time_iftry.py

# With the time module we investigate the claim
# that try-except statements are more costly than
# if-else statements.

from random import randint, seed

def ifelse(n):
   """
   Does n divisions of p by q,
   checks first if q is zero.
   """
   cnt = 0
   for i in range(0,n):
      p = randint(-1,1)
      q = randint(0,1)
      if q != 0:
         r = p/q
      else:
         cnt = cnt + 1
   print '#divisions by zero :', cnt

def tryexcept(n):
   """
   Does n divisions of p by q,
   treats zero q as exception.
   """
   cnt = 0
   for i in range(0,n):
      p = randint(-1,1)
      q = randint(0,1)
      try:
         r = p/q
      except:
         cnt = cnt + 1
   print '#divisions by zero :', cnt

def main():
   """
   Compares the efficiency of if-else with
   the try-except to avoid division by zero.
   """
   import time
   n = 1000000
   seed(2)
   starttime = time.clock()
   ifelse(n)
   stoptime = time.clock()
   elapsed = stoptime - starttime
   print 'if-else: %.2f seconds' % elapsed
   seed(2)
   starttime = time.clock()
   tryexcept(n)
   stoptime = time.clock()
   elapsed = stoptime - starttime
   print 'try-except: %.2f seconds' % elapsed

if __name__=="__main__": main()
