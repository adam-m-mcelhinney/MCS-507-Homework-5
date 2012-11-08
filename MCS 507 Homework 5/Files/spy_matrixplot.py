import numpy as np
from matplotlib.pyplot import spy
import matplotlib.pyplot as plt
from scipy import sparse

r = 0.1 # ratio of nonzeroes
n = 100 # dimension of the matrix
A = np.random.rand(n,n)
A = np.matrix(A < r,int)
S = sparse.coo_matrix(A)
x = S.row; y = S.col
fig = plt.figure() 
ax  = fig.add_subplot(111) 
ax.plot(x,y,'.')
plt.show()
