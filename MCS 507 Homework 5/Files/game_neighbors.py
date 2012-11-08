# L-30 MCS 507 Mon 5 Nov 2012 : game_neighbors.py

# This script below prepares the vectorized version
# of the counting of the live neighbors in Conway's game of life.
# We compare the neighbor count matrix to the directly
# calculated number of neighbors.

import numpy as np

def neighbors(A,i,j):
   """
   Returns #cells alive next to A[i,j].
   """
   cnt = 0
   if i > 0:
      if A[i-1,j]: cnt = cnt + 1
      if j > 0:
         if A[i-1,j-1]: cnt = cnt + 1
      if j < A.shape[1]-1: 
         if A[i-1,j+1]: cnt = cnt + 1
   if i < A.shape[0]-1:
      if A[i+1,j]: cnt = cnt + 1
      if j > 0: 
         if A[i+1,j-1]: cnt = cnt + 1
      if j < A.shape[1]-1:
         if A[i+1,j+1]: cnt = cnt + 1
   if j > 0:
      if A[i,j-1]: cnt = cnt + 1
   if j < A.shape[1]-1:
      if A[i,j+1]: cnt = cnt + 1
   return cnt

def neighbor_count(A):
   """
   The (i,j)-th entry of the matrix A
   counts the number of live neighbors
   of the (i,j)-th cell.
   """
   B = np.zeros((A.shape[0],A.shape[1]),int)
   for i in range(0,A.shape[0]):
      for j in range(0,A.shape[1]):
         B[i,j] = neighbors(A,i,j)
   return B

def neighbor_count_matrix(A):
   """
   Returns a matrix counting the
   number of live neighbors.
   """
   AA = np.copy(A)
   R = np.copy(A)
   B = np.copy(R[:,:-1])
   C = np.copy(R[:,+1:])
   R[:,+1:] = np.copy(R[:,+1:]) + B 
   R[:,:-1] = np.copy(R[:,:-1]) + C 
   D = np.copy(R[:-1,:])
   E = np.copy(R[+1:,:])
   R[+1:,:] = np.copy(R[+1:,:]) + D
   R[:-1,:] = np.copy(R[:-1,:]) + E
   R = R - AA
   return R

def main():
   """
   Test on neighbor count.
   """
   n = 8 
   r = 0.2
   A = np.random.rand(n,n)
   A = np.matrix(A < r,int)
   B = neighbor_count_matrix(A)
   print 'cells alive'
   print A
   print 'vectorized neighbor count'
   print B
   C = neighbor_count(A)
   print 'original neighbor count'
   print C
   print 'equality check :'
   print np.equal(B,C)

if __name__ == "__main__": main()
