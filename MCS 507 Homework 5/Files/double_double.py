# L-26 MCS 507 Fri 26 Oct 2012 : double_double.py

# With the operator overloading in Python we encapsulate the
# wrapping of the doubleDouble module in the class DoubleDouble.

import doubleDouble

class DoubleDouble():
   """
   Wraps some of the functionality of the QD library
   to perform double double arithmetic.
   """
   def __init__(self,hi=0.0,lo=0.0):
      """
      A double double consists of a high and a low part.
      """
      self.high = hi
      self.low = lo

   def __str__(self):
      """
      Returns the string representation of a double double.
      """
      return doubleDouble.str(self.high,self.low)

   def __repr__(self):
      """
      Returns the representation of a double double.
      """
      return self.__str__()

   def copy(self):
      """
      Returns a copy of the double double.
      """
      return DoubleDouble(self.high,self.low)

   def __add__(self,other):
      """
      Returns the sum of two double doubles.
      """
      z = doubleDouble.add(self.high,self.low,other.high,other.low)
      return DoubleDouble(z[0],z[1])

   def __sub__(self,other):
      """
      Returns the difference of self and the other.
      """
      z = doubleDouble.sub(self.high,self.low,other.high,other.low)
      return DoubleDouble(z[0],z[1])

   def __mul__(self,other):
      """
      Returns the product of two double doubles.
      """
      z = doubleDouble.mul(self.high,self.low,other.high,other.low)
      return DoubleDouble(z[0],z[1])

   def __div__(self,other):
      """
      Returns the division of self by the other.
      """
      z = doubleDouble.div(self.high,self.low,other.high,other.low)
      return DoubleDouble(z[0],z[1])

   def __pow__(self,n):
      """
      Returns self to the power n.
      """
      z = self.copy()
      for i in range(1,n):
         z = z*self
      return z

def newton4sqrt2():
   """
   Applies Newton's method to approximate sqrt(2).
   """
   x = DoubleDouble(2.0)
   print 'step 0 :', x
   for i in range(1,9):
      z = x**2
      z = z + DoubleDouble(2.0)
      z = z/x
      z = DoubleDouble(0.5)*z
      x = z.copy()
      print 'step', i, ':', x

def test():
   """
   Basic test on arithmetical operations.
   """
   hi = 1.4142135623730951
   lo = -9.6672933134529147e-17
   x = DoubleDouble(hi,lo)     # defines the sqrt(2)
   print 'x = sqrt(2) =', str(x)
   y = x**2
   print 'x*x =', y
   z = y/x
   print 'x*x/x =', z
   u = x+x
   print 'x+x =', u
   two = DoubleDouble(2.0)
   print '2*x =', two*x
   v = u-x
   print 'x+x-x =', v
   newton4sqrt2()

if __name__=="__main__": test()
