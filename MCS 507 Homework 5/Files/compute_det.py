#!/usr/bin/python
import cgi

from numpy import matrix, zeros
from numpy.linalg import det

def Determinant(form,n):
   """
   returns the determinant of the matrix
   available in the form
   """
   A = zeros((n,n),float)
   for i in range(0,n):
      for j in range(0,n):
         info = "%d,%d" % (i,j)
         if form.has_key(info):
            A[i,j] = float(form[info].value)
   print "The matrix is"
   print A
   return det(A)

def main():
   """
   web interface to compute a determinant
   """
   print "Content-type: text/plain\n"
   form = cgi.FieldStorage()
   if form.has_key("dim"):
      n = int(form["dim"].value)
      d = Determinant(form,n)
      print "The determinant :", d

main()
