# -*- coding: utf-8 -*-
"""
A program to open up a text file full of data, compute the average and 
standard deviation of the maximum and minimum data and then create a 
text file with a table including  the average and standard deviation of these 
temperatures by month.

Created by: Clare Goodwin (Student ID: 14139478)
"""

import numpy as np

heathrow = np.load('heathrow_data.npz') 
#this opens the file
Tmax = heathrow['tmax']
Tmin = heathrow['tmin']
Month = heathrow['month']
Year = heathrow['year']
#extracting each data set from the file and assigned it to a variable...
#...for easy use
lenmin = len(Tmin) 
#calculating the number of pieces of data in Tmin
lenmax = len(Tmax) 
#calculating the number of pieces of data in Tmax

k = 0
h = 0
j = 0
l = 0 
#setting variables to zero for use in my for loops
m = 1 
#to be used to clarify which month each result corresponds to, starting...
#...with 1 for January

y_bar = sum(Tmax)/lenmax 
#calculating the mean of the data for the max temperatures
print 'Average of max temperatures: ',y_bar

for item in Tmax:
    p = item-y_bar
    j = j+p**2
y_sd = (j/(lenmax-1))**0.5 
#calculating the SD of the data for the maximum temperatures in 'Tmax'
print 'Standard deviation of max temperatures: ', y_sd

x_bar = sum(Tmin)/lenmin 
 #calculating the mean of the data for the minimum temperatures
print 'Average of min temperatures: ',x_bar

for item in Tmin:
    h = item-x_bar
    l = l+h**2
x_sd = (l/(lenmin-1))**0.5
#calculating the mean of the data for the minimum temperatures
print 'Standard deviation of min temperatures: ', x_sd

min_av = []
min_sd = []
max_av = []
max_sd = []
#Setting up four arrays to store the results of my calculations
print " " 
#printing a space in the output to make the output easier to read

for i in range(1,13): 
    #range 1 to 13 so that 12 values of i are used; one for each month
    Min_Month = Tmin[Month==i] 
    #used boolean slicing to seperate he data into months for the...
    #...maximum temperatures
    Max_Month = Tmax[Month==i] 
    #used boolean slicing to seperate he data into months for the...
    #...maximum temperatures

    Average_Min_Month = (sum(Min_Month)/len(Min_Month))
    print 'Average minimum temperature for month',m,': ', Average_Min_Month 
    min_av.append(Average_Min_Month)
    #appending my array to add the new data to it
    
    Average_Max_Month = (sum(Max_Month)/len(Max_Month))
    print 'Average Maximum temperature for month',m,': ', Average_Max_Month
    max_av.append(Average_Max_Month)
    #the above is to calculate the average temperatures of Tmax...
    #...and Tmin for each month
    
    a = 0
    b = 0 
    c = 0
    d = 0 
    #variables set back to zero so that they do not carry over the...
    #...answers from the last value of i 
    for item in Min_Month:
        a = item-(Average_Min_Month)
        b = b+a**2
    SD_Min_Month = (b/len(Min_Month))**(0.5)
    print 'SD of the minimum temperature for month',m,': ', SD_Min_Month
    min_sd.append(SD_Min_Month)
    

    for item in Max_Month:
        c = item-(Average_Max_Month)
        d = d+c**2
    SD_Max_Month = (d/len(Max_Month))**(0.5) 
    print 'SD of the maximum temperature for month',m,': ',SD_Max_Month
    max_sd.append(SD_Max_Month)
    #the above is two for loops to calculate the standard deviation...
    #...Tmin and Tmax of each month respectively

    m = m+1 #used to move on the track from month to month for easier...
    #...reading of the output data
    
    print " " 
    #to create spaces between the data for each month when the program...
    #...is run for easier reading

Min_av = np.array(min_av)
Min_sd = np.array(min_sd)
Max_av = np.array(max_av)
Max_sd = np.array(max_sd)

outfile = open("Heathrow_data_output", "w")
#opening a new file to store my table in
outfile.write("Month  Minimum Average  Minimum SD  Max Average       Max SD\n")

for i in range(12):
    outfile.write(" %d       %10f    %10f    %10f    %10f \n" % (i+1, 
                                Min_av[i], Min_sd[i], Max_av[i], Max_sd[i]))
outfile.close()
#closing the file for writing so it can be reopened for reading and printed...
#... to check the table
inFile = open('Heathrow_data_output', 'r')
contents = inFile.read()
print(contents)