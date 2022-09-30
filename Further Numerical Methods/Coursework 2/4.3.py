# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 18:20:44 2018

@author: Clare Goodwin
"""

import numpy as np
import matplotlib.pyplot as plt
a=7
def f(x):
    return (x**6)*np.exp(x)

def fprimes(x):
    return ((6*x**5)+(x**6))*np.exp(x)

loghs=[]
logerrs=[]
logerrsrich2=[]
logerrsrich3=[]
fprime=fprimes(a)

for logh in np.arange(-1,-17,-0.1):
    loghs.append(logh)
    h=10.**logh
    fprimehat=(f(a+h)-f(a))/h
    fprimehatrich2=(4.*f(a+h/2.)-3.*f(a)-f(a+h))/h
    fprimehatrich3=(32.*f(a+h/4.)-21.*f(a)-12.*f(a+h/2)+f(a+h))/(3*h)
    
    relative_error=abs((fprimehat-fprime)/fprime)
    relative_error_rich2=abs((fprimehatrich2-fprime)/fprime)
    
    logerrs.append(np.log10(relative_error))
    logerrsrich2.append(np.log10(relative_error_rich2))
    
    relative_error_rich3=abs((fprimehatrich3-fprime)/fprime)
    logerrsrich3.append(np.log10(relative_error_rich3))
    

    
plt.plot(loghs,logerrs, color='blue')
plt.plot(loghs,logerrsrich2,color='red')
plt.plot(loghs,logerrsrich3,color='green')
plt.xlabel('log(h)')
plt.ylabel('log(error)')
plt.show()

    