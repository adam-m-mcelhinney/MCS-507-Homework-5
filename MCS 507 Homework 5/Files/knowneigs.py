# L-14 MCS 507 Fri 28 Sep 2012 : knowneigs.py

# This script to generate a matrix with given eigenvalues
# via the QR decomposition on a random matrix.

import numpy as np

def generate_matrix(L, verbose=False):
   """
   Generates a matrix with eigenvalues in L.
   In verbose mode, the steps are documented
   and the eigenvalues and eigenvectors of
   the generated matrix are computed.
   """
   n = len(L)
   A = np.random.rand(n,n)
   Q,R = np.linalg.qr(A)
   D = np.diag(L)
   B = np.dot(np.dot(Q.T,D),Q)
   if verbose:
      print 'a random matrix A :'
      print A
      print 'QR decomposition, Q*R = A :'
      print np.dot(Q,R)
      print 'R is upper triangular :'
      print R
      print 'Q is orthonormal, Q.T*Q = I :'
      print np.dot(Q.T,Q)
      print 'known eigenvalues on diagonal :'
      print D
      print 'the generated matrix :'
      print B
      L, V = np.linalg.eig(B)
      print 'eigenvalues :', L
      print 'eigenvectors :' 
      print V
   return B

def main():
   """
   Shows the generation of a matrix.
   """
   A = generate_matrix([4,3,2,1],True)

if __name__=="__main__": main()
