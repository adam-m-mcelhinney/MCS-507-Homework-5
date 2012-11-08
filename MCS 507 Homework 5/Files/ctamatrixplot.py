# L-22 MCS 507 Wed 17 Oct 2012 : ctamatrixplot.py

# This script creates a sparse matrix A,
# which is the adjacency matrix of the stops:
# A[i,j] = 1 if stops i and j are connected.

from scipy import sparse
import matplotlib.pyplot as plt

filename = 'CTA/stop_times.txt'
print 'opening', filename, '...'
file = open(filename,'r')

n = 12165
A = sparse.dok_matrix((n,n))

i = 0; prev_id = -1; prev_hd = ''
while True:
   d = file.readline()
   if d == '': break
   L = d.split(',')
   try:
      id = int(L[3]); hd = L[5]
      if(prev_id == -1):
         prev_id = id; prev_hd = hd
      else:
         if(prev_hd == hd):
            A[prev_id,id] = 1
         else:
            prev_id = id; prev_hd = hd
   except:
      pass # print 'skipping line', i
   i = i + 1

B = sparse.coo_matrix(A)
x = B.row; y = B.col
fig = plt.figure() 
ax  = fig.add_subplot(111) 
ax.set_xlim(-1,n)
ax.set_ylim(-1,n)
ax.plot(x,y,'b.')
plt.show()
