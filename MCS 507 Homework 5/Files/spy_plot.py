# L-30 MCS 507 Mon 5 Nov 2012 : spy_plot.py

# We plot the pattern of a random matrix
# using plot of scitools.std.

import numpy as np
from scitools.std import plot

r = 0.1 # ratio of nonzeroes
n = 100 # dimension of the matrix
A = np.random.rand(n,n)
A = np.matrix(A < r,int)
print A
from scipy import sparse
S = sparse.coo_matrix(A)
print 'number of nonzeros :', S.nnz
x = S.row; y = S.col
plot(x,y,'ro',axis=[-1, n, -1, n])
ans = raw_input('quit ? (y/n) ')
