# -*- coding: utf-8 -*-
"""
A program to calulate the integral of the normalised and centralised normal
distrabution using the trapezium rule between bounds submitted by the user.

@author: Clare Goodwin (Student ID: 14139478)
"""

import numpy as np

def f(x):
    return (1/(np.sqrt(2*np.pi)))*(np.exp(-0.5*x**2)) 
    #defined the function to be integrated
b = float(raw_input('What is your upper bound? ')) 
a = float(raw_input('What is your lower bound? '))
#'b' and 'a' must both be floats so I set up for the raw data to be... 
# ...changed to this data type
N = 10 
#number of intervals
NEW = 10 
#'NEW' set up to store the new answer to each integral
OLD = 0 
#'OLD' set up to be used to store the answer for the previous integral.
#used random numbers for the initial values of 'NEW' and 'OLD' that...
#... satisfy the while condition so that my loop will run
steps = 1 
#used to count the number of times the integral has been calculated

while abs(NEW -OLD)> 10e-7:
    k = 0.0
    h = (b-a)/N 
    for i in range(1,N): 
        #range of 1 to n so that y0 and yn are left out of for special ...
        #...treatment
        x = a+(i*h)
        y = f(x)
        k = k+y
    y0 = f(a)
    yn = f(b)  
    OLD = NEW #used to change the variable being stored under 'NEW' to be...
    #...stored under 'OLD' so that it is not overwritten in the next step
    NEW = h*(k+0.5*(y0+yn))
    steps = steps+1 
    #sum the number of steps taken thus for in the integral
    N = 2*N 
    #doubling the number of intervals being used to make the integration...
    # ...more accurate
 
print "Your answer is:", NEW
print "Number of steps taken:", steps
print "Number of intervals required:",N