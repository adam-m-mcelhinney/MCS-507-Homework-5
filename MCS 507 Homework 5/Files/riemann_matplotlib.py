# L-16 MCS 507 Wed 3 Oct 2012 : riemann_matplotlib.py

# This script uses pyplot of matplotlib to plot
# the Riemann surface of the cubed root.

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

f = plt.figure()
a = f.gca(projection='3d')
u = np.arange(-1,1,0.01)
v = np.arange(-1,1,0.01)
U, V = np.meshgrid(u,v)
X = U**3 - 3*U*V**2
Y = 2*U**2*V - V**3

# scale colors so that in [0,1]
cV = (1.0 + V)/2

# s = a.plot_surface(X,Y,U,rstride=1,cstride=1,facecolors=cm.jet(cV))
s = a.plot_surface(X,Y,U,facecolors=cm.jet(cV))

plt.show()
