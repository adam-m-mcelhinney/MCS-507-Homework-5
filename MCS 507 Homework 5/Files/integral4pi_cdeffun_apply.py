# L-31 MCS 507 Wed 7 Nov 2012 : integral4pi_cdeffun_apply.py

# This script applies the composite trapezoidal rule 
# to the integral of sqrt(1-x^2) for x from 0 to 1,
# to obtain an approximation for pi.

from time import clock
from integral4pi_cdeffun import integral4pi

start_time = clock()
a = integral4pi(10**7)
stop_time = clock()
print 'pi =', a
elapsed = stop_time - start_time
print 'elapsed time = %.3f seconds' % elapsed
