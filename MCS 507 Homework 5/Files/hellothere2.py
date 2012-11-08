#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# L-3 MCS 507 Fri 31 Aug 2012 : hellothere2.py

# If the file hellothere2.py is executable
# -- do "chmod +x hellothere2.py" to set the permissions --
# then typing at the command prompt $
# $ ./hellothere2.py
# will call the interpreter located as defined by the
# first line of this script and run the script.
# If this does not work, do "which python" and replace
# the first line of this script with what "which python" returns.

print 'Welcome to our interactive Python script!'
name = raw_input('who is there ? ')
print 'How are you, ' + name + '?'
x = input('type some number : ')
t = type(x)
print '-> your number', x , ':', t
