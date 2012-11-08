# L-26 MCS 507 Fri 26 Nov 2012 : classpoint.py

# We define a simple class to store coordinates of a point in the plane.
# The main program illustrates two instantiations.

class Point:
   """
   Stores a point in the plane.
   """
   def __init__(self,x=0,y=0):
      """
      Defines the coordinates.
      """
      self.x = x
      self.y = y

   def __str__(self):
      """
      Returns the string representation.
      """
      return '(' + str(self.x) \
                 + ',' \
                 + str(self.y) + ')'

   def __repr__(self):
      """
      Returns the representation.
      """
      return self.__str__()

def main():
   """
   Instantiates two points.
   """
   p = Point()
   print 'p =', p
   q = Point(3,4)
   print 'q =', q

if __name__=="__main__": main()
