# L-8 MCS 507 Fri 14 Sep 2012 : enumwords.py

# Given are three lists of letters.  We want to enumerate all 3-letter "words"
# where the k-th letter in the word is drawn from the k-th list.

A = ['b','c','d']; B = ['a','e','u']; C = ['d','p']

def enumwords(k,L,accu):
   """
   Prints all words of length len(L), accumulating in accu,
   choosing the k-th letter from the k-th list in L.
   In the first call, take 0 for k and "" for accu. 
   """
   if(k >= len(L)):
      print accu
   else:
      for i in xrange(len(L[k])):
         enumwords(k+1,L,accu+L[k][i])

enumwords(0,[A,B,C],"")
