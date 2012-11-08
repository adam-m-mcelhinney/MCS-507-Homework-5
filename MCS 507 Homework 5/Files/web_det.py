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

def AskDimension():
   """
   form to enter the dimension
   """
   print """<form method = "post" 
                  action = "web_det.py">
   <p>
     Give dimension:
     <input type = "text" name = "dim"
            size = 4 value = 2>
     <input type = "submit">
   </p>
   </form>"""

def AskMatrix(n):
   """
   form to enter an n-by-n  matrix
   """
   print """<form method = "post"
                  action = "compute_det.py">"""
   print """The dimension:
      <input type = "text" name = "dim"
             size = 4 value = %d>""" % n
   print "<p>Enter matrix :</p>"
   print "<table>"
   for i in range(0,n):
      print "<tr>"
      for j in range(0,n):
         print """<td><input type = "text"
         name = %d,%d size = 4></td>""" % (i,j)
   print "</table>"
   print """<input type = "submit">"""
   print "</form>"

def main():
   """
   Web interface to compute a determinant.
   """
   PrintHeader("compute determinant")
   form = cgi.FieldStorage()
   if not form.has_key("dim"):
      AskDimension()
   else:
      n = int(form["dim"].value)
      AskMatrix(n)
   print "</body></html>\n"

main()
