# L-24 MCS 507 Mon 22 Oct 2012 : pendlsode.py

# The second order ODE theta''(t) + alpha*sin(theta(t)) = 0
# is solved as a system of two coupled first order ODEs:
# theta'(t) = v(t)
#     v'(t) = -alpha*sin(theta(t))
# with initial conditions theta(0) = theta0, v(0) = v0.
# The parameter alpha equals g/L, where
# g is the gravitational constant, and
# L is the length of the pendulum.

# We use odeint of ODEPACK to solve this problem.

import scipy as sp
import matplotlib.pyplot as plt
from scipy.integrate.odepack import odeint

def f(y,t):
   """
   Is the right hand side of the
   ODE dy/dt = f(y,t).
   """
   r = sp.array([0,0],float)
   r[0] = y[1]
   r[1] = -5.0*sp.sin(y[0])
   return r

def main():
   """
   Computes the motion of a pendulum,
   governed by the ODE: 
   theta''(t) + alpha*sin(theta(t)) = 0,
   """
   T = 10; n = 1000
   theta0 = sp.pi/6; v0 = 0
   tspan = sp.linspace(0,T,n+1)
   initc = sp.array([theta0,v0])
   y = odeint(f,initc,tspan)
   theta = y[:,0]
   v = y[:,1]
   fig = plt.figure()
   fig.add_subplot(211)
   plt.plot(tspan,theta)
   plt.title('angle as function of time')
   fig.add_subplot(212)
   plt.plot(tspan,v,label='velocity(t)')
   plt.title('velocity as function of time')
   plt.show()

main()
