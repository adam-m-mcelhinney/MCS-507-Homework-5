# L-30 MCS 507 Mon 5 Nov 2012 : spy_plot_movie.py

# The script uses scitools.std to plot the pattern 
# of random matrices in an animation.

import numpy as np
from scitools.std import plot
from scipy import sparse

r = 0.1  # ratio of nonzeroes
n = 100  # dimension of the matrix
for i in xrange(n):
   A = np.random.rand(n,n)
   A = np.matrix(A < r,int)
   S = sparse.coo_matrix(A)
   x = S.row; y = S.col
   plot(x,y,'ro',axis=[-1, n, -1, n], \
        title='matrix %d has %d nonzeroes' % (i, S.nnz))
