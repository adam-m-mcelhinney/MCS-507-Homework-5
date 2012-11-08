"""
HW 5, #2

Adjust webcrawler.py to search for a path between two
locations. The user is prompted for two URLs. Crawling stops if a
path has been found.

Done


"""

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

def crawler(url,k,V,end):
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
         #print loc
         u = urlunparse(('http',loc,'','','',''))
         print u
         if u==end:
             return 'Path found!'
         else:
             newV = crawler(u,k-1,newV,end)
      return newV

def main():
   """
   Prompts the user for a web page,
   and prints all URLs this page refers to.
   """
   print 'crawling the web ...'
   #page = raw_input('Give starting URL : ')
   #end = raw_input('Give ending URL : ')
   page='http://home.simula.no/~hpl/INF1100/install.html'
   end='http://www.enthought.com'
   #k = input('give maximal depth : ')
   k=1
   L = crawler(page,k,[],end)
   print 'reachable locations :', L
   print 'total #locations :', len(L)

if __name__=="__main__": main()



##def NewLocations(L,V):
##   """
##   Given the list L of new URLs and the
##   list of already visited locations,
##   returns the list of new locations,
##   locations not yet visited earlier.
##   """
##   from urlparse import urlparse
##   newL = []
##   for h in L:
##      p = urlparse(h)
##      loc = p[1]
##      if not loc in newL:
##         if not loc in V:
##            newL.append(loc)
##   return newL
##
##def crawler(url,k,V):
##   """
##   Returns the list V updated with the
##   list of locations reachable from the
##   given url using k steps.
##   """
##   from urlparse import urlunparse
##   L = HTTPlinks(url)
##   newL = NewLocations(L,V)
##   newV = V + newL
##   if k == 0:
##      return newV
##   else:
##      for loc in newL:
##         u = urlunparse(('http',loc,'','','',''))
##         newV = crawler(u,k-1,newV)
##      return newV
##
##def main():
##   """
##   Prompts the user for a web page,
##   and prints all URLs this page refers to.
##   """
##   print 'crawling the web ...'
##   page = raw_input('Give URL : ')
##   k = input('give maximal depth : ')
##   L = crawler(page,k,[])
##   print 'reachable locations :', L
##   print 'total #locations :', len(L)
##
##if __name__=="__main__": main()
