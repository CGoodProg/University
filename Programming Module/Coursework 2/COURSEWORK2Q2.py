# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:40:33 2016

A program reading in the temperature data for Heathrow Airport from the required
data file and producing a scatter graph of the maximum and minimum temperature
data with a linear regression line.

@author: Clare Goodwin (14139478)
"""

import numpy as np
import matplotlib.pyplot as plt #shortening the code for pyplot as it is to be
#  used frequently.

infile = np.load('heathrow_data.npz')
#loading the file containing the data we want to make our table from.

Tmax = infile['tmax']
Tmin = infile['tmin']
# importing the necessary data from the file. 'year' and 'month' are ommitted
# as they are unnecessary for the table we want to create.

plt.figure(1) 
plt.plot(Tmax,Tmin,".") #setting what variables we want to plot and how we want
# the points to be displayed. In this case "." for dots.
plt.xlabel("Maximum Temperature") 
plt.ylabel("Minimum Temperature")
# labeling the x axis and y axis
plt.title("Linear Regression of Maximum and Minimum Temperatures")
#naming the graph
plt.axis([-5,35, -10, 25])
# setting the axis of my graph to stretch a resonable amount past the data limits
# for easy reading and to make it clear that all points are contained on the graph.
fit = np.polyfit(Tmax, Tmin, 1)
x_line = np.linspace(-3,32)
y_line = fit[0]*x_line+fit[1]
plt.plot(x_line,y_line)
# plotting the regression line and to my graph and fitting it to spread slightly
# outside of the bounds of the data but still within the graph

plt.show()
#showing the graph.