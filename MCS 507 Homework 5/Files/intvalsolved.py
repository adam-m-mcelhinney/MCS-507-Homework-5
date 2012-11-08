# L-25 MCS 507 Wed 24 Oct 2012 : intvalsolved.py

# The example is taken from the paper of Stefano Taschini:
# "Interval Arithmetic: Python Implementation and Applications"
# Proceedings of the 7th Python in Science Conference (SciPy 2008).

# We show how to obtain a correct numerical approximation for this example
# using the interval arithmetic in the mpmath of SymPy.
# The width of the interval gives us an upper bound for the error.

import sympy as sp
x,y = sp.var('x,y')
g = (sp.Rational(33375)/100 - x**2)*y**6 \
+ x**2*(11*x**2*y**2 - 121*y**4 - 2) \
+ sp.Rational(55)/10*y**8 \
+ sp.Rational(1)*x/(2*y);
a = 77617; b = 33096
print 'evaluating', g, 'at', (a,b)
e = sp.Subs(g,(x,y),(a,b)).doit()
e15 = e.evalf(15)
print 'exact value :', e, '~', e15
# now we use interval arithmetic
from sympy.mpmath import iv
print 'using 35 decimal places ...'
iv.dps = 35
iv_f = lambda x,y: (iv.mpf('333.75') \
- x**2)*y**6 \
+ x**2*(iv.mpf('11')*x**2*y**2 \
- iv.mpf('121')*y**4 - iv.mpf('2')) \
+ iv.mpf('5.5')*y**8 + x/(iv.mpf('2')*y);
iv_a = iv.mpf(str(a))
iv_b = iv.mpf(str(b))
iv_z = iv_f(iv_a,iv_b)
print iv_z
print 'using 36 decimal places ...'
iv.dps = 36
iv_f = lambda x,y: (iv.mpf('333.75') \
- x**2)*y**6 \
+ x**2*(iv.mpf('11')*x**2*y**2 \
- iv.mpf('121')*y**4 - iv.mpf('2')) \
+ iv.mpf('5.5')*y**8 + x/(iv.mpf('2')*y);
iv_a = iv.mpf(str(a))
iv_b = iv.mpf(str(b))
iv_z = iv_f(iv_a,iv_b)
print iv_z
