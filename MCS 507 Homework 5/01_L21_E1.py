"""
HW 5, #1

Write a script to download all .py files from
http://www.math.uic.edu/jan/mcs507/main.html

Done


"""
import os, HTMLParser, urllib
os.chdir("C:/Documents and Settings/amcelhinney/My Documents/GitHub/MCS507HW/MCS 507 Homework 4/MCS-507-Homework-5/MCS 507 Homework 5")

from copywebpage import  copypage
from tallytags import TagTally
from scanquotes import QuotedStrings
from scanhttplinks import *
from urllib import urlopen

url='http://homepages.math.uic.edu/~jan/mcs507/main.html'

# Turn it into a file-like object
e=urlopen(url)
# Get all quoted strings
r=QuotedStrings(e)

# Reduce it only to ones with .py
type='.py'
files=[]
url2=url

out="C:/Documents and Settings/amcelhinney/My Documents/GitHub/MCS507HW/MCS 507 Homework 4/MCS-507-Homework-5/MCS 507 Homework 5/Files/"

for i in range(len(r)):
    if type in r[i]:
        files.append(r[i])
        url2=url.replace('main.html',r[i])
        #print url2
        q=copypage(url2,out+r[i])

print str(len(files))+' files found!'



