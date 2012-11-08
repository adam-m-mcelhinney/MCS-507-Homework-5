# L-5 MCS 507 Fri 7 Sep 2012 : testgauss.py

# For the normal distribution provided by the function gauss in the
# module random, we generate a number of samples for a given mean
# and standard deviation.  The script computes the mean and standard 
# deviation of the computed samples.  For large enough number of samples, 
# the computed mean and # standard deviation should coincide with the 
# mean and standard deviation given by the user.  The script also counts
# the number of samples within the standard deviation of the mean.

from random import gauss
from math import sqrt

print 'testing the normal distribution'
mu = input('give the mean : ')
sigma = input('give the standard deviation : ')
n = input('give the number of samples : ')
L = [gauss(mu,sigma) for i in xrange(n)]
a = sum(L)/n
S = [(e - a)**2 for e in L]
s = sqrt(sum(S)/n)
A = mu - sigma; B = mu + sigma
F = filter(lambda x: A < x < B,L)
print 'average of samples : ', a
print 'standard deviation : ', s
print '#samples in [%.2f,%.2f] : %d' % (A,B,len(F))
print '        smallest sample : ', min(L)
print '         largest sample : ', max(L)
