# L-16 MCS 507 Wed 3 Oct 2012 : sympy_cplot.py

# If matplotlib is installed, then we can plot surfaces
# with the visualization module of the package sympy.mpmath.

# Below we illustrate the command cplot to make complex plots
# of the taking 2nd, 3rd, 4th, and 5th root.
# The plots show the branches of the n-th root function
# as the coloring of the Riemann surface.

# The color shows the argument (or phase) of the root
# and the magnitude is shown as brightness.
# The pattern of colors show the n in the n-th root.

# As we follow the recommendation of the documentation
# to increase the number of points to 100,000
# this script takes a while.

import matplotlib
import matplotlib.pyplot as plt

from sympy.mpmath import *
fig = plt.figure()
print '....please be patient....'
print '...for several minutes...'
print 'making the first plot...'
a1 = fig.add_subplot(221)
cplot(f=lambda x: x**2,re=[-1, 1],im=[-1,1], \
      points=100000,axes=a1)
print 'making the second plot...'
a2 = fig.add_subplot(222)
cplot(f=lambda x: x**3,re=[-1, 1],im=[-1,1], \
      points=100000,axes=a2)
print 'making the third plot...'
a3 = fig.add_subplot(223)
cplot(f=lambda x: x**4,re=[-1, 1],im=[-1,1], \
      points=100000,axes=a3)
print 'making the fourth plot...'
a4 = fig.add_subplot(224)
cplot(f=lambda x: x**5,re=[-1, 1],im=[-1,1], \
      points=100000,axes=a4)
fig.show()
ans = raw_input('type enter to exit')
