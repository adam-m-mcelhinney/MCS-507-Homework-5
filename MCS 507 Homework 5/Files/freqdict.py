# L-19 MCS 507 Wed 10 Oct 2012 : freqdict.py

# Make a frequency table of the words in a text file.
# Anything separated by spaces qualifies as a word.
# The script prompts the user for a file name
# and prints the dictionary with the frequency table.
# The keys in the dictionary are the words on file,
# the values count their occurrences.

name = raw_input('give a file name : ')
file = open(name,'r')
D = {}
while True:
   line = file.readline()
   if line == "": break
   words = line.split()
   for w in words:
      if D.has_key(w):
         D[w] = D[w] + 1
      else:
         D[w] = 1
print D
