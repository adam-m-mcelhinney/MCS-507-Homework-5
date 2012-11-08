# L-14 MCS 507 Fri 28 Sep 2012 : power_convergence.py

# We study the convergence of the power method,
# using the Power_Method class and knowneigs.generate_matrix().
# We generate a matrix with one eigenvalue of modulus one
# and all other eigenvalues have modulus 1/m, for some m.
# The higher m, the faster the power method converges.

import numpy as np
from knowneigs import generate_matrix
from power_iterator import Power_Method

def main():
   """
   Prompts the user for a dimension
   and the number of iterations.
   """
   print 'Running the power method...'
   n = input('Give the dimension : ')
   m = input('Convergence factor ? ')
   L = np.random.uniform(0,2*np.pi,n)
   j = complex(0,1)
   K = np.exp(j*L)
   for i in range(1,len(K)): K[i] = K[i]/m
   A = generate_matrix(K)
   p = Power_Method(n,A=A);
   for i in range(1000):
      p.next()
      print p
      if p.accurate(): break

if __name__=="__main__": main()
