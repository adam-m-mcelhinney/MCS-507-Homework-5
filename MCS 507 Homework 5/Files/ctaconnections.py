# L-22 MCS 507 Wed 17 Oct 2012 : ctaconnections.py

# This script creates a dictionary with keys (i,j)
# where i and j are stop ids, and values the
# corresponding trip head sign.

filename = 'CTA/stop_times.txt'
print 'opening', filename, '...'
file = open(filename,'r')
i = 0; prev_id = -1; prev_hd = ''
D = {}
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
print D, len(D)
