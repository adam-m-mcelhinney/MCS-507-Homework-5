# L-25 MCS 507 Wed 24 Oct 2012 : usempmathivfun.py

# Illustration of the evaluation of functions using interval arithmetic 
# with the mpmath package of SymPy

import sympy as sp
from sympy.mpmath import iv
iv.dps = 15
e = iv.exp(1)
print 'e :', e 
print 'log(e) :', iv.log(e)
print 'sin(e) :', iv.sin(e)
print 'cos(e) :', iv.cos(e)
p = iv.pi
print 'pi :', p
print 'sin(pi) :', iv.sin(p)
print 'cos(pi) :', iv.cos(p)
