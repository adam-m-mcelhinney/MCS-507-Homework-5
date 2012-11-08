# L-18 MCS 507 Mon 3 Oct 2011 : randpoly.py

# Script to generate a random polynomial in several variables
# with coefficients uniformly generated on the complex unit circle.
# The polynomials are turned into sympy expressions.

def random_coefficient():
   """
   Returns a random complex coefficient,
   uniformly distributed on the unit circle.
   """
   from math import cos, sin, pi
   from random import uniform
   u = uniform(0,2*pi)
   return complex(cos(u),sin(u))

def random_exponent(n,d):
   """
   Returns an n-tuple obtained after
   d coin flips.
   """
   from random import randint
   L = [0 for i in xrange(n)]
   for i in xrange(d):
      L[randint(0,n-1)] += randint(0,1)
   return tuple(L)

def randpoly(n,d,m):
   """
   A random polynomial in n variables
   of degree at most d and m terms is
   returns as a tuple of two lists:
   coefficients and exponents.
   """
   C = [random_coefficient() for i in xrange(m)]
   E = [random_exponent(n,d) for i in xrange(m)]
   return (C,E)

def strmon(S,c,e):
   """
   Returns a string representation of a
   monomial using the list of symbols in S,
   the coefficient c, and the exponents e.
   """
   r = (' + ' + str(c))
   for i in xrange(len(e)):
      if e[i] > 0: r += ('*' + S[i]) 
      if e[i] > 1: r += ('**' + str(e[i]))
   return r

def strpoly(S,C,E):
   """
   Returns a string representation of 
   a polynomial in the variables in S with 
   coefficients in C and exponents in E.
   """
   p = ""
   for i in xrange(len(C)):
      p += strmon(S,C[i],E[i])
   return p

import sympy as sp

def sympypoly(S,C,E):
   """
   Turns the polynomial with coefficients
   in C, exponents in E and symbols in S
   into a sympy expression.
   """
   strp = strpoly(S,C,E)
   sp.var(S)
   return eval(strp)

def main():
   """
   Prompts the user for number of variables,
   largest degree, number of monomials, and
   then generates a random polynomial.
   """
   n = input('give number of variables : ')
   d = input('give the largest degree : ')
   m = input('give number of monomials : ')
   (C,E) = randpoly(n,d,m)
   print 'coefficients & exponents :', (C,E)
   S = ['x' + str(i) for i in xrange(1,n+1)]
   strp = strpoly(S,C,E)
   print 'string representation :', strp
   p = sympypoly(S,C,E)
   print 'sympy expression :', p

if __name__=="__main__": main()
