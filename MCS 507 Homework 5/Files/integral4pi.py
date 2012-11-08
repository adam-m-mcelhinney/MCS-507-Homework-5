# L-31 MCS 507 Wed 7 Nov 2012 : integral4pi.py

# This script applies the composite trapezoidal rule 
# to the integral of sqrt(1-x^2) for x from 0 to 1,
# to obtain an approximation for pi.
# This inefficient computational expensive method give us
# an example to optimize with cython.

from time import clock
from math import sqrt

def circle(x):
   return sqrt(1-x**2)

def integral4pi(n):
   h = 1.0/n
   r = (circle(0)+circle(1))/2
   for i in range(n):
      r += circle(i*h)
   return 4*r*h

start_time = clock()
a = integral4pi(10**7)
stop_time = clock()
print 'pi =', a
elapsed = stop_time - start_time
print 'elapsed time = %.3f seconds' % elapsed
