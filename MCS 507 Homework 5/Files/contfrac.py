# L-20 MCS 507 Fri 12 Oct 2012 : showpaths.py

# Consider a real number x.  Let i be the integer part of x 
# and let f be the fractional part of x.
# If f is zero, then the continued fraction representation of x is [i].
# Otherwise, the continued fraction representation of x is [i,L],
# where L is the continued fraction representation of 1/f.

def cf(x,k,n):
   """
   Returns n convergents of a continued
   fraction representation of x, when
   called with k = 0, computed recursively.
   """
   from math import floor
   if k == n:
      return []
   else:
      i = int(floor(x))
      f = x - i
      if f == 0.0:
         return [i]
      else:
         L = cf(1.0/f,k+1,n)
         L.insert(0,i)
         return L

def cf2(x,n):
   """
   Returns n convergents of a continued
   fraction representation of x.
   """
   from math import floor
   L = []
   for k in range(0,n): 
      i = int(floor(x))
      f = x - i
      L.append(i)
      if f == 0.0: break
      x = 1.0/f
   return L

def dcf(L):
   """
   Returns the expansion of the convergents
   in the list L, as a float.
   """
   k = len(L)-1;
   r = L[k]
   while(k > 0):
      r = L[k-1] + 1.0/r
      k = k - 1
   return r

def rcf(L):
   """
   Returns the expansion of the convergents
   in the list L, as a Fraction.
   """
   import fractions
   k = len(L)-1;
   r = fractions.Fraction(L[k])
   while(k > 0):
      r = L[k-1] + 1/r
      k = k - 1
   return r

def test(x,n):
   """
   Tests the continued fraction representations for x.
   """
   x_cf = cf(x,0,n)
   x_cf2 = cf2(x,n)
   x_dcf = dcf(x_cf)
   x_rcf = rcf(x_cf)
   err = '%.2e' % abs(x-x_dcf)
   print len(x_cf), x_cf, x, x_dcf, err
   print len(x_cf2), x_cf2, x_cf == x_cf2
   print x_rcf, float(x_rcf), x_dcf

def main():
   """
   Shows the continued fractions
   for sqrt(2), e, and pi.
   """
   from math import sqrt, exp, pi
   print 'testing for sqrt(2)...'
   test(sqrt(2.0),20)
   print 'testing for exp(1)...'
   test(exp(1.0),20)
   print 'testing for pi...'
   test(pi,20)
   x = input('give x : ')
   n = input('give n : ')
   test(x,n)

main()
