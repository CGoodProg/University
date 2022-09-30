# -*- coding: utf-8 -*-
"""
Script to calculate the value of the derivative of sin(x) at the point x=0.5 
using two different methods- forward difference and richardson extrapolation 
and produce a graph of their respective relative errors.

Clare Goodwin
14139478
"""
import numpy as np
import matplotlib.pyplot as plt
a=0.5
#the point at which we wish to find the value of sin as h decreases
fprime=np.cos(a)
#actual value of the differential of sin(a)

loghs=[]
#empty list to iterate over and append with values of logh
logerrs=[]
#empty list to iterate over and append with the relative error of the forward 
#difference operator 
logerrsrich2=[]
#empty list to iterate over and append with the relative error of the 2nd order 
#accurate richardson extrapolation 

for logh in np.arange(-1,-17,-0.1):
    #iterating with step size 0.1
    loghs.append(logh)
    #adding current step value to list
    h=10.**logh
    #setting h to desired step length for formula
    fprimehat=(np.sin(a+h)-np.sin(a))/h
#using forward difference operator to calculate the derivative
    fprimehatrich2=(4.*np.sin(a+h/2.)-3*np.sin(a)-np.sin(a+h))/h
#using 2nd order accurate richardson extrapolation to calculate the derivative
    
    relative_error=abs((fprimehat-fprime)/fprime)
    #calculating relative error of forward difference operator 
    relative_error_rich2=abs((fprimehatrich2-fprime)/fprime)
    #calculating relative error of 2nd order accurate richardson extrapolation
    
    logerrs.append(np.log10(relative_error))
    #adding log of the relative error for current step to the list 
    #(forward difference)
    logerrsrich2.append(np.log10(relative_error_rich2))
    #adding log of the relative error for current step to the list (richardson)
    
plt.plot(loghs,logerrs, color='blue')
#plot line of log h against the relative error for the forward differance 
#operator
plt.plot(loghs,logerrsrich2,color='red')
#plot line of log h against the relative error for the 2nd order accurate
#richardson extrapolation

plt.xlabel('log(h)')
plt.ylabel('log(error)')
plt.show()
#printing graph of relative error against log h for our 2 methods
    