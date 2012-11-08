# L-31 MCS 507 Wed 7 Nov 2012 : run_game_of_life.py

# This script provides a basic implementation of the game of life
# of John Conway, without the visualization (see lecture 30),
# in order to time the cost of searching through numpy arrays.
# We do as many updates as the dimension of the matrix.

from time import clock
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
   start_time = clock()
   for i in range(n): A = update(A)
   stop_time = clock()
   elapsed = stop_time - start_time
   print 'elapsed time', elapsed, 'seconds'

main()
