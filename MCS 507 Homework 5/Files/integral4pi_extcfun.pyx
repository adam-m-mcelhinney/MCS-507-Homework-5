# L-31 MCS 507 Wed 7 Nov 2012 : integral4pi_extcfun.pyx

# This script applies the composite trapezoidal rule 
# to the integral of sqrt(1-x^2) for x from 0 to 1,
# to obtain an approximation for pi.
# Type declarations have been added so the for loop
# will be compiled into pure C code.
# Instead of the sqrt of the Python math library,
# we call the sqrt of the external C library.
# To avoid the construction of float objects around function calls,
# we declare a C-style function.

cdef extern from "math.h":
   double sqrt(double)

cdef double circle(double x) except *:
   return sqrt(1-x**2)

def integral4pi(int n):
   cdef int i
   cdef double h, r
   h = 1.0/n
   r = (circle(0)+circle(1))/2
   for i in range(n):
      r += circle(i*h)
   return 4*r*h
