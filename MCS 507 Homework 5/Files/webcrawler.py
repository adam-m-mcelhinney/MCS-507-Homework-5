# L-21 MCS 507 Mon 15 Oct 2012 : webcrawler.py

# Prompts the user for a URL and the maximal
# depth of the recursion tree.
# Lists all locations of web servers that can
# reached starting from the user given URL.

from scanquotes import UpdateQstrings
from scanhttplinks import HTTPfilter, HTTPlinks

def NewLocations(L,V):
   """
   Given the list L of new URLs and the
   list of already visited locations,
   returns the list of new locations,
   locations not yet visited earlier.
   """
   from urlparse import urlparse
   newL = []
   for h in L:
      p = urlparse(h)
      loc = p[1]
      if not loc in newL:
         if not loc in V:
            newL.append(loc)
   return newL

def crawler(url,k,V):
   """
   Returns the list V updated with the
   list of locations reachable from the
   given url using k steps.
   """
   from urlparse import urlunparse
   L = HTTPlinks(url)
   newL = NewLocations(L,V)
   newV = V + newL
   if k == 0:
      return newV
   else:
      for loc in newL:
         u = urlunparse(('http',loc,'','','',''))
         newV = crawler(u,k-1,newV)
      return newV

def main():
   """
   Prompts the user for a web page,
   and prints all URLs this page refers to.
   """
   print 'crawling the web ...'
   page = raw_input('Give URL : ')
   k = input('give maximal depth : ')
   L = crawler(page,k,[])
   print 'reachable locations :', L
   print 'total #locations :', len(L)

if __name__=="__main__": main()
