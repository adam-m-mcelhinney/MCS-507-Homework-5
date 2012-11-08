# L-29 MCS 507 Fri 2 Nov 2012 : extrapoldiff.py

# We inherit the forward difference approximation and apply once
# Richardson extrapolation to improve the accuracy of the approximation.

from subformdiff import *

class Extrapolate(Forward):
   """
   Applies Richardson extrapolation on
   forward difference approximations.
   """
   def __call__(self,x):
      h = self.h
      dfh = Forward.__call__(self,x)
      self.h = self.h/2
      dfh2 = Forward.__call__(self,x)
      self.h = h
      r = 2*dfh2 - dfh
      return r

def main():
   """
   Simple test on difference
   approximations of functions.
   """
   f = lambda x: 7*x**2 - 5*x + 3
   print 'f = 7 x^2 - 5 x + 3'
   dfh1 = Forward(f)
   dfh2 = Extrapolate(f)
   print 'df(1) ~ %.16f' % dfh1(1)
   print 'df(1) ~ %.16f' % dfh2(1)

if __name__=="__main__": main()
