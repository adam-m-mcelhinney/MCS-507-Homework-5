# L-12 MCS 507 Mon 24 Sep 2012 : guieval.py

# GUI to evaluate a user given function,
# using a class.

from Tkinter import *
from math import *

class EvalFun():
   """
   GUI to evaluate user given expressions.
   """
   def __init__(self,wdw):
      "Determines the layout of the GUI."
      wdw.title("Evaluate Expressions")
      self.L1 = Label(wdw,text="f(x) =")
      self.L1.grid(row=0)
      self.L2 = Label(wdw,text="x =")
      self.L2.grid(row=0,column=2)
      self.f = Entry(wdw)
      self.f.grid(row=0,column=1)
      self.e = Entry(wdw)
      self.e.grid(row=0,column=3)
      self.r = Entry(wdw)
      self.r.grid(row=0,column=5)
      self.b = Button(wdw,text="equals",
         command=self.calc)
      self.b.grid(row=0,column=4)

   def calc(self):
      "Evaluates the function f at x."
      self.r.delete(0,END)
      x = float(self.e.get())
      y = eval(self.f.get())
      self.r.insert(INSERT,y)

def main():
   top = Tk()
   eva = EvalFun(top)
   top.mainloop()

if __name__ == "__main__": main()
