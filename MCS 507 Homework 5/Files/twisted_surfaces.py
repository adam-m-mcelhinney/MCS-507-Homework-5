# L-16 MCS 507 Wed 3 Oct 2012 : twisted_surfaces.py

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

f = plt.figure()
a2 = f.gca(projection='3d',azim=-117,elev=15)

x2 = np.arange(-1,1,0.03)
z2 = np.arange(-1,1,0.03)
X2, Z2 = np.meshgrid(x2,z2)
Y2 = X2**2

a3 = f.gca(projection='3d')
x3 = np.arange(-1,1,0.01)
y3 = np.arange(-1,1,0.01)
X3, Y3 = np.meshgrid(x3,y3)
Z3 = X3**3
for i in xrange(X3.shape[0]):
  for j in xrange(X3.shape[1]):
     if X3[i,j]**2 < Y3[i,j]: Z3[i,j] = -1

s3 = a3.plot_surface(X3,Y3,Z3,rstride=1,cstride=1,
                     linewidth=0,cmap=cm.jet)
f.colorbar(s3,shrink=0.5)
plt.hold('on')
s2 = a2.plot_surface(X2,Y2,Z2,rstride=1,cstride=1,
                     linewidth=0,cmap=cm.jet)

plt.show()
