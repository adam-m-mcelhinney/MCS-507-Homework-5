# L-31 MCS 507 Wed 7 Nov 2012 : run_game_of_life.pyx

# This files defines Cython code for the module run_game_of_life to export
# methods to update the matrix as in the game of life of John Conway.
# With type declarations we hope to achieve fast access.

import numpy as np
cimport numpy as np
ctypedef np.uint8_t dtype_t

def neighbors(np.ndarray[dtype_t, ndim=2] A,
              Py_ssize_t i, Py_ssize_t j):
   """
   Returns #cells alive next to A[i,j].
   """
   cdef dtype_t cnt = 0
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

def update(np.ndarray[dtype_t, ndim=2] A):
   """
   Applies the rules of Conway's game of life.
   """
   cdef Py_ssize_t i,j
   cdef np.ndarray[dtype_t, ndim=2] B
   cdef dtype_t nb

   B = np.zeros((A.shape[0],A.shape[1]),np.uint8)
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
