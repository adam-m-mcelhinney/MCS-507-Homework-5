"""
HW 5, #5

Instead of odeint() for the planar 3-body problem, write code for
the forward Euler method. For which value(s) of the step size do
you get the figure eight?


Ask Prof, show him forward euler and example from wikipedia

"""

# L-24 MCS 507 Mon 22 Oct 2012 : celestial.py

# The script plots the figure eight arising from the trajectories of three
# masses, in a simulation of the n-body problem from celestial mechanics.

# The parameters and initial values make a figure eight.
# Read "Strange Orbits" by Ivars Petersen, in # Science News 168(7), 2005.
# http://www.sciencenews.org/articles/20050813/mathtrek.asp

import scipy as sp
import matplotlib.pyplot as plt
from scipy.integrate.odepack import odeint

def f(z,t):
   """
   z is a vector with 12 entries
   ordered in blocks of 4:
   x[k](t),x'[k](t),y[k](t),y'[k](t)
   for k = 1,2,3.
   """
   L = [0 for k in xrange(12)]
   r = sp.array(L,float)
   # take three equal masses
   m = [1, 1, 1]
   # relabel input vector z
   x1 = z[0]; u1 = z[1]; y1 = z[2]; v1 = z[3]
   x2 = z[4]; u2 = z[5]; y2 = z[6]; v2 = z[7]
   x3 = z[8]; u3 = z[9]; y3 = z[10]; v3 = z[11]
   # u and v are first derivatives of x and y
   r[0] = u1; r[2] = v1
   r[4] = u2; r[6] = v2
   r[8] = u3; r[10] = v3
   # compute squared distances
   dx12 = x1 - x2; sdx12 = dx12**2
   dx13 = x1 - x3; sdx13 = dx13**2
   dx23 = x2 - x3; sdx23 = dx23**2
   dy12 = y1 - y2; sdy12 = dy12**2
   dy13 = y1 - y3; sdy13 = dy13**2
   dy23 = y2 - y3; sdy23 = dy23**2
   # denominators 
   d12 = (sdx12 + sdy12)**1.5 
   d13 = (sdx13 + sdy13)**1.5
   d23 = (sdx23 + sdy23)**1.5 
   # righthandside for second order
   r[1] = - m[1]*dx12/d12 - m[2]*dx13/d13;
   r[3] = - m[1]*dy12/d12 - m[2]*dy13/d13;
   r[5] = - m[0]*(-dx12)/d12 - m[2]*dx23/d23;
   r[7] = - m[0]*(-dy12)/d12 - m[2]*dy23/d23;
   r[9] = - m[0]*(-dx13)/d13 - m[1]*(-dx23)/d23;
   r[11] = - m[0]*(-dy13)/d13 - m[1]*(-dy23)/d23;
   return r

##def main():
##   """
##   Plots the trajectories of 3 equal masses
##   forming a figure 8.
##   """
##   # initial positions
##   ip1 = [0.97000436, -0.24308753]
##   ip2 = [-ip1[0], -ip1[1]]; ip3 = [0, 0]
##   # initial velocities
##   iv3 = [-0.93240737, -0.86473146] 
##   iv2 = [-iv3[0]/2, -iv3[1]/2]; iv1 = iv2
##   # input for initial righthandside vector
##   initz = [ip1[0], iv1[0], ip1[1], iv1[1], \
##            ip2[0], iv2[0], ip2[1], iv2[1], \
##            ip3[0], iv3[0], ip3[1], iv3[1]]
##   # solving the IVP
##   T = 2*sp.pi/3; n = 1000
##   tspan = sp.linspace(0,T,n+1)
##   z = odeint(f,initz,tspan)
##   # extracing the trajectories
##   x1 = z[:,0]; y1 = z[:,2]
##   x2 = z[:,4]; y2 = z[:,6]
##   x3 = z[:,8]; y3 = z[:,10];
##   # plotting the trajectories
##   fig = plt.figure()
##   plt.plot(x1,y1,'r',x2,y2,'g',x3,y3,'b')
##   plt.show()
##   return z
##
##t=main()


def forward_euler(y_n,t,f,h):
   """
   Does forward euler
   y_n+1=y_n+h*f(t_n,y_n)
   http://en.wikipedia.org/wiki/Euler_method
   """
   y_n1=y_n+h*f(y_n,t)
   #print y_n,h,f(t,y_n)
   return y_n1, t


f=lambda y, t: y
y_n=1;t=0;h=1
for i in range(4):
	y_n,t=forward_euler(y_n,t,f,h)
	print y_n,t
	t=t+1
      



   

"""
Plots the trajectories of 3 equal masses
forming a figure 8.
"""
# initial positions
ip1 = [0.97000436, -0.24308753]
ip2 = [-ip1[0], -ip1[1]]; ip3 = [0, 0]
# initial velocities
iv3 = [-0.93240737, -0.86473146] 
iv2 = [-iv3[0]/2, -iv3[1]/2]; iv1 = iv2
# input for initial righthandside vector
initz = [ip1[0], iv1[0], ip1[1], iv1[1], \
         ip2[0], iv2[0], ip2[1], iv2[1], \
         ip3[0], iv3[0], ip3[1], iv3[1]]
# solving the IVP
T = 2*sp.pi/3; n = 1000
tspan = sp.linspace(0,T,n+1)
#z = odeint(f,initz,tspan)
f=lambda y, t: y
z = forward_euler(f,initz,tspan)
# extracing the trajectories
x1 = z[:,0]; y1 = z[:,2]
x2 = z[:,4]; y2 = z[:,6]
x3 = z[:,8]; y3 = z[:,10];
# plotting the trajectories
fig = plt.figure()
plt.plot(x1,y1,'r',x2,y2,'g',x3,y3,'b')
plt.show()
