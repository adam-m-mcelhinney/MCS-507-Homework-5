# L-21 MCS 507 Mon 15 Oct 2012 : scanhttplinks.py

# Prompts the user for a URL, opens the page and
# shows the list of all double quoted strings
# which begin with http.

from scanquotes import UpdateQstrings

def HTTPfilter(L):
   """
   Returns from the list L only those strings
   which begin with http.
   """
   H = []
   for s in L:
      if len(s) > 4:
         if s[0:4] == 'http': H.append(s)
   return H

def HTTPlinks(url):
   """
   Given the URL for the web page,
   returns the list of all HTTP strings.
   """
   import urllib
   try:
      print 'opening ' + url + ' ...'
      f = urllib.urlopen(url)
   except:
      print 'opening ' + url + ' failed'
      return []
   L = []; b = ''
   while True:
      data = f.read(80)
      if data == '': break
      (L,b) = UpdateQstrings(L,b,data)
      L = HTTPfilter(L)
   f.close()
   return L

def ShowLocations(L):
   """
   Shows the locations of the URL in L.
   """
   from urlparse import urlparse
   for h in L:
      p = urlparse(h)
      print p[1]

def main():
   """
   Prompts the user for a web page,
   and prints all URLs this page refers to.
   """
   print 'listing reachable locations'
   page = raw_input('Give URL : ')
   L = HTTPlinks(page)
   print 'found %d HTTP links' % len(L)
   ShowLocations(L)

if __name__=="__main__": main()
