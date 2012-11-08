# L-14 MCS 507 Fri 28 Sep 2012 : power_method.py

# The script is a very simple illustration using numpy
# of the power method to compute an approximation for
# the largest eigenvalue of a complex matrix.

import numpy as np

def power_method(A,x,m):
   """
   Does m iterations of the power
   method starting at x.  Returns
   an approximation of the largest
   eigenvector of the matrix A.
   """
   y = x
   for i in xrange(m):
      y = A*y
      y = y/np.linalg.norm(y)
   return y

def check(A,Y):
   """
   Compares the output Y of the power
   method with the largest eigenvalue.
   """
   Z = A*Y
   la = Z[0]/Y[0]
   print 'computed eigenvalue :' , la
   [L,V] = np.linalg.eig(A)
   K = list(abs(L))
   k = K.index(max(K))
   print ' largest eigenvalue :', L[k]
   
def main():
   """
   Prompts the user for a dimension
   and the number of iterations.
   """
   print 'Running the power method...'
   n = input('Give the dimension : ')
   m = input('How many iterations ? ')
   j = complex(0,1)
   a = np.random.normal(0,1,(n,n)) \
     + np.random.normal(0,1,(n,n))*j
   x = np.random.normal(0,1,(n,1)) \
     + np.random.normal(0,1,(n,1))*j
   A = np.matrix(a); X = np.matrix(x)
   Y = power_method(A,X,m)
   check(A,Y)

main()
