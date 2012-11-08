# L-7 MCS 507 Wed 12 Sep 2012 : define_series.py

from sympy import *

def safe_expand(t,o):
   """
   Given an iterator, returns the list
   of terms up to the order o.
   Uses an exception handler to catch
   cases when there is no next term.
   """
   L = []
   for i in xrange(o):
      try:
         L.append(t.next())
      except StopIteration:
         return L
   return L

def bivariate_series(e,v,o):
   """
   Returns a series of the expression e
   in the pair of variables in v 
   of respective orders in the pair o.
   """
   t1 = e.series(v[0],n=None)
   L1 = safe_expand(t1,o[0])
   t2 = [a.series(v[1],n=None) for a in L1]
   L2 = [safe_expand(t,o[1]) for t in t2]
   return sum([sum(L) for L in L2])

def main():
   """
   Prompts user for an expression,
   a pair of variables and orders.
   """
   e = raw_input('give an expression : ')
   v = raw_input('give pair of variables (e.g.: x,y) : ')
   o = input('give pair of orders (e.g.: 3,4) : ')
   w = var(v)
   print bivariate_series(eval(e),w,o)

if __name__=="__main__": main()
