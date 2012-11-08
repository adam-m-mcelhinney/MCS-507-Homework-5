# L-22 MCS 507 Wed 17 Oct 2012 : ctaconnectstops.py

# This script is used to determine whether two stops
# lie on the same trip.

filename = 'CTA/stop_times.txt'

def stopdict(name):
   """
   Opens the file with given name.
   The file contains scheduled arrival
   and departure times for each stop
   on each trip.  On return is a dictionary
   with keys (i,j) and strings as values,
   where i and j are stop ids and the
   value is the empty string if i and j
   are not connected by a trip, otherwise
   D[(i,j)] contains the trip name.
   """
   print 'opening', name, '...'
   file = open(name,'r')
   i = 0; prev_id = -1; prev_hd = ''
   D = {}
   print 'loading a big file, be patient ...'
   while True:
      d = file.readline()
      if d == '': break
      L = d.split(',')
      try:
         id = int(L[3]); hd = L[5]
         if(prev_id == -1):
            prev_id = id; prev_hd = hd
         else:
            if(prev_hd == hd):
               D[(prev_id,id)] = hd     
            else:
               prev_id = id; prev_hd = hd
      except:
         print 'skipping line', i
      i = i + 1
   return D

def main():
   """
   Creates a dictionary from the file
   stop_times.txt and prompts the user
   for a start and end stop id.
   The result of the dictonary query
   tells whether the stops are connected.
   """
   D = stopdict(filename)
   print len(D), 'connections'
   i = input('give start stop id : ')
   j = input('  give end stop id : ')
   s = str(i) + ' and ' + str(j)
   if not D.has_key((i,j)):
      print s + ' are not connected'
   else:
      print s + ' are connected by ' + D[(i,j)]

if __name__=="__main__": main()
