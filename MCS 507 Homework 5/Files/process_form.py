#!/usr/bin/python

# L-27 MCS 507 Mon 29 Oct 2012 : process_form.py

# This script is called when the user presses the submit button
# in the form show_form.html.

import cgi
form = cgi.FieldStorage()
print "Content-Type: text/plain\n"
try:
   w = form['word'].value
   s = 'your word is '
   s = s + '\"' + w + '\"'
   print s
except KeyError:
   print "please enter a word"
