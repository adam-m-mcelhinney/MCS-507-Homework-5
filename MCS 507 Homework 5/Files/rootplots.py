# L-19 MCS 507 Wed 10 Oct 2012 : rootplots.py

# Roots of random polynomials tend to lie
# around the unit circle in the complex plane.
# Write a script to make a plot of the roots
# of a random polynomial of degree 100. 

from matplotlib import pyplot as plt
import numpy as np

p = np.random.rand(100)
r = np.roots(p)
L = list(r)
re = [c.real for c in L]
im = [c.imag for c in L]
plt.plot(re,im,'bo')
plt.show()
