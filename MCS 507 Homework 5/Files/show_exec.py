# L-10 MCS 507 Wed 19 Sep 2012 : show_exec.py

# With "exec" we can change the code of a program while the program
# is running.  We illustrate exec turning a formula into a function.

# The function we make is stored first in a string that spans
# multiple lines, enclosed by triple quotes.  With a %s inside
# that string we mark the position where we insert the formula
# given by the user.  The insertion is done by the % operator.

from math import *

formula = raw_input('Give a formula in x : ')
code = """
def f(x):
   return %s
""" % formula
exec(code)
x = input('give a value for x : ')
y = f(x)
print formula, "at x =", x , "is", y
