# L-21 MCS 507 Mon 15 Oct 2012 : sympydochtmlopen.py

# Illustration of opening the index.html of the SymPy documentation.
# We downloaded the SymPy documentation onto disk:

# Welcome to SymPy's documentation! -- SymPy v0.7.1 documentation
# file:///Users/jan/Courses/MCS507/sympy-0.7.1-docs-html/index.html

from urllib import urlopen

u = 'file:///Users/jan/Courses/MCS507/' \
  + 'sympy-0.7.1-docs-html/index.html'
file = urlopen(u)
data = file.read(80)
print '80 characters :', data
L = data.split('\n')
print 'the lines :', L
file.close()
