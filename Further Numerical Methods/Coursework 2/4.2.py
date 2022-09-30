# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 14:31:04 2018

@author: cg14acu
"""

import numpy as np
import matplotlib.pyplot as plt
a=0.5
fprime=np.cos(a)

loghs=[]
logerrs=[]
logerrsrich2=[]
logerrsrich3=[]

for logh in np.arange(-1,-17,-0.1):
    loghs.append(logh)
    h=10.**logh
    fprimehat=(np.sin(a+h)-np.sin(a))/h
    fprimehatrich2=(4.*np.sin(a+h/2.)-3.*np.sin(a)-np.sin(a+h))/h
    fprimehatrich3=(32.*np.sin(a+h/4.)-21.*np.sin(a)-12.*np.sin(a+h/2)+np.sin(a+h))/(3*h)
    
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

    