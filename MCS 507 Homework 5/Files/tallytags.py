# L-21 MCS 507 Mon 15 Oct 2012 : tallytags.py

# Illustration of HTMLParser to parse an html page.
# At the start of each tag, we print the attributes
# when the tag is 'a'.  The tally is updated each
# time we encounter the end of a tag.

from HTMLParser import HTMLParser
from urllib import urlopen

class TagTally(HTMLParser):
   """
   Shows attributes for 'a' tags
   and makes a tally of ending tags.
   """
   def __init__(self):
      """
      Initializes the dictionary of tags.
      """
      HTMLParser.__init__(self)
      self.TagTally = {}

   def handle_starttag(self, tag, attrs):
      """
      Looks for tags equal to 'a' and
      prints their attributes.
      """
      if tag == 'a':
         print "Attributes of tag : %s " % attrs

   def handle_endtag(self, tag):
      """
      Maintains a tally of the tags.
      """
      if self.TagTally.has_key(tag):
         self.TagTally[tag] = self.TagTally[tag] + 1
      else:
         self.TagTally.update({tag:1})

   def ShowTally(self):
      """
      Prints the tally to screen.
      """
      for each in self.TagTally:
         print each, ':', self.TagTally[each]

def main():
   """
   Opens a web page and parses it.
   """
   page = 'http://www.uic.edu'
   print 'opening %s ...' % page
   f = urlopen(page)
   p = TagTally()
   while True:
      data = f.read(80)
      if data == '': break
      p.feed(data)
   p.close()
   print 'the tally of tags :'
   p.ShowTally()

if __name__=="__main__": main()
