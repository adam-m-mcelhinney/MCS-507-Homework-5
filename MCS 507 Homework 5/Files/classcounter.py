# L-10 MCS 507 Wed 19 Sep 2012 : classcounter.py

# This file defines a class Counter.
# An object of this class can be used as a counter.
# We use this as a template to invert the control
# of the function Newton.

# We can use the code in this file as a module
# and import the class definition in an interactive session
# or into another Python program.
# Because of the last line, we can also run this file
# as $ python classcounter.py and execute the test program.

class Counter():
   """
   Our first class stores a counter.
   """
   def __init__(self,v=0):
      """
      Sets the counter to the value v.
      """
      self.count = v

   def __str__(self):
      """
      Returns the string representation.
      """
      return "counter is " + str(self.count)

   def __repr__(self):
      """
      Defines the representation. 
      """
      return self.__str__()
  
   def next(self):
      """
      Adds one to the counter.
      """
      self.count = self.count + 1

def test():
   """
   Performs a simple test.
   """
   c = Counter(3)
   print c
   c.next()
   print c

if __name__=="__main__": test()
