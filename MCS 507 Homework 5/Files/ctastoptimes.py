# L-22 MCS 507 Wed 17 Oct 2012 : ctastoptimes.py

# Scans the file stop_times.txt for all trips
# that contain a given stop id.

filename = 'CTA/stop_times.txt'
print 'opening', filename, '...'
file = open(filename,'r')
id = input('give a stop id : ')
i = 0; H = []
while True:
   d = file.readline()
   if d == '': break
   L = d.split(',')
   try:
      if int(L[3]) == id:
         if not L[5] in H:
            print 'adding', L[5]
            H.append(L[5])
   except:
      print 'skipping line', i
   i = i + 1
print H
