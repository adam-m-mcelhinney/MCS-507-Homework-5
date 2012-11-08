# L-25 MCS 507 Wed 24 Oct 2012 : usempmathiv.py

# Illustration of interval arithmetic in the mpmath package of SymPy

import sympy as sp
from sympy.mpmath import iv
iv.dps = 15
x = iv.mpf(3)
print x, 'has type', type(x)
y = iv.mpf([3,4])
z = x/y
print x, '/', y, '=', z
# 0.1 /= '0.1'
a = iv.mpf(0.1)
b = iv.mpf('0.1')
print 'Observe strings!'
print a
print b
print 'some properties of', b
print 'middle :', b.mid
print 'width :', b.delta
print 'left bound :', b.a
print 'right bound :', b.b
print 'internal representation of', b
print b.__dict__
fraction = b.__dict__['_mpi_'][0][1]
exponent = b.__dict__['_mpi_'][0][2]
print 'fraction =', fraction
print 'exponent =', exponent
lb = fraction*2.0**exponent
print lb
