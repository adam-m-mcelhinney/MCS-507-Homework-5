# L-20 MCS 507 Fri 12 Oct 2012 : showpaths.py

# The adjacency matrix A of a graph of n vertices
# is a symmetric n-by-n matrix, defined as follows:
# A[i,j] = 1, if vertex i and j are connected by an edge,
# A[i,j] = 0, otherwise.

# We say that two vertices i and j are connected by a path of
# length m if one can go from i to j by walking along m edges. 
# To denote a path, we list the vertices connected by the edges
# along the path.  A path of length m is a list of m+1 vertices.

# Write a script that given an n-by-n adjacency matrix A
# (as a numpy matrix) and two vertices i and j,
# prints all paths of length at most n that connect the two vertices.
# Every vertex in the path should be visited only once.

import numpy as np

def show_paths(A,n,j,L):
  """
  Prints all paths from i to j.
  """
  i = L[len(L)-1]
  if A[i,j] == 1:
     print L + [j]
  else:
     if len(L) < n:
        for k in range(n):
           if A[i,k] == 1 and not (k in L):
              show_paths(A,n,j,L+[k])

n = input('give n : ')
A = np.random.random_integers(0,1,size=(n,n))
A = (A + A.transpose())/2
print A
i = input('give i : ')
j = input('give j : ')
show_paths(A,n,j,[i])
