# L-15 MCS 507 Mon 1 Oct 2012 : linearregression.py

# Taken from the documentation of Matplotlib.

from pylab import *
x = arange(0.0,2.0,0.05)
noise = 0.3*randn(len(x))
y = 2 + 3*x + noise
m,b = polyfit(x,y,1)
figure()
plot(x,y,'bo',x,m*x+b,'-k',linewidth=2)
show()
