# L-26 MCS 507 Fri 26 Oct 2012 : classparabola.py

from classpoint import *
from classline import *

class Parabola(Line):
   """
   A parabola is defined by a line,
   its directrix and a point, its focus.
   """
   def __init__(self,x,y,a,b,c):
      """
      Defines the line at (x,y)
      and angle a and focus (b,c).
      """
      Line.__init__(self,x,y,a)
      self.focus = Point(b,c)

   def __str__(self):
      """
      Returns the string representation.
      """
      F = str(self.focus)
      L = Line.__str__(self)
      s = 'focus : ' + F
      s = s + ', directrix : ' + L
      return s

   def __call__(self,t):
      """
      Returns a point on the parabola
      as far from the focus and the point
      obtained by evaluating the directrix.
      """
      c = Line.__call__(self,t)
      fx = self.focus.x
      fy = self.focus.y
      d = 2*(fx - c.x)*(c.y - self.y) \
        - 2*(fy - c.y)*(c.x - self.x)
      r1 = fx**2 + fy**2 - c.x**2 - c.y**2
      if d + 1.0 != 1.0:
         r2 = c.x*(c.x - self.x) + c.y*(c.y - self.y)
         dx = (r1*(c.y - self.y) - 2*r2*(fy - c.y))/float(d)
         dy = (2*(fx - c.x)*r2 - (c.x - self.x)*r1)/float(d)
      else:
         c10 = Line.__call__(self,10)
         d = 2*(fx - c.x)*(c10.y - self.y) \
           - 2*(fy - c.y)*(c10.x - self.x)
         r2 = c10.x*(c10.x - self.x) + c10.y*(c10.y - self.y)
         dx = (r1*(c10.y - self.y) - 2*r2*(fy - c.y))/float(d)
         dy = (2*(fx - c.x)*r2 - (c10.x - self.x)*r1)/float(d)
      return Point(dx,dy)

def main():
   """
   Instantiates a parabola.
   """
   p = Parabola(3,4,-1.23,10,0)
   print p
   q = p(4)
   print q

if __name__=="__main__": main()
