# -*- coding: cp1252 -*-
"""
HW 5, #3

Modify ctastopname.py so the user is prompted for a string
instead of a number. The modified script prints all id’s and
corresponding names that have the given string as substring. Use
the in operator.

Done

"""


# This script reads the file stops.txt,
# prompts the user for a stop identification number,
# and searches the file for the corresponding name.

filename = 'C:/Documents and Settings/amcelhinney/My Documents/GitHub/MCS507HW/MCS 507 Homework 4/MCS-507-Homework-5/MCS 507 Homework 5/stops.txt'
print 'opening', filename, '...'
file = open(filename,'r')
#id = input('give a stop id : ')
stop=raw_input("Give some part of a stop name:")
i = 0; stopname = None
while True:
   d = file.readline()
   if d == '': break
   L = d.split(',')
   try:
      #if int(L[0]) == id:
       if stop in d:
       #if stop in L:
           #stopname = L[2]; break
           print L[1]+','+L[2]
           
   except:
       print 'skipping line', i
   i = i + 1

