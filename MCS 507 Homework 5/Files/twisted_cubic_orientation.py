# L-16 MCS 507 Wed 3 Oct 2012 : twisted_cubic_orientation.py

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

print 'plotting the twisted cubic'
az = input('give the azimuth : ')
el = input('give the elevation : ')

t = np.linspace(-5,5,100)
x = t; y = t**2; z = t**3
f = plt.figure()
# get current axes of the figure
a = f.gca(projection='3d',
    azim=az,elev=el)
L = 'azimuth = %d, elevation = %d' % (az,el)
a.plot(x,y,z,label=L)
a.legend()
plt.show()
