# L-24 MCS 507 Mon 22 Oct 2012 : pendulum.py

# The second order ODE theta''(t) + alpha*sin(theta(t)) = 0
# is solved as a system of two coupled first order ODEs:
# theta'(t) = v(t)
#     v'(t) = -alpha*sin(theta(t))
# with initial conditions theta(0) = theta0, v(0) = v0.
# The parameter alpha equals g/L, where
# g is the gravitational constant, and
# L is the length of the pendulum.

# Following appendix C.4 of the text book we use SciPy 
# to compute an approximate solution for this problem.
# The angle and its velocity are plotted with matplotlib.

import scipy as sp
import matplotlib.pyplot as plt

def pendulum(T,n,theta0,v0,alpha):
   """
   Return the motion (theta, v, t) of
   a pendulum, governed by the ODE: 
   theta''(t) + alpha*sin(theta(t)) = 0,
   where the parameters are
     T : time t ranges from 0 to T,
     n : the number of time steps,
     theta0 : angle at t = 0,
     v0 : velocity at t = 0,
     alpha : value for the parameter.
   """
   dt = T/float(n)
   t = sp.linspace(0,T,n+1)
   v = sp.zeros(n+1)
   theta = sp.zeros(n+1)
   v[0] = v0 
   theta[0] = theta0
   for k in range(n):
      theta[k+1] = theta[k] + dt*v[k]
      v[k+1] = v[k] - alpha*dt*sp.sin(theta[k+1])
   return theta, v, t

def test_values():
   """
   Returns values for the input data:
   T, n, theta0, v0, and alpha.
   """
   theta0 = sp.pi/6
   n = 1000
   T = 10
   v0 = 0
   alpha = 5
   return T, n, theta0, v0, alpha

def main():
   """
   Defines the test values and
   computes the trajectory of
   the pendulum.  
   """
   T,n,p0,v0,a = test_values()
   theta,v,t = pendulum(T,n,p0,v0,a)
   f = plt.figure()
   f.add_subplot(211)
   plt.plot(t,theta)
   plt.title('angle as function of time')
   f.add_subplot(212)
   plt.plot(t,v,label='velocity(t)')
   plt.title('velocity as function of time')
   plt.show()

main()
