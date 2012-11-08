# L-30 MCS 507 Mon 5 Nov 2012 : walk2D.py

# Code copied from book-examples/random/walk2D.py
# with several changes and adjustments made.

import numpy as np
import random
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
   for step in range(nst):
      for i in range(npa):
         d = random.randint(1,4)
         if d == 1: y[i] += 1   # north
         elif d == 2: y[i] -= 1 # south
         elif d == 3: x[i] += 1 # east
         elif d == 4: x[i] -= 1 # west
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
   random.seed(10)
   particles(3000,4000,20)

main()
