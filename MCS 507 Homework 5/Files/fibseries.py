# L-19 MCS 507 Wed 10 Oct 2012 : fibseries.py

# The Fibonacci numbers arise as the coefficients of the
# Taylor expansion of g(z) = z/(1 - z - z^2) about z = 0.
# Use sympy or Sage to compute the first 10 terms
# of the series development of g(z) about z = 0.
# Extract the coefficients of the terms in the series.

import sympy as sp
z = sp.var('z')
g = z/(1-z-z**2)
print g
t = g.series(z,x0=0,n=None)
L = [t.next() for i in xrange(10)]
print L
F = [sp.Poly(e).terms()[0][1] for e in L]
print F
