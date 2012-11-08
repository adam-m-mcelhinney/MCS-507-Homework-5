# L-26 MCS 507 Fri 21 Oct 2011 : symdiff.py

# Plain application of the diff method of sympy to check
# the value of the scipy.derivative computed by numdiff.py.

import sympy as sp
x = sp.var('x')
f = sp.exp(-x**2)*sp.sin(x)
df = sp.diff(f,x)
print df
v = 0.1
y = sp.Subs(df,(x),(v)).doit()
print y
