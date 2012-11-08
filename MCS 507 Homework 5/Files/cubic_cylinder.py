# L-16 MCS 507 Wed 3 Oct 2012 : cubic_cylinder.py

# This script uses pyplot of matplotlib to plot
# the cubic cylinder z = x^3.

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

f = plt.figure()
a = f.gca(projection='3d')
x = np.arange(-1,1,0.01)
y = np.arange(-1,1,0.01)
X, Y = np.meshgrid(x,y)
Z = X**3

s = a.plot_surface(X,Y,Z,cmap=cm.jet)
f.colorbar(s,shrink=0.5)

plt.show()
