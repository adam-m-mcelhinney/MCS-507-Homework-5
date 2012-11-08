# L-20 MCS 507 Fri 12 Oct 2012 : graphplot.py

# The adjacency matrix A of a graph of n vertices
# is a symmetric n-by-n matrix, defined as follows:
# A[i,j] = 1, if vertex i and j are connected by an edge,
# A[i,j] = 0, otherwise.

import numpy as np

n = input('give n : ')
A = np.random.random_integers(0,1,size=(n,n))
A = (A + A.transpose())/2
print A

from matplotlib import pyplot as plt
import numpy as np

x = [np.cos(2*k*np.pi/n) for k in range(n)]
y = [np.sin(2*k*np.pi/n) for k in range(n)]

for i in range(n):
   for j in range(i+1,n):
      if A[i,j] == 1: plt.plot([x[i],x[j]],[y[i],y[j]],'b-')

plt.axis([-1.5,1.5,-1.5,1.5])
plt.plot(x,y,'bo')
plt.show()
