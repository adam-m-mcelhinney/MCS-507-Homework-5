# L-11 MCS 507 Fri 21 Sep 2012 : show_cmdlinargs.py

# This script simply prints the arguments entered at the command line.
# At the command prompt $, run this script for example as
# $ python show_cmdlinargs.py a 3.14
# and then the script will print all arguments, starting with the
# name of the script as argument 0.

import sys
L = sys.argv
print 'the list of arguments :'
print L
print 'number of arguments :', len(L)
for k in xrange(len(L)):
   print 'argument %d is %s' % (k,L[k])
