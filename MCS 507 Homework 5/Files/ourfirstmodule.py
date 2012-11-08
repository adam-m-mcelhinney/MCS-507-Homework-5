# L-7 MCS 507 Wed 12 Sep 2012 : ourfirstmodule.py

# A module is a collection of functions.
# This module exports two functions: f and main.
# By the last line of this file, we can run this
# script at the command prompt $ as
# $ python ourfirstmodule.py.
# Alternatively, we can import f and/or main
# in an interactive Python session.

def f(x,y,z):
   """
   Returns the value of the expression
     x**2*cos(y) + 4*exp(z)*sin(x)
   for numerical values of x, y, and z.
   """
   from math import exp, cos, sin
   v = x**2*cos(y) + 4*exp(z)*sin(x)
   return v 

def main():
   """
   Prompts the user for three values
   for the variables x, y, z and
   prints x**2*cos(y) + 4*exp(z)*sin(x).
   """
   print 'v = x**2*cos(y) + 4*exp(z)*sin(x)'
   x = input('give x : ')
   y = input('give y : ')
   z = input('give z : ')
   v = f(x,y,z)
   print 'v = ', v

if __name__ == "__main__": main()
