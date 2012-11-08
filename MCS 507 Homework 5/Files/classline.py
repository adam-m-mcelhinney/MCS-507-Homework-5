# L-26 MCS 507 Fri 26 Nov 2012 : classline.py

# We define a line as a point and a direction,
# inheriting from the class Point.
# The line is a callable object, evaluating the line
# yields points on the line.
# The main program illustrates instantiations and the call method.

from classpoint import *
from math import cos, sin

class Line(Point):
   """
   A line is a base point and
   a direction angle.
   """
   def __init__(self,x=0,y=0,a=0):
      """
      Defines base point and angle.
      """
      Point.__init__(self,x,y)
      self.angle = a

   def __str__(self):
      """
      Returns the string representation.
      """
      p = Point.__str__(self)
      a = ', angle = ' + str(self.angle)
      return p + a

   def __repr__(self):
      """
      Returns the representation.
      """
      return self.__str__()

   def __call__(self,t):
      """
      Returns a new point on the line.
      """
      xt = self.x + t*cos(self.angle)
      yt = self.y + t*sin(self.angle)
      return Point(xt,yt)

def main():
   """
   Instantiates two points.
   """
   L = Line()
   print 'L =', L
   q = Line(3,4,10)
   p = q(4)
   print p

if __name__=="__main__": main()
