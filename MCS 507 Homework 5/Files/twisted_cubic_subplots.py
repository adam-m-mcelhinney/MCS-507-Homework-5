# L-16 MCS 507 Wed 3 Oct 2012 : twisted_cubic_subplots.py

# This script displays in a figure window four subplots
# with different azimuth plot of the twisted cubic.

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5,5,100)
x = t; y = t**2; z = t**3
f = plt.figure()
# first subplot with default view
f.add_subplot(221,projection='3d')
a1 = f.gca()
az = a1.azim; el = a1.elev
t = 'azim = %d, elev = %d' % (az,el)
a1.set_title(t)
a1.plot(x,y,z)
# second subplot 
az = -30; el = 30
f.add_subplot(222,projection='3d',azim=az,elev=el)
a2 = f.gca()
t = 'azim = %d, elev = %d' % (az,el)
a2.set_title(t)
a2.plot(x,y,z)
# third subplot
az = 0; el = 30
f.add_subplot(223,projection='3d',azim=az,elev=el)
a3 = f.gca()
t = 'azim = %d, elev = %d' % (az,el)
a3.set_title(t)
a3.plot(x,y,z)
# fourth subplot
az = 30; el = 30
f.add_subplot(224,projection='3d',azim=az,elev=el)
t = 'azim = %d, elev = %d' % (az,el)
a4 = f.gca()
t = 'azim = %d, elev = %d' % (az,el)
a4.set_title(t)
a4.plot(x,y,z)
plt.show()
