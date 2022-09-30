# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 10:46:05 2016

Differentiation of an equation using Euler's method. 

@author:  Clare Goodwin (Student ID: 14139478)
"""

import numpy as np

def f(a):
    return a
    
x_start = float(0) 
x_finish = float(1)
y_start = float(1)
interval_input = raw_input('How many initial intervals?: ')
interval = int(interval_input)
#setting up the input varibles. Input this data myself as the only...
# information that would change is the number of intervals

ex = np.exp(1)
ynew = 0

while abs(ex-ynew)> (10e-7):
    h = (x_finish-x_start)/interval
    y_dash = f(y_start)
    x = x_start+h
    y = y_start+(y_dash*h)
    #setting up my variables for the for loop
    for i in range (interval):
        x = x+h
        y = y+(y*h)
        #computing the differentiation
        
    interval = interval*2
    ynew = y
    
print 'The number of intervals is: ', interval
print 'x = ', x
print 'y = ', y


    