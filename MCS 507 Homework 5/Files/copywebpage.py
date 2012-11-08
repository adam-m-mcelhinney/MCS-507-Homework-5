# L-21 MCS 507 Mon 15 Oct 2012 : copywebpage.py

# Script to make a local copy of a web page.
# The function copypage does the same as
# urrlib.urlretrieve(url,file).

def copypage(url,file):
   """
   Given the URL for the web page,
   a copy of its contents is written to file.
   Both url and file are strings.
   """
   import urllib
   copyfile = open(file,'w')
   f = urllib.urlopen(url)
   while True:
      data = f.read(80)
      print data
      if data == '': break
      copyfile.write(data)
   f.close()
   copyfile.close()

def main():
   """
   Prompts the user for a web page,
   a file name, and then starts copying.
   """
   print 'making a local copy of a web page'
   page = raw_input('Give URL : ')
   name = raw_input('Give file name : ')
   copypage(page,name)

if __name__=="__main__": main()
