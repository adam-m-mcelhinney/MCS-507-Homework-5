# L-507 MCS 507 Wed 19 Sep 2012 : newtonfun.py

# Newton function to find a root of a nonlinear equation f(x) = 0
# uses the formula x(k+1) = x(k) - f(x(k))/f'(x(k)), where f' is
# the derivative of f, starting at some x(0).

# The function illustrates the use of a break inside a loop.
# We apply sympy to compute the derivative of an expression.

from sympy import *

def Newton(f,df,x0,n=5,eps=1.0e-8):
   """
   Runs Newton's method on f(x) = 0.

   INPUT PARAMETERS :
     f    a function in one variable,
     df   derivative of the function f,
     x0   initial guess for the root,
     n    maximum number of iterations,
     eps  accurary requirement on |f(x)|
          and on the update to x, |dx|.

   ON RETURN : the tuple (x,dx,y,fail), with:
     x    approximation for the root,
     dx   magnitude of last correction,
     y    residual |f(x)|,
     fail is true if accuracy not reached.
   """
   x = x0; fail = True
   for i in xrange(n):
      dx = -f(x)/df(x)
      x = x + dx
      y = abs(f(x))
      if ((abs(dx) <= eps) or (y <= eps)):
         fail = False
         break
   return (x,abs(dx),y,fail)

def main():
   """
   Prompts the user for an expression in x,
   computes its derivative and calls Newton.
   """
   var('x')
   e = input('Give an expression in x : ')
   d = e.diff(x) # using sympy
   f = lambda v: Subs(e,(x),(v)).doit()
   df = lambda v: Subs(d,(x),(v)).doit()
   x0 = input('Give an initial guess : ')
   x0 = float(x0) # force float arithmetic
   print Newton(f,df,x0)

main()
