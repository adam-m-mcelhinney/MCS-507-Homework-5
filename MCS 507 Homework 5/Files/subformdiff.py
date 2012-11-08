# L-29 MCS 507 Fri 2 Nov 2012 : subformdiff.py

# The parent class stores code common to all differentiation formulas for
# callable objects: the object that is differentiated and the step size.
# The test illustrates the difference between O(h) and O(h^2) errors.

class Diff:
    """
    The superclass stores code 
    common to all differentiation
    formulas for any callable object.
    """
    def __init__(self,f,h=1.0E-5):
       """
       Store function and step size
       for numerical differentiation.
       """
       self.f = f
       self.h = float(h)

class Forward(Diff):
   """
   Applies forward differences.
   """
   def __call__(self,x):
      """
      Returns forward difference
      approximation for derivative.
      """
      f, h = self.f, self.h
      return (f(x+h) - f(x))/h

class Backward(Diff):
   """
   Applies backward differences.
   """
   def __call__(self,x):
      """
      Returns backward difference
      approximation for derivative.
      """
      f, h = self.f, self.h
      return (f(x) - f(x-h))/h

class Central(Diff):
   """
   Applies central differences.
   """
   def __call__(self,x):
      """
      Returns central difference
      approximation for derivative.
      """
      f, h = self.f, self.h
      return (f(x+h) - f(x-h))/(2*h)

def main():
   """
   Simple test on difference
   approximations of functions.
   """
   f = lambda x: 7*x**2 - 5*x + 3
   forw = Forward(f)
   back = Backward(f)
   cent = Central(f)
   print ' forward : %.16f' % forw(1)
   print 'backward : %.16f' % back(1)
   print ' central : %.16f' % cent(1)

if __name__=="__main__": main()
