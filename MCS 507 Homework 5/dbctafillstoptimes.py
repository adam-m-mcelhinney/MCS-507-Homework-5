# L-23 MCS 507 Fri 19 Oct 2012 : dbctafillstoptimes.py

# This script reads the file stop_timess.txt,
# and inserts the data on the lines into the table stop_times
# of the database CTA.  We use the GTFS feed of Lecture 22.

filename = '../Lec22/CTA/stop_times.txt'

import MySQLdb

def InsertData(c,s):
   """
   Inserts the data in the comma separated
   string using the cursor c.
   """
   L = s.split(',')
   d = 'insert into stop_times values ('
   d = d + ('0,' if L[0] == '' else L[0] + ',')
   d = d + '\"' + L[1] + '\"' + ','
   d = d + '\"' + L[2] + '\"' + ','
   d = d + L[3] + ',' + L[4] + ','
   d = d + L[5] + ',' + L[6] + ','
   w = L[7]; L7 = w[0:len(w)-2] + ')'
   d = d + ('0)' if L[7] == '' else L7)
   # print d
   c.execute(d)

def main():
   """
   Opens the file with name 'filename',
   reads every line and insert the data
   into the table 'stops'.
   """
   L = MySQLdb.connect(db="CTA")
   c = L.cursor()
   print 'opening', filename, '...'
   file = open(filename,'r')
   # we skip the first line
   d = file.readline()
   while True:
      d = file.readline()
      if d == '': break
      InsertData(c,d)

main()
