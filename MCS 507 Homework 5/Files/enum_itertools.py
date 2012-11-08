# L-8 MCS 507 Fri 14 Sep 2012 : enum_itertools

# Given are three lists of letters.  We want to enumerate all 3-letter "words"
# where the k-th letter in the word is drawn from the k-th list.

A = ['b','c','d']; B = ['a','e','u']; C = ['d','p']

from itertools import product
p = product(A,B,C)
L = [p.next() for i in xrange(len(A)*len(B)*len(C))]
print L
