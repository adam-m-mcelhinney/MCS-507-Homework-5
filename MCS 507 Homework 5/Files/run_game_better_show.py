# L-31 MCS 507 Mon 5 Nov 2012 : run_game_better_show.py

# The script uses scitools.std to run the game of life
# applying the rules of John Conway.

import numpy as np
from scitools.std import plot
from scipy import sparse
from run_game_better import update

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
   A = np.matrix(A < r,np.uint8)
   for i in xrange(10*n):
      S = sparse.coo_matrix(A)
      x = S.row; y = S.col
      plot(x,y,'r.',axis=[-1, n, -1, n], \
           title='stage %d' % i)
      A = update(A)

main()
