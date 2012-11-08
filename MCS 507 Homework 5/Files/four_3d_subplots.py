# L-16 MCS 507 Wed 3 Oct 2012 : four_3d_subplots.py

# This script displays in a figure window four subplots
# with axes of different azimuth.

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

f = plt.figure()
# first subplot with default view
f.add_subplot(221,projection='3d')
f.add_subplot(222,projection='3d',azim=-30,elev=30)
f.add_subplot(223,projection='3d',azim=0,elev=30)
f.add_subplot(224,projection='3d',azim=30,elev=30)
plt.show()
