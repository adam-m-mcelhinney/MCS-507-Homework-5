# L-9 MCS 507 Mon 17 Sep 2012 : makerule.py

# We show how to derivate an integration rule with sympy.
# Our rule approximates an integral over [a,b],
# evaluating a function at a, m = (a+b)/2, and b,
# so we look for 3 weights: wa, wm, and wb.
# With 3 unknown weights we can require that all quadrics
# are integrated correctly because:
# (1) the integration operator is a linear operator and 
# (2) it suffices to require that the 3 basic functions
#     1, x, and x**2 are integrated correctly.

from sympy import *
var('a,b,wa,wm,wb')
rule = lambda f: wa*f(a) + wm*f((a+b)/2) + wb*f(b)
var('f')
print 'making the rule', rule(f)
# the basic functions are 1, x, and x**2
b0 = lambda x: 1
b1 = lambda x: x
b2 = lambda x: x**2
# require that b0, b1, b2 are integrated exactly
var('x')
e0 = rule(b0) - integrate(b0(x),(x,a,b))
e1 = rule(b1) - integrate(b1(x),(x,a,b))
e2 = rule(b2) - integrate(b2(x),(x,a,b))
# for the user, we print the equations
print 'solving 3 equations :'
print e0,'== 0'
print e1,'== 0'
print e2,'== 0'
# the equations are easy to solve:
R = solve((e0,e1,e2),(wa,wm,wb))
print R
v = rule(f)
s = Subs(v,(wa,wm,wb),(R[wa],R[wm],R[wb])).doit()
formula = factor(s)
print 'Simpson formula :', formula
r = lambda f: (b-a)*(f(a) + 4*f((a+b)/2) + f(b))/6
# verifying if every quadric is integrated exactly
var('c0,c1,c2')
q = lambda x: c0 + c1*x + c2*x**2
vr = simplify(r(q))
print 'approximation :', vr
er = integrate(q(x),(x,a,b))
print '  exact value :', er
print '    the error :', vr - er
