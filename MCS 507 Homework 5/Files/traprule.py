# L-9 MCS 507 Mon 17 Sep 2012 : trapezoidal rule

# The trapezoidal rule approximates the
# integral of a function f(x) over [a,b]
# via (f(a) + f(b))*(b-a)/2

def traprule(f,a,b):
   "trapezoidal rule for f(x) over [a,b]"
   return (b-a)*(f(a) + f(b))/2

import math
s = 'integrating exp() over '
print s + '[a,b]'
a = input('give a : ')
b = input('give b : ')
y = traprule(math.exp,a,b)
print s + '[%.1E,%.1E] : ' % (a,b)
print 'the approximation : %.15E' % y
e = math.exp(b) - math.exp(a)
print '  the exact value : %.15E' % e
