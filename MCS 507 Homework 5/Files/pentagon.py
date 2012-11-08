# L-11 MCS 507 Fri 21 Sep 2012 : pentagon.py

# Illustration of canvas: drawing a quartic
# passing to the corners of a pentagon.
# The origin is at the top left corner.

from Tkinter import *
from math import *

d = 400      # number of pixels in rows/columns
r = 0.8*d/2  # radius of the pentagon
a = 2*pi/5   # dividing angle
L = [(d/2,d/2-r),\
     (d/2+r*cos(pi/2-a),d/2-r*sin(pi/2-a)),\
     (d/2+r*cos(pi/2-2*a),d/2-r*sin(pi/2-2*a)),\
     (d/2+r*cos(pi/2-3*a),d/2-r*sin(pi/2-3*a)),\
     (d/2+r*cos(pi/2-4*a),d/2-r*sin(pi/2-4*a))]

wdw = Tk()
wdw.title('five points')
c = Canvas(wdw,width=d,height=d,bg='white')
c.pack()
for p in L:
   c.create_oval(p[0]-6,p[1]-6,p[0]+6,p[1]+6,\
       width=1,outline='black',fill='SkyBlue2') 

import numpy as np
A = np.array([x for (x,y) in L])
B = np.array([y for (x,y) in L])
quartic = np.polyfit(A,B,4)
for i in xrange(400):
   j = np.polyval(quartic,i)
   c.create_oval(i-1,j-1,i+1,j+1,\
      width=1,outline='red',fill='red')

wdw.mainloop()
