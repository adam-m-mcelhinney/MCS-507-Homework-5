# L-26 MCS 507 Fri 26 Nov 2012 : showline.py

# Inheriting from the class Line, we extend a point with a canvas
# data attribute and with a method to draw a line on the canvas.
# The main program pops a new window with a canvas and draws
# eleven random lines on the canvas.

from Tkinter import *
from classpoint import *
from classline import *

class ShowLine(Line):
   """
   Extends the Line class
   with a draw method.
   """
   def __init__(self,c,d,x=0,y=0,a=0):
      """
      Defines the line and stores
      the canvas c of dimension d.
      """
      Line.__init__(self,x,y,a)
      self.canvas = c
      self.dimension = d

   def draw(self):
      """
      Draws the line on canvas.
      """
      a = self.x; b = self.y
      self.canvas.create_oval(a-3, \
         b-3,a+3,b+3,fill='SkyBlue2')
      da = self.dimension - a
      cs = cos(self.angle)
      if cs + 1.0 != 1.0:
         t = da/cs
         p = Line.__call__(self,t)
         self.canvas.create_line(a,b,p.x,p.y)
         t = a/cs
         q = Line.__call__(self,-t)
         self.canvas.create_line(q.x,q.y,a,b)
      else: # vertical line
         self.canvas.create_line(a,0,a,self.dimension)

def main():
   """
   Shows 11 lines on canvas.
   """
   top = Tk()
   d = 400
   c = Canvas(top,width=d,height=d)
   c.pack()
   from random import uniform, randint
   from math import pi
   L = [ShowLine(c,d,100,300,pi/2)]
   for i in xrange(10):
      a = randint(6,d-6)
      b = randint(6,d-6)
      r = uniform(0,2*pi)
      L.append(ShowLine(c,d,a,b,r))
   for e in L: e.draw()
   top.mainloop()

if __name__=="__main__": main()
