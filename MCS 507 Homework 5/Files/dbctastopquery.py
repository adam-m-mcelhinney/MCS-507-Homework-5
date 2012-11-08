# L-23 MCS 507 Fri 19 Oct 2012 : dbctastopquery.py

# The script prompts the user for a stop id
# and queries the stops table of the CTA database.

import MySQLdb

def getStopName(c,id):
   """
   Given a cursor c to the CTA database,
   queries the stops table for the stop id.
   Returns None if the stop id has not been
   found, otherwise returns the stop name.
   """
   s = 'select name from stops'
   w = ' where id = %d' % id
   q = s + w
   r = c.execute(q) 
   if r == 0:
      return None
   else:
      t = c.fetchone()
      return t[0]

def main():
   """
   Connects to the database,
   prompts the user for a stop id
   and the queries the stops table.
   """
   L = MySQLdb.connect(db="CTA")
   c = L.cursor()
   id = input('give a stop id : ')
   n = getStopName(c,id)
   print id, 'has name', n

main()
