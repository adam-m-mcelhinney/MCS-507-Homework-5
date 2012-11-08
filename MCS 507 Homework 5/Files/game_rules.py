# This script tests the vectorized version of the transition rules
# of Conway's game of life.

import numpy as np
from game_neighbors import neighbor_count_matrix

def update(A,B):
   """
   Applies the rules of Conway's game of life,
   given the matrix of live cells in A and
   the neighboring count in B.
   """
   C = np.zeros((A.shape[0],A.shape[1]),int)
   for i in range(0,A.shape[0]):
      for j in range(0,A.shape[1]):
         nb = B[i,j]
         if A[i,j] == 1:
            if nb < 2 or nb > 3:
               C[i,j] = 0
            else:
               C[i,j] = 1
         else:
            if nb == 3: C[i,j] = 1
   return C 

def update_matrix(A,B):
   """
   The vectorized version of update.
   """
   starve = np.where(B > 3,0,A)
   lonely = np.where(B < 2,0,starve)
   alive = np.where(B == 3,1,lonely)
   return alive

def main():
   """
   Test on rules.
   """
   n = 20
   r = 0.3
   A = np.random.rand(n,n)
   A = np.matrix(A < r,int)
   B = neighbor_count_matrix(A)
   C = update(A,B)
   print 'live cells :'
   print A
   print 'apply original rules :'
   print C
   D = update_matrix(A,B)
   print 'apply matrix rules :'
   print D
   print 'equality check :'
   print np.equal(C,D)

if __name__ == "__main__": main()
