# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 19:03:03 2016

@author: Clare Goodwin
"""

import numpy as np

def trap(x):
    return (1/(np.sqrt(2*np.pi)))*(np.exp(-0.5*x**2))
b1 = raw_input('What is your upper bound? ')
b = float(b1)
a1 = raw_input('What is your lower bound? ')
a = float(a1)
N = raw_input('What is your starting interval? ')
m = int(N)
k = 0.0
NEW=10
OLD=0.0
e=10**-7
num=0.0

while abs(NEW-OLD)>e:
    for i in range(m):
        h = (b-a)/m
        x = a+(i*h)
        y = trap(x)
        k = k+y
    y0=trap(a)
    yn=trap(b)  
    OLD=NEW
    NEW=h*(k+0.5*(y0+yn))
    num=num+1
    m=2*m
    if abs(NEW-OLD)<e:
        num=num+1
        print "Your answer:", NEW
        print "Number of iterations:", num