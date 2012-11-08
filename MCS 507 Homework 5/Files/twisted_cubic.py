# L-16 MCS 507 Wed 3 Oct 2012 : twisted_cubic.py

# This script uses pyplot to show the twisted cubic,
# a space curve defined by x = t, y = t^2, z = t^3.

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# sample points of (t,t^2,t^3)
t = np.linspace(-5,5,100)
x = t; y = t**2; z = t**3
# open a new figure window
f = plt.figure()
# get current axes of the figure
a = f.gca(projection='3d')
# plot the sampled points
a.plot(x,y,z,label='the twisted cubic')
# show the label
a.legend()
# render the plot in the window
plt.show()
