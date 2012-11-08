# L-14 MCS 507 Fri 28 Sep 2012 : power_show.py

# matplotlib animation of the convergence 
# of the power method

import numpy as np
from knowneigs import generate_matrix
from power_iterator import Power_Method

import matplotlib
import matplotlib.pyplot as plt

def animate(pw):
   """
   Shows the progress towards 
   the dominant eigenvalue.
   """
   plt.ion()
   fig = plt.figure() 
   ax  = fig.add_subplot(111) 
   ax.set_xlim(-2,2)
   ax.set_ylim(-2,2)
   x = [float(np.real(pw.v))]
   y = [float(np.imag(pw.v))]
   dots, = ax.plot(x,y,'ro')
   fig.canvas.draw()
   for i in range(100):
      pw.next()
      print pw
      x.append(float(np.real(pw.v)))
      y.append(float(np.imag(pw.v)))
      dots.set_xdata(x)  # update data for plot
      dots.set_ydata(y)
      plt.pause(1)        # pause for a second
      fig.canvas.draw()   # update canvas
      if pw.accurate(): break
   ans = raw_input('hit enter to exit')

def main():
   """
   Generates a matrix with given eigenvalues
   and launches the animation.
   """
   print 'Running the power method...'
   n = input('Give the dimension : ')
   # m = input('Convergence factor ? ')
   m = 1.2
   L = np.random.uniform(0,2*np.pi,n)
   j = complex(0,1)
   K = np.exp(j*L)
   for i in range(1,len(K)): K[i] = K[i]/m
   A = generate_matrix(K)
   p = Power_Method(n,eps=1.0e-2,A=A);
   animate(p)

if __name__=="__main__": main()
