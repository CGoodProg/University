# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 15:48:55 2016

@author: Clare Goodwin
"""
import numpy as np

def trap(x):
    return (1/(np.sqrt(2*np.pi)))*(np.exp(-0.5*x**2))
b1 = raw_input('What is your upper bound? ')
b = float(b1)
a1 = raw_input('What is your lower bound? ')
a = float(a1)
N = raw_input('How many intervals? ')
m = int(N)
h = (b-a)/m
k = 0.0

for i in range(1,m):
    x = a+(i*h)
    y = trap(x)
    k = k+y
y0=trap(a)
yn=trap(b)
ans=h*(k+0.5*(y0+yn))
print "Your answer:", ans