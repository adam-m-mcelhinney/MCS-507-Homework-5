# L-12 MCS 507 Fri 21 Sep 2012 : classpointsdb.py

# This script refactors the code of storepoints.py into a class.

import anydbm

class Points():
   """
   Encapsulation of an anydbm object to store a
   collection of coordinates of points in the plane.
   """
   def __init__(self,name):
      """
      Attempts to open the database with the name.
      """
      try:
         self.db = anydbm.open(name,'c')
         print 'opening', name, 'succeeded'
      except:
         print 'opening', name, 'failed'
         self.db = None

   def __str__(self):
      """
      Shows the list of stored points.
      """
      K = self.db.keys()
      s = ""
      for k in K:
         s += '(' + k + ',' + self.db[k] + ')' 
      return s

   def add_point(self,s):
      """
      Adds the point in the string s
      encoded as x,y.
      """
      L = s.split(',')
      x = L[0]; y = L[1]
      print 'adding', x, y
      self.db[x] = y

   def value_of_point(self,s):
      """
      Returns the value of the point
      with key stored in the string s
      """
      if self.db.has_key(s):
         return self.db[s]
      else:
         return None

def test():
   """
   Tests the methods of the Points class.
   """
   p = Points("data")
   p.add_point("1,2")
   print str(p)
   print "the value of 1 is", p.value_of_point("1")

if __name__=="__main__": test()
