# L-9 MCS 507 Mon 17 Sep 2012 : area

# A rectangle is given by length and width,
# for a square we only need one argument
# to compute the area.

def area ( length , *width ):
   "returns area of rectangle"
   if len(width) == 0:          # square
      return length**2
   else:                     # rectangle              
      return length*width[0]

print 'area of square or rectangle'
L = input('give length : ')
W = input('give width : ')
if W == 0:
   a = area(L)
else:
   a = area(L,W)
print 'the area is', a
