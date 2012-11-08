# L-29 MCS 507 Fri 2 Nov 2012 : numdiff.py

# We compute the first derivative of increasing (odd) orders,
# using the derivative method of the package scipy.

from scipy.misc import derivative
from scipy import exp, sin

f = lambda x: exp(-x**2)*sin(x)

L = [derivative(f,x0=0.1,dx=1.0e-2,order=n) for n in xrange(3,12,2)]

last = L[len(L)-1]
E = [abs(L[k] - last) for k in xrange(len(L)-1)]
for k in xrange(len(E)):
   print '%.15f  error: %.3e' % (L[k],E[k])
print '%.15f' % last
