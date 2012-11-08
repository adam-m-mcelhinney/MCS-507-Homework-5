# L-25 MCS 507 Wed 24 Oct 2012 : doubleDoubleCalc.py

# Test the double double arithmetic.

import doubleDouble

def test_arithmetic():
   """
   Basic test on arithmetical operations.
   """
   hi = 1.4142135623730951
   lo = -9.6672933134529147e-17
   x = (hi,lo)     # defines the sqrt(2)
   print 'x = sqrt(2) = ', doubleDouble.str(x[0],x[1])
   y = (1.0,0.0)
   z = doubleDouble.add(x[0],x[1],y[0],y[1])
   print 'x + 1 = ', doubleDouble.str(z[0],z[1])
   xx = doubleDouble.sub(z[0],z[1],y[0],y[1])
   print 'x + 1 - 1 = ', doubleDouble.str(x[0],x[1])
   x2 = doubleDouble.mul(x[0],x[1],x[0],x[1])
   print 'x*x = ', doubleDouble.str(x2[0],x2[1])
   x2dx = doubleDouble.div(x2[0],x2[1],x[0],x[1])
   print 'x*x/x = ', doubleDouble.str(x2dx[0],x2dx[1])

def test_newton4sqrt2():
   """
   Applies Newton's method to approximate the
   square root of two with double double arithmetic.
   """
   x = [2.0, 0.0]
   print 'step 0 :', doubleDouble.str(x[0],x[1])
   for i in range(1,9):
      z = doubleDouble.mul(x[0],x[1],x[0],x[1])
      z = doubleDouble.add(z[0],z[1],2.0,0.0)
      z = doubleDouble.div(z[0],z[1],x[0],x[1])
      z = doubleDouble.mul(z[0],z[1],0.5,0.0)
      x[0] = z[0]
      x[1] = z[1]
      print 'step', i, ':', doubleDouble.str(x[0],x[1])

test_arithmetic()
ans = raw_input('continue ? (y/n) ')
test_newton4sqrt2()
ans = raw_input('continue ? (y/n) ')
