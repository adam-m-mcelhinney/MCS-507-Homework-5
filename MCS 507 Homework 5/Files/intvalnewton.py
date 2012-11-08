# L-25 MCS 507 Wed 24 Oct 2012 : intvalnewton.py

# First we show a naive use of interval arithmetic in Newton's method.
# with the mpmath package of SymPy.  Then we do it in proper manner.

import sympy as sp
from sympy.mpmath import iv
iv.dps = 15
print 'naive interval Newton :'
x = iv.mpf(['1.4','1.5'])
for i in xrange(5):
   x = x - (x**2 - 2)/(2*x)
   print x
print 'proper interval Newton :'
x = iv.mpf(['1.4','1.5'])
for i in xrange(5):
   x = x.mid
   x = x - (x**2 - 2)/(2*x)
   print x
