#!/usr/bin/python
import cgi

def PrintHeader(title):
   """
   writes title and header of page
   """
   print """Content-type: text/html

<html>
<head>
<title>%s</title>
</head> 
<body>""" % title

PrintHeader("MCS 507 Lec34: forms")

print """
<form method = "post"
 method = "show_process_form.py">
  <b>Enter a word:</b>
  <input type = "text" name = "word">
  <input type = "submit" value = "submit word">
</form>"""

form = cgi.FieldStorage()
if form.has_key("word"):
   print """<p>Your word is <em>%s</em></p>
   """ % form["word"].value

print "</body></html>\n"

