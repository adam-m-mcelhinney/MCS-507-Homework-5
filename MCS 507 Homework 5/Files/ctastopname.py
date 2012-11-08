# L-22 MCS 507 Wed 17 Oct 2012 : ctastopname.py

# This script reads the file stops.txt,
# prompts the user for a stop identification number,
# and searches the file for the corresponding name.

filename = 'CTA/stops.txt'
print 'opening', filename, '...'
file = open(filename,'r')
id = input('give a stop id : ')
i = 0; stopname = None
while True:
   d = file.readline()
   if d == '': break
   L = d.split(',')
   try:
      if int(L[0]) == id:
         stopname = L[2]; break
   except:
      print 'skipping line', i
   i = i + 1
print id, 'has name', stopname
