# L-26 MCS 507 Fri 26 Nov 2012 : showpoint.py

# Inheriting from the class Point, we extend a point with a canvas
# data attribute and with a method to draw the point on the canvas.
# The main program pops a new window with a canvas and draws ten
# random points on the canvas.

from Tkinter import *
from classpoint import *

class ShowPoint(Point):
   """
   Extends the Point class 
   with a draw method.
   """
   def __init__(self,cv,x=0,y=0):
      """
      Defines the coordinates
      and stores the canvas.
      """
      Point.__init__(self,x,y)
      self.canvas = cv

   def draw(self):
      """
      Draws the point on canvas.
      """
      a = self.x; b = self.y
      self.canvas.create_oval(a-3, \
         b-3,a+3,b+3,fill='SkyBlue2')

def main():
   """
   Shows 10 random points on canvas.
   """
   top = Tk()
   d = 400
   c = Canvas(top,width=d,height=d)
   c.pack()
   from random import randint
   L = []
   for i in xrange(10):
      a = randint(6,d-6)
      b = randint(6,d-6)
      L.append(ShowPoint(c,a,b))
   for p in L: p.draw()
   top.mainloop()

if __name__=="__main__": main()
