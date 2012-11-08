# L-12 MCS 507 Mon 24 Sep 2012 : rgbgui.py

# This GUI illustrates the use of sliders in Tkinter.
# The users can manipulate the intensity of red, green, and blue
# as the background of the canvas.  Every time the scale widget
# is touched a variable holding the corresponding intensity is set
# and the command "ShowColors" is executed.

from Tkinter import *

class ColorGUI:
   """
   Manipulate rgb color parameters with scale widgets.
   """
   def __init__(self,wdw):
      """
      Defines canvas and three scales.
      """
      wdw.title('color slider')
      self.d = 400
      self.L = Label(wdw,text='use scales to change colors')
      self.L.grid(row=0,column=1)
      self.c = Canvas(wdw,width=self.d,height=self.d,bg='white')
      self.c.grid(row=1,column=1)
      self.Lr = Label(wdw,text='red')
      self.Lr.grid(row=0,column=0)
      self.r = DoubleVar()
      self.sr = Scale(wdw,orient='vertical',length=self.d,
         from_=0.0,to=1.0, resolution = 1.0/256, 
         variable=self.r,command=self.ShowColors)
      self.sr.set(0.5)
      self.sr.grid(row=1,column=0)
      self.Lb = Label(wdw,text='blue')
      self.Lb.grid(row=0,column=2)
      self.b = DoubleVar()
      self.sb = Scale(wdw,orient='vertical',length=self.d,
         from_=0.0,to=1.0,resolution = 1.0/256,
         variable=self.b,command=self.ShowColors)
      self.sb.set(0.5)
      self.sb.grid(row=1,column=2)
      self.Lg = Label(wdw,text='green')
      self.Lg.grid(row=2,column=0)
      self.g = DoubleVar()
      self.sg = Scale(wdw,orient='horizontal',length=self.d,
         from_=0.0,to=1.0,resolution = 1.0/256,
         variable=self.g,command=self.ShowColors)
      self.sg.set(0.5)
      self.sg.grid(row=2,column=1)

   def ShowColors(self,v):
      """
      Displays a rectangle on canvas, filled with rgb colors
      """
      x = self.d/2+1; y = self.d/2+1; d = self.d/2-3
      r = self.sr.get()
      g = self.sg.get()
      b = self.sb.get()
      print 'r = %f, g = %f, r = %f' % (r,g,b)
      hr = '%.2x' % int(255*r)
      hg = '%.2x' % int(255*g)
      hb = '%.2x' % int(255*b)
      color = '#' + hr + hg + hb
      self.c.delete("box")
      self.c.create_rectangle(x-d,y-d,x+d,y+d,width=1,outline='black',
         fill=color,tags='box')

def main():
   top = Tk()
   show = ColorGUI(top)
   top.mainloop()

if __name__=='__main__': main()
