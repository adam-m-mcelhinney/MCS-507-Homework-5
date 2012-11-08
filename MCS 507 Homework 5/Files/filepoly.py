# L-18 MCS 507 Mon 5 Oct 2011 : filepoly.py

# With this script we compute a tableau format of a random polynomial
# for writing to file. 

# We use sympy to make sure we have a valid expression,
# but sympy does not support complex numbers as coefficient domain
# for polynomials.

# With a dictionary we ensure every monomial is stored only once.

import randpoly as rp
import sympy as sp

def dictpoly(p):
   """
   Returns a dictionary representation of
   the polynomial p.  The imaginary unit I
   is the last power of every exponent. 
   """
   R = {}
   T = p.terms()
   for t in T:
      (e,c) = t
      a = e[0:-1]
      Ideg = e[len(e)-1]
      cf = (c if Ideg == 0 else complex(0,c))
      if not R.has_key(a):
         R[a] = cf
      else:
         R[a] += cf
   return R

def strexp(e):
   """
   Returns a string representation of
   the exponent in the tuple e.
   """
   s = ""
   for d in e:
      s += (' ' + str(d))
   return s

def dictprint(n,D):
   """
   Prints the tableau format of the
   dictionary representation in D,
   n is the number of variables.
   """
   print len(D), n
   for k in D.keys():
      c = D[k]
      print sp.re(c), sp.im(c), strexp(k)

def dictwrite(name,n,D):
   """
   Writes the dictionary D in tableau
   format to file with the given name.
   """
   file = open(name,'w')
   s = str(len(D)) + ' ' + str(n) + '\n'
   file.write(s)
   for k in D.keys():
      c = D[k]
      s = str(sp.re(c))
      s += ' ' + str(sp.im(c))
      s += ' ' + strexp(k) + '\n'
      file.write(s)
   file.close()

def cffexp(s):
   """
   Returns the tuple of coefficient
   and exponent stored in s.
   """
   L = s.split(' ')
   c = complex(eval(L[0]),eval(L[1]))
   e = []
   for k in xrange(2,len(L)):
      if L[k] != '':
         e.append(eval(L[k]))
   return (c, tuple(e))

def dictread(name):
   """
   Opens the file with name, reads it and
   returns the dictionary representation
   of the polynomial stored in the file.
   """
   file = open(name,'r')
   line = file.readline()
   L = line.split(' ')
   s = 'reading ' + L[0] + ' monomials'
   n = eval(L[1])
   s += ' in ' + str(n) + ' variables...'
   print s
   D = {}
   while True:
      s = file.readline()
      if s == '': break
      (c,e) = cffexp(s)
      D[e] = c
   file.close()
   return D

def main():
   """
   Tests manipulation of a random
   polynomial as a sympy polynomial.
   """
   (C,E) = rp.randpoly(3,7,5)
   S = ['x','y','z']
   p = rp.sympypoly(S,C,E)
   q = sp.Poly(p)
   print 'a random polynomial :', q
   D = dictpoly(q)
   print 'dictionary representation :', D
   print 'tableau representation :'
   dictprint(len(S),D)
   filename = raw_input('give a file name : ')
   dictwrite(filename,len(S),D)
   R = dictread(filename)
   print R

main()
