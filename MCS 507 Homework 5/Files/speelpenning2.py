# L-29 MCS 507 Fri 2 Nov 2012 : speelpenning2.py

# Computes the gradient of Speelpenning's example
# using ideas of algorithmic differentiation.

import sympy as sp

n = input('give number of variables : ')
V = ['x' + str(i) for i in range(n)]
X = sp.var(tuple(V))
F = [X[0]]
for i in xrange(1,n): F.append(F[i-1]*X[i])
print F
B = [X[n-1]]
for i in xrange(1,n-1): B.append(B[i-1]*X[n-i-1])
print B
G = [F[n-2]]
for i in xrange(0,n-2): G.append(F[i]*B[n-3-i])
G.append(B[n-2])
print G
