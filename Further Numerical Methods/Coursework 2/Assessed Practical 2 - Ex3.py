# -*- coding: utf-8 -*-
"""
Script to calculate the value of the derivative of the function (x^6)exp(x)
at the point x=7 using 3 different methods- forward difference, 2nd order
accurate richardson extrapolation and 3rd order accurate richardson 
extrapolation and produce a graph of their respective relative errors.

Clare Goodwin
14139478
"""

import numpy as np
import matplotlib.pyplot as plt
a=7
#the point at which we wish to find the derivative of the function
def f(x):
    return (x**6)*np.exp(x)
#defining the funtion f(x) to required function for use in equations

def fprimes(x):
    return ((6*x**5)+(x**6))*np.exp(x)
#defining funtion of actual differential of the function f(x)

loghs=[]
#empty list to iterate over and append with values of logh
logerrs=[]
#empty list to iterate over and append with the relative error of the forward 
#difference operator
logerrsrich2=[]
#empty list to iterate over and append with the relative error of the 2nd order 
#accurate richardson extrapolation 
logerrsrich3=[]
#empty list to iterate over and append with the relative error of the 3rd order 
#accurate richardson extrapolation 

fprime=fprimes(a)
#saving funtion of value of derivative of the function for later calculations

for logh in np.arange(-1,-17,-0.1):
    #iterating with step size 0.1
    loghs.append(logh)
    #adding current step value to list
    h=10.**logh
    #getting a linear value of h
    fprimehat=(f(a+h)-f(a))/h
    #using forward difference operator to calculate the derivative
    fprimehatrich2=(4.*f(a+h/2.)-3.*f(a)-f(a+h))/h
    #using 2nd order accurate richardson extrapolation to calculate the derivative
    fprimehatrich3=(32.*f(a+h/4.)-21.*f(a)-12.*f(a+h/2)+f(a+h))/(3*h)
    #using 3rd order accurate richardson extrapolation to calculate the derivative
    
    relative_error=abs((fprimehat-fprime)/fprime)
    #calculating relative error of forward difference operator
    relative_error_rich2=abs((fprimehatrich2-fprime)/fprime)
    #calculating relative error of 2nd order accurate richardson extrapolation
    
    logerrs.append(np.log10(relative_error))
    #adding log of the relative error for current step to the list 
    #(forward difference)
    logerrsrich2.append(np.log10(relative_error_rich2))
    #adding log of the relative error for current step to the list (2nd order
    #accurate richardson)
    
    relative_error_rich3=abs((fprimehatrich3-fprime)/fprime)
    #calculating relative error of 3rd order accurate richardson extrapolation
    logerrsrich3.append(np.log10(relative_error_rich3))
    #adding log of the relative error for current step to the list (3rd order 
    #accurate richardson
    

    
plt.plot(loghs,logerrs, color='blue')
#plot line of log h against the relative error for the forward differance 
#operator
plt.plot(loghs,logerrsrich2,color='red')
#plot line of log h against the relative error for the 2nd order accurate
#richardson extrapolation
plt.plot(loghs,logerrsrich3,color='green')
#plot line of log h against the relative error for the 3rd order accurate
#richardson extrapolation
plt.xlabel('log(h)')
plt.ylabel('log(error)')
plt.show()
#printing graph of relative error against log h for our 3 methods
    