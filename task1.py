# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 15:04:15 2021

@author: 
"""
import math
import matplotlib.pyplot as plt
import numpy as np
import random

from scipy.signal import find_peaks

def function(p,q,t):
    e1=((p+q)**t)
    e2=e1*p*((p+q)*(p+q))
    e3=((p*e1+q)*(p*e1+q))
    res=e2/e3
    return res

numbers = range(1, 30)
m = float(21000000)
p = 0.0395
q = 0.556
s = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

      
t=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ss=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
st=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(1,30):
    s[i]=i
    st[i]=random.randint(25000,10000000)
    t[i]=m*function(p,q,i)
#print(t)

plt.plot(s, t)
plt.xlabel('Time in Years')
plt.ylabel('Adaption of eBook')
plt.title('Adoptions of eBooks!')
plt.show()
print('************------------------------****************')
print('  ')
print('  ')
print('  ')
print('Adoptions of eBooks for first five years!')
print('************------------------------****************')
print(t[:5])
print('  ')
print('  ')
print('  ')
print('************------------------------****************')
pt=max(t)
#peaks = find_peaks(t, height = 1, threshold = 1, distance = 1)
#height = peaks[1]['peak_heights'] #list of the heights of the peaks
indices = find_peaks(t)[0]
#print(indices)
print('************------------------------****************')
print('  ')
print('  ')
print('  ')
print('Predicted peak for eBook adoptions is {0} at the  year {1} '.format(pt,indices))
print('  ')
print('  ')
print('  ')
print('************------------------------****************')
b0=p*m
b1=q-p
b2=-(q/m)
for i in range(1,30):
    
    ss[i]=b0+b1*st[i]+b2*(st[i]*st[i])
    
plt.plot(s, ss)
plt.xlabel('Time in Years')
plt.ylabel('Sales of eBook')
plt.title('Sales of eBooks!')
plt.show()
pt=max(ss)
#print(pt)
print('************------------------------****************')
print('  ')
print('  ')
print('  ')
print('plot Adoptions of eBooks and Sales of eBooks differs based on the p,q and m and sales of eBook ')
print('  ')
print('  ')
print('  ')
print('************------------------------****************')
    