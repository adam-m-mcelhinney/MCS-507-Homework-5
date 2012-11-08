# L-29 MCS 507 Fri 2 Nov 2012 : speelpenning1.py

# Computes the gradient of Speelpenning's example
# using simply the diff method of sympy.

import sympy as sp

n = input('give number of variables : ')
V = ['x' + str(i) for i in range(n)]
X = sp.var(tuple(V))
p = reduce(lambda a,b: a*b,X)
print p
g = [sp.diff(p,X[i]) for i in xrange(n)]
for e in g: print e
