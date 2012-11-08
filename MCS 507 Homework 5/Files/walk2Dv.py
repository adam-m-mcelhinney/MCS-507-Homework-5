# L-30 MCS 507 Mon 5 Nov 2012 : walk2Dv.py

# This is the vectorized version of walk2D.py,
# modified from book-examples/random/walk2Dv.py.

import numpy as np
from scitools.std import plot

def particles(npa,nst,pls):
   """
   Shows random particle movement with
     npa : number of particles,
     nst : number of time steps,
     pls : how many steps for next plot.
   """
   x = np.zeros(npa); y = np.zeros(npa)
   xymax = 3*np.sqrt(nst);
   xymin = -xymax
   moves = np.random.random_integers(1,4,nst*npa)
   moves.shape = (nst,npa)
   for step in range(nst):
      this_move = moves[step,:]
      y += np.where(this_move == 1,1,0)
      y -= np.where(this_move == 2,1,0)
      x += np.where(this_move == 3,1,0)
      x -= np.where(this_move == 4,1,0)
      if (step+1) % pls == 0:
         plot(x,y,'bo', \
              axis=[xymin, xymax, xymin, xymax], \
              title='%d particles after %d steps' \
                    % (npa, step+1))

def main():
   """
   Fixes the seed for the random numbers
   and starts the particle simulation.
   """
   np.random.seed(10)
   particles(3000,4000,20)

main()
