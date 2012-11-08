# L-4 MCS 507 Wed 5 Sep 2012 : testevalfun.py

from scitools.StringFunction \
import StringFunction

formula = raw_input('give a function in x : ')
f = StringFunction(formula)
v = input('  give a value for x : ')
y = f(v)
print 'formula', formula, 'at', v, 'is', y
