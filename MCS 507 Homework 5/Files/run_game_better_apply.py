# L-31 MCS 507 Wed 7 Nov 2012 : run_game_better_apply.py

from time import clock
import numpy as np
from run_game_better import update

def main():
   """
   Generates a random matrix and
   applies the rules for Conway's game of life.
   """
   r = 0.2  # ratio of nonzeroes
   # n = 100  # dimension of the matrix
   n = input('give the dimension : ')
   A = np.random.rand(n,n)
   A = np.matrix(A < r,np.uint8)
   start_time = clock()
   for i in range(n): A = update(A)
   stop_time = clock()
   elapsed = stop_time - start_time
   print 'elapsed time', elapsed, 'seconds'

main()
