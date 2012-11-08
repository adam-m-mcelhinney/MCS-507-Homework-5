# L-507 MCS 507 Wed 19 Sep 2012 : newtoncallback.py

# Newton function to find a root of a nonlinear equation f(x) = 0
# uses the formula x(k+1) = x(k) - f(x(k))/f'(x(k)), where f' is
# the derivative of f, starting at some x(0).

# The function illustrates the use of a callback function.
# A callback function can report intermediate results and
# also provide data to the function it calls.

# Instead of using an optional argument, we use "None"
# as default value.

from sympy import *

def Newton(f,df,x0,n=5,eps=1.0e-8,g=None):
   """
   Runs Newton's method on f(x) = 0.

   INPUT PARAMETERS :
     f    a function in one variable,
     df   derivative of the function f,
     x0   initial guess for the root,
     n    maximum number of iterations,
     eps  accurary requirement on |f(x)|
          and on the update to x, |dx|

   ON RETURN :
     x    approximation for the root,
     dx   magnitude of last correction,
     y    residual |f(x)|
     fail is true if accuracy not reached.
   """
   x = x0; fail = True
   for i in xrange(n):
      dx = -f(x)/df(x)
      x = x + dx
      y = abs(f(x))
      fail = ((abs(dx) > eps) and (y > eps))
      if g != None:
         D = {'step': i+1, 'x': x, 'dx': dx, 'res': y}
         proceed = g(D)
         if proceed != None:
            if not proceed: break
      if not fail: break
   return (x,abs(dx),y,fail)

def print_steps(D):
   """
   Prints the content of the dictionary D
   and prompts the user to continue or not.
   """
   s = ""
   for k in D.keys():
      s = s + "  " + k + ' = '
      if ((k == 'dx') or (k == 'res')):
         s = s + ('%.3e' % D[k])
      else:
         s = s + str(D[k])
   print s
   answer = raw_input("continue ? (y/n) ")
   return (answer == 'y')

def main():
   """
   Prompts the user for an expression in x,
   computes its derivative and calls Newton.
   """
   var('x')
   e = input('Give an expression in x : ')
   d = e.diff(x)
   f = lambda v: Subs(e,(x),(v)).doit()
   df = lambda v: Subs(d,(x),(v)).doit()
   x0 = input('Give an initial guess : ')
   x0 = float(x0)
   print Newton(f,df,x0,g=print_steps)

main()
