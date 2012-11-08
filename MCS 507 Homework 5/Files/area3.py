# L-9 MCS 507 Mon 17 Sep 2012 : area3

# A rectangle is given by length and width,
# for a square we only need one argument
# to compute the area.
# This function prints the keys of the dictionary
# to show that the formal parameter given by the
# user is stored as a string and we can test it.

def area ( length , **width ):
   "returns area of rectangle"
   if len(width) == 0:          # square
      return length**2
   else:                     # rectangle              
      a = length
      if width.has_key('width'):
         a *= width['width']
         return a
      else:
         print 'Please provide width.'
         return -1

print 'area of square or rectangle'
L = input('give length : ')
W = input('give width (0 if square) : ')
if W == 0:
   a = area(L)
else:
   a = area(L,width=W)
print 'the area is', a
if W <> 0:
   print 'the next call fails...'
   a = area(L,h=W)
   print 'the returned value is', a
