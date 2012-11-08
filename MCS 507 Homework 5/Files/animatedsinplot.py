# L-15 MCS 507 Mon 1 Oct 2012 : animatedsinplot.py

# We plot sin functions of increasing frequencies.

from scitools.std import *
x = arange(0,2*pi,0.01)
figure()
axis([0,2*pi,-1.5,+1.5])
for i in xrange(1,11):
   x = arange(0,1,0.01)
   y = sin(i*2*pi*x)
   plot(x,y,axis=[0,1,-1.5,+1.5],
        legend='frequency = %d' % i,
        savefig='/tmp/mov%02d.png' % i)
movie('/tmp/mov*.png')
