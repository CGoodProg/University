# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 00:37:50 2016

Differentation of a problem using the Heun method.

@author:  Clare Goodwin (Student ID: 14139478)
"""


import numpy as np

def f(a):
    return a
    
xstart = float(0)
xend = float(1)
ystart = float(1)

interval_input = raw_input('How many initial intervals?: ')
interval = int(interval_input)

ex = np.exp(1)
ynew = 0

while abs(ex-ynew)> (10e-7):
    
    
    h = (xend-xstart)/interval
    y_dash = f(ystart)
    x = xstart+h
    y = ystart
    
    for i in range (interval):
        x = x+h
        est_y = y+(f(y)*h)
        y = y+((h/2)*(f(y)+f(est_y)))
        #changes the integration from Euler to the Heun method
        
    interval = interval*2
    ynew = y
    #doubling the number of steps to make the value of ynew more accurate...
    #...each time the integration is carried out
    
print 'The number of intervals is: ', interval
print 'x = ', x
print 'y = ', y