# L-10 MCS 507 Wed 19 Sep 2012 : simpsonrule.py

# This script is a modification of "makerule.py" of lecture 9,
# illustrating an application of exec to the symoblic construction
# of the Simpson rule.

# Part I: code copied from makerule.py :
from sympy import *
var('a,b,wa,wm,wb')
rule = lambda f: wa*f(a) + wm*f((a+b)/2) + wb*f(b)
b0 = lambda x: 1; b1 = lambda x: x
b2 = lambda x: x**2
var('f,x')
e0 = rule(b0) - integrate(b0(x),(x,a,b))
e1 = rule(b1) - integrate(b1(x),(x,a,b))
e2 = rule(b2) - integrate(b2(x),(x,a,b))
R = solve((e0,e1,e2),(wa,wm,wb))
v = rule(f)
s = Subs(v,(wa,wm,wb),(R[wa],R[wm],R[wb])).doit()
formula = factor(s)
# Part II: applying exec
code = """
def Simpson(f,A,B):
   y = %s
   z = Subs(y,(a,b),(A,B)).doit()
   return z
""" % formula
exec(code)
# Part III: integrating any quadric
print 'integrating c0+c1*x+c2*x**2 over [L,U]'
var('c0,c1,c2,L,U')
q = lambda x: c0 + c1*x + c2*x**2
vr = simplify(Simpson(q,L,U))
print 'approximation :', vr
er = integrate(q(x),(x,L,U))
print '  exact value :', er
print '    the error :', vr - er
