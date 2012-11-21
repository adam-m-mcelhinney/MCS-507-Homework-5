# -*- coding: utf-8 -*-
"""
HW 5, #8

Compute 1/x for x = [−1,+1]. Compare the outcome with the
graph of 1/x. Can you improve the outcome?

Ask prof: 1/-1=-1. I dont understand what we are supposed to do. 
Why is graph the same for all obs?

"""
import matplotlib.pyplot as plt 


f=lambda x:1/float(x)
a=-1;b=1;n=10;x=a
h=(b-a)/float(n)
val=[]
x_axis=[]
for i in range(n+1):
    x_axis.append(x)
    val.append(f(x))
    print x, f(x)
    x=x+h

##plt.plot(x_axis,val)
##plt.show()
    
    

# now we use interval arithmetic
from sympy.mpmath import iv
print 'using 35 decimal places ...'
iv.dps = 35
iv_f = lambda x: 1/(iv.mpf(x))
a=-1;b=1;n=10;x=a
h=(b-a)/float(n)
x_axis=[]
val2=[]
for i in range(n+1):
    x_axis.append(x)
    #c=float(str(iv_f(x).mid).split()[0].replace('[','').replace(',',''))
    c=float(str(iv_f(x)).split()[0].replace('[','').replace(',',''))
    val2.append(c)
    print x, f(x)
    x=x+h

plt.plot(x_axis,val,'*',x_axis,val2,'^')
plt.show()


##iv_a = iv.mpf(str(a))
##iv_b = iv.mpf(str(b))
##iv_z = iv_f(iv_a)
##print iv_z
##iv_z = iv_f(iv_b)
##print iv_z
