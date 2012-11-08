# L-9 MCS 507 Mon 17 Sep 2012 : inlineif.py

# Illustration of the inline if construction.
# In case the statements in if-else tests are short,
# there is the one-line syntax for the if-else statement.
# The illustration below avoids the exception 
# "ValueError: math domain error" which is triggered
# when a function as asin or acos gets a value outside [-1,+1].
# The one-line if-else statement is useful in lambda statement.
# From numpy we import the NaN (the "Not a Number" float).

from math import asin, acos

x = input("give a number : ")
safe_asin = (asin(x) if -1 <= x <= +1 else "undefined")
print ('asin(%f) is' % x), safe_asin

from numpy import NaN

acos_fun = lambda x: (acos(x) if -1 <= x <= +1 else NaN)
y = input("give a number : ")
print ('acos(%f) is' % y), acos_fun(y)
