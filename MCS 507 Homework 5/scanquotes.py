# L-21 MCS 507 Mon 15 Oct 2012 : scanquotes.py

# Opens a file and returns all strings on file
# that are between the double quotes.

def UpdateQstrings(L,b,s):
   """
   L is a list of double quoted strings,
   b buffers a double quoted string, and
   s is the data string to be processed.
   Returns an update of (L,b).
   """
   nb = b
   for i in range(0,len(s)):
      if nb == '':
         if s[i] == '\"':
            nb = 'o' # 'o' is for 'opened'
      else:
         if s[i] != '\"':
            nb += s[i]
         else:       # do not store 'o'
            L.append(nb[1:len(nb)])
            nb = ''
   return (L,nb)

def QuotedStrings(file):
   """
   Given a file object, this function scans
   the file and returns a list of all strings
   on the file enclosed between double quotes.
   """
   L = []
   buffer = ''
   while True:
      d = file.read(80)
      if d == '': break
      (L,buffer) = UpdateQstrings(L,buffer,d)
   return L

def main():
   """
   Prompts the user for a file name and
   scans the file for double quoted strings.
   """
   print 'getting double quoted strings'
   name = raw_input('Give file name : ')
   file = open(name,'r')
   L = QuotedStrings(file)
   print L
   file.close()

if __name__=="__main__": main()
