# L-16 MCS 507 Wed 3 Oct 2012 : quadratic_cylinder.py

# This script uses pyplot of matplotlib to plot
# the parabolic cylinder y = x^2.

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

f = plt.figure()
a = f.gca(projection='3d')
x = np.arange(-1,1,0.01)
z = np.arange(-1,1,0.01)
X, Z = np.meshgrid(x,z)
Y = X**2

s = a.plot_surface(X,Y,Z,cmap=cm.jet)
f.colorbar(s,shrink=0.5)

plt.show()
