# L-14 MCS 507 Fri 28 Sep 2012 : power_iterator.py

# This script exports a class for the power method.

import numpy as np

class Power_Method():
   """
   Provides an iterator for the power method
   to find the dominant eigenvalue of a matrix.
   """
   def __init__(self,n,eps=1.0e-8,**data):
      """
      Stores the class and the current
      approximation for the eigenvector
      with the dominant eigenvalue.
      The dimension equals n.
      If the dictionary data does not
      contain an element with key A,
      then a random matrix is generated.
      If the dictionary data does not
      contain an element with key x0,
      then a random vector is generated.
      """
      self.step = 0     # step size
      self.v = 0        # dominant eigenvalue
      self.acc = 1.0    # accuracy estimate
      self.eps = eps    # accuracy requirement
      j = complex(0,1)
      if data.has_key('A'):
         self.A = data['A']
      else:
         a = np.random.normal(0,1,(n,n)) \
           + np.random.normal(0,1,(n,n))*j
         self.A = np.matrix(a)
      if data.has_key('x0'):
         self.x = data['x0']
      else:
         x = np.random.normal(0,1,(n,1)) \
           + np.random.normal(0,1,(n,1))*j
         self.x = np.matrix(x)

   def __repr__(self):
      """
      Defines the representation.
      """
      return self.__str__()

   def __str__(self):
      """
      The string representation shows
      the current step and approximation
      for the dominant eigenvector.
      """
      s = "step %d : " % self.step
      ac = np.ndarray.tolist(self.acc)
      s = s + ('err : %.3e' % ac[0][0]) + '\n'
      ev = np.ndarray.tolist(self.v)
      s = s + 'lambda = ' + str(ev[0][0]) + '\n'
      s = s + str(self.x)
      return s

   def next(self):
      """
      The next step of the power method.
      """
      self.step = self.step + 1
      y = self.A*self.x
      z = y[0]/self.x[0]
      self.acc = abs(z - self.v)
      self.v = z
      self.x = y/np.linalg.norm(y)

   def accurate(self):
      """
      Returns true if the accuracy equals
      the tolerance.
      """
      return (self.acc < self.eps)

def check(A,Y):
   """
   Compares the output Y of the power
   method with the largest eigenvalue.
   """
   Z = A*Y
   la = Z[0]/Y[0]
   print 'computed eigenvalue :' , la
   [L,V] = np.linalg.eig(A)
   K = list(abs(L))
   k = K.index(max(K))
   print ' largest eigenvalue :', L[k]
   
def main():
   """
   Prompts the user for a dimension
   and the number of iterations.
   """
   print 'Running the power method...'
   n = input('Give the dimension : ')
   j = complex(0,1)
   a = np.random.normal(0,1,(n,n)) \
     + np.random.normal(0,1,(n,n))*j
   x = np.random.normal(0,1,(n,1)) \
     + np.random.normal(0,1,(n,1))*j
   A = np.matrix(a); X = np.matrix(x)
   p = Power_Method(n,A=A,x0=X);
   for i in range(1000):
      p.next()
      print p
      if p.accurate(): break
   Y = p.x
   check(A,Y)

if __name__=="__main__": main()
