# L-26 MCS 507 Fri 26 Oct 2012 : showparabola.py

from Tkinter import *
from classparabola import *

class ShowParabola(Parabola):
   """
   Extends the Parabola class
   with a draw method.
   """
   def __init__(self,cv,d,x,y,a,b,c):
      """
      Defines the parabola and stores
      the canvas cv of dimension d.
      """
      Parabola.__init__(self,x,y,a,b,c)
      self.canvas = cv
      self.dimension = d

   def draw_directrix(self):
      """
      Draws the directrix on canvas.
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
         print 'vertical line'
         self.canvas.create_line(a,0,a,self.dimension)

   def draw_focus(self):
      """
      Draws the focus on canvas.
      """
      fx = self.focus.x
      fy = self.focus.y
      self.canvas.create_oval(fx-3, \
         fy-3,fx+3,fy+3,fill='SkyBlue2')

   def draw(self):
      """
      Draws the parabola on canvas.
      """
      self.draw_directrix()
      self.draw_focus()
      for t in xrange(-1000,1000):
         p = Parabola.__call__(self,t)
         self.canvas.create_oval(p.x-1, \
            p.y-1,p.x+1,p.y+1,fill='SkyBlue2')

def main():
   """
   Draws a parabola
   """
   top = Tk()
   d = 400
   c = Canvas(top,width=d,height=d)
   c.pack()
   from math import pi
   from random import randint
   from random import uniform
   L = []
   for i in xrange(1):
      x = randint(6,d-6)
      y = randint(6,d-6)
      r = uniform(0,2*pi) 
      a = randint(6,d-6);
      b = randint(6,d-6);
      L.append(ShowParabola(c,d,x,y,r,a,b))
   for e in L: e.draw()
   top.mainloop()

if __name__=="__main__": main()
