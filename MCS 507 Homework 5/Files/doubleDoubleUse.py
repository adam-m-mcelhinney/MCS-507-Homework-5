# L-25 MCS 507 Wed 24 Oct 2012 : doubleDoubleUse.py

# This script takes the double double representation of the sqrt(2)
# send the high and low part to the string method and parses this
# string back to the high and low part of a double double.

import doubleDoubleStringRep

hi = 1.4142135623730951
lo = -9.6672933134529147e-17
print 'hi = %22.17e' % hi
print 'lo = %22.17e' % lo
sqrt2 = "1.4142135623730950488016887242097e+00"
print 'sqrt(2) =', sqrt2

s = doubleDoubleStringRep.str(hi,lo)
print 'sqrt(2) =', s

x = doubleDoubleStringRep.parse(s)
print x

# Oddly enough, there is a segmentation fault if the script
# immediately ends after the parse() statement.

print (hi,lo)
