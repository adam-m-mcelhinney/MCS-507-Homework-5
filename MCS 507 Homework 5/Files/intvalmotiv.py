# L-25 MCS 507 Wed 24 Oct 2012 : intvalmotiv.py

# The example is taken from the paper of Stefano Taschini:
# "Interval Arithmetic: Python Implementation and Applications"
# Proceedings of the 7th Python in Science Conference (SciPy 2008).

# While we get the final correct approximation when we use 36
# decimal places using mpmath of SymPy, the choice of 36 is not obvious.

f = lambda x,y: (333.75 - x**2)*y**6 \
+ x**2*(11*x**2*y**2 - 121*y**4 - 2) \
+ 5.5*y**8 + x/(2*y);
a = 77617; b = 33096
z = f(float(a),float(b))
# to check the answer with SymPy :
import sympy as sp
x,y = sp.var('x,y')
g = (sp.Rational(33375)/100 - x**2)*y**6 \
+ x**2*(11*x**2*y**2 - 121*y**4 - 2) \
+ sp.Rational(55)/10*y**8 \
+ sp.Rational(1)*x/(2*y);
print 'evaluating', g, 'at', (a,b)
e = sp.Subs(g,(x,y),(a,b)).doit()
e15 = e.evalf(15)
print 'numerical value :', z
print 'exact value :', e, '~', e15
print 'error :', abs(e15 - z)
# let us double the precision to 30
sp.mpmath.mp.dps = 30
mp_f = lambda x,y: (sp.mpmath.mpf('333.75') \
- x**2)*y**6 \
+ x**2*(11*x**2*y**2 - 121*y**4 - 2) \
+ sp.mpmath.mpf('5.5')*y**8 + x/(2*y);
mp_a30 = sp.mpmath.mpf(str(a))
mp_b30 = sp.mpmath.mpf(str(b))
z30 = mp_f(mp_a30,mp_b30)
print 'using 30 digits :', z30
# adjusting the precision to 35
sp.mpmath.mp.dps = 35
mp_a35 = sp.mpmath.mpf(str(a))
mp_b35 = sp.mpmath.mpf(str(b))
z35 = mp_f(mp_a35,mp_b35)
print 'using 35 digits :', z35
# adjusting the precision to 36
sp.mpmath.mp.dps = 36
mp_a36 = sp.mpmath.mpf(str(a))
mp_b36 = sp.mpmath.mpf(str(b))
z36 = mp_f(mp_a36,mp_b36)
print 'using 36 digits :', z36
