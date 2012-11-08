# L-17 MCS 507 Fri 5 Oct 2012 : heatmovie

# The script makes an animation of a model of a heat wave.

from scitools.std import *

def animate(tmax,dt,x,function,ymin,ymax,t0=0,
            xlabel='x',ylabel='y',file='/tmp/m'):
   """
   Makes plots for t from t0 to tmax with steps dt,
   evaluating the function.
   """
   t = t0; counter = 0
   while (t <= tmax):
      y = function(x,t)
      plot(x,y,
           axis=[x[0],x[-1],ymin,ymax],
           title = 'time=%2d h'%(t/3600.0),
           xlabel=xlabel,ylabel=ylabel,
           savefig=file + '%04d.png' % counter)
      t = t + dt; counter = counter + 1
     
# global variables of the model

k = 1.E-6      # thermal diffusivity
P = 24*3600    # oscillation period in seconds
omega = 2*pi/P
dt = P/24      # time lag is one hour
tmax = 3*P     # 3 day and night simulation
T0 = 10        # mean temperature in Celsius
A = 10         # max amplitude variation
a = sqrt(omega/(2*k))
D = -(1/a)*log(0.001) # maximal depth
n = 501        # number of points in z-direction

def T(z,t):
   """
   Evaluates our mathematical model.
   """
   return T0 + A*exp(-a*z)*cos(omega*t - a*z)

def main():
   """
   Calls the animate command to make a movie.
   """
   z = linspace(0,D,n)
   while True:
      animate(tmax,dt,z,T,T0-A,T0+A,0,'z','T')
      ans = raw_input('play it again? (y/n) ')
      if ans != 'y': break

main()
