# L-26 MCS 507 Fri 26 Oct 2012 : double_double_eval.py

# The purpose of this script is to see whether we can evaluate the
# motivating expression of the lecture of Wednesday 24 October correctly
# with double double arithmetic.  We use our class DoubleDouble.

from double_double import DoubleDouble

print 'checking the motivating interval arithmetic example'
f = lambda x,y: (DoubleDouble(333.75) - x**2)*y**6 \
  + x**2*(DoubleDouble(11)*x**2*y**2 \
  - DoubleDouble(121)*y**4 - DoubleDouble(2)) \
  + DoubleDouble(5.5)*y**8 + x/(DoubleDouble(2)*y);
a = 77617; b = 33096
z = f(DoubleDouble(a),DoubleDouble(b))
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
print 'error :', abs(e15 - z.high)
