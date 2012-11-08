# L-7 MCS 507 Wed 12 Sep 2012 : example_series.py

# The script illustrates the use of sympy to develop
# a Taylor series development in several variables.

from sympy import sin, cos, exp
from sympy.abc import x, y, z
e = x**2*cos(y) + 4*exp(z)*sin(x)
# developing e about x = 0, 4th order
print e.series(x,x0=0,n=4)
# using an iterator of the series
tx = e.series(x,x0=0,n=None)
Lx = [tx.next() for i in range(3)]
print 'Lx =', Lx
e3x = sum(Lx)
# observe there is no O() in e3x
print 'sum(Lx) =', e3x
# developing e3x about y = 1
ty = Lx[1].series(y,n=None)
Ly = [ty.next() for i in range(2)]
print 'Ly =', Ly
e2y = sum(Ly)
print 'e2y =', e2y
# developing z about z = 0, 3rd order
tz0 =  Lx[0].series(z,n=None)
tz2 =  Lx[2].series(z,n=None)
Lz0 = [tz0.next() for i in range(2)]
print 'Lz0 =', Lz0
Lz2 = [tz2.next() for i in range(2)]
print 'Lz2 = ', Lz2
s = sum(Lz0) + sum(Ly) + sum(Lz2)
print 's =', s
from sympy import Subs
v = (0.01,1.01,0.01)
ev = Subs(e,(x,y,z),v).doit()
sv = Subs(s,(x,y,z),v).doit()
print 'expression value =', ev
print '    series value =', sv
print '      difference =', abs(ev - sv)
