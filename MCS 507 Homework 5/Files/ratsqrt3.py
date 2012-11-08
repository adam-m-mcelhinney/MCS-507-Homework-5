# L-19 MCS 507 Wed 10 Oct 2012 : ratsqrt3.py

# Compute rational approximations for sqrt(3) using sympy
# and list comprehensions, working with approximations
# accurate from 3 to 10 decimal places.

import sympy as sp
L = [sp.sqrt(3).evalf(k) for k in xrange(3,10)]
print L
K = [int(L[k]*10**(k+2)) for k in xrange(len(L))]
print K
E = [sp.Rational(K[k])/10**(k+2) for k in xrange(len(K))]
print E
