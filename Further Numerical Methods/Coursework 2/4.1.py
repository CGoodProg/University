 -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
a=0.5
fprime=np.cos(a)

loghs=[]
logerrs=[]
logerrsrich2=[]

for logh in np.arange(-1,-17,-0.1):
    loghs.append(logh)
    h=10.**logh
    fprimehat=(np.sin(a+h)-np.sin(a))/h
    fprimehatrich2=(4.*np.sin(a+h/2.)-3*np.sin(a)-np.sin(a+h))/h
    
    relative_error=abs((fprimehat-fprime)/fprime)
    relative_error_rich2=abs((fprimehatrich2-fprime)/fprime)
    
    logerrs.append(np.log10(relative_error))
    logerrsrich2.append(np.log10(relative_error_rich2))
    
plt.plot(loghs,logerrs, color='blue')
plt.plot(loghs,logerrsrich2,color='red')
plt.xlabel('log(h)')
plt.ylabel('log(error)')
plt.show()

    