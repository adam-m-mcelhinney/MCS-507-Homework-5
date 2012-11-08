# -*- coding: utf-8 -*-
"""
HW 5, #7

Consider p(x) = x2 − 4x, q(x) = x(x − 4) and [a, b] = [1, 4].
Compare the straightforward interval evaluations of [a, b] in p
and q with the graph of the function. Which form, p or q, yields the
best result?

Ask Prof: I'm getting the same result for p and q

"""

import sympy as sp
from sympy.mpmath import iv
from numpy import linspace
from matplotlib import pylab as pl
#iv.dps = 15
#iv_p=lambda x; iv.mpf(
p=lambda x: x**2-4*x
q=lambda x: x*(x-4)

X=linspace(.5,4.5,2)
Y1=[p(1),p(4)]
Y2=[q(1),q(4)]


X2=linspace(.5,4.5,20)
YZ1=p(X2)
YZ2=q(X2)



pl.plot(X, Y1, "-r")
pl.plot(X, Y2, "-b")
pl.plot(X2, YZ1, "*r")
pl.plot(X2, YZ2, "*b")
pl.show()






