# L-30 MCS 507 Mon 5 Nov 2012 : game_of_life.py

# The script uses scitools.std to run the game of life
# applying the rules of John Conway.

import numpy as np
from scitools.std import plot
from scipy import sparse

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

def update(A):
   """
   Applies the rules of Conway's game of life.
   """
   B = np.zeros((A.shape[0],A.shape[1]),int)
   for i in range(0,A.shape[0]):
      for j in range(0,A.shape[1]):
         nb = neighbors(A,i,j)
         if A[i,j] == 1:
            if nb < 2 or nb > 3:
               B[i,j] = 0
            else:
               B[i,j] = 1
         else:
            if nb == 3: B[i,j] = 1
   return B

def main():
   """
   Generates a random matrix and
   applies the rules for Conway's
   game of life.
   """
   r = 0.2  # ratio of nonzeroes
   # n = 100  # dimension of the matrix
   n = input('give the dimension : ')
   A = np.random.rand(n,n)
   A = np.matrix(A < r,int)
   for i in xrange(10*n):
      S = sparse.coo_matrix(A)
      x = S.row; y = S.col
      plot(x,y,'r.',axis=[-1, n, -1, n], \
           title='stage %d' % i)
      A = update(A)

main()
