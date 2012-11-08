# L-24 MCS 507 Mon 22 Oct 2012 : tractrix.py

# A tractor is connected to a trailer by a rigid bar of unit length.
# The tractor moves in a circle.  The path of the trailer is the solution
# of a system of ordinary differential equations.

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate.odepack import odeint

def tractor(t):
   """
   Returns the position (x,y) 
   and velocity vector (u,v)
   for the tractor at time t.
   """
   x = sp.cos(t); y = sp.sin(t)
   u = -sp.sin(t); v = sp.cos(t)
   return x,y,u,v

def trailer(y,t):
   """
   Defines the right hand side of
   the system for the trailer.
   """
   r = np.array([0,0],float)
   x1, x2, x1v, x2v = tractor(t)
   r[0] = y[0] - x1
   r[1] = y[1] - x2
   r = r/np.linalg.norm(r)
   d = x1v*r[0] + x2v*r[1]
   r = d*r
   return r

def main():
   """
   Defines the setup for the system
   for the trailer and solves it.
   """
   T = 20; n = 100
   tspan = sp.linspace(0,T,n+1)
   initc = sp.array([2,0])
   path = odeint(trailer,initc,tspan)
   x = path[:,0]; y = path[:,1]
   x1, x2, x1v, x2v = tractor(tspan)
   fig = plt.figure()
   plt.plot(x1,x2,'r',x,y,'g')
   for i in xrange(0,n,6):
      plt.plot(sp.array([x1[i],x[i]]), \
               sp.array([x2[i],y[i]]),'b')
   plt.show()

main()
