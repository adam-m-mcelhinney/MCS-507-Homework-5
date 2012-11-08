# L-1 MCS 507 Mon 27 Aug 2012 : hex4pi.py

# Discovery of the formula to compute hexadecimal digits of pi
# with the PSLQ algorithm using the PSLQ algorithm of sympy.

from sympy.mpmath import pslq
S = [sum([1.0/(16**k*(8*k+j)) \
   for k in xrange(8)]) \
   for j in xrange(1,8)]
print S
import math
S.append(math.pi)
P = pslq(S)
print P
