# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 17:50:05 2016

A program to read in the data of a CSV file and organise into three text files
containing:
- a table with the information sorted by city name.
- a table containing the summed population of in England, Scotland, Wales and 
  Northern Ireland
- a table sorted by city name containing data on city name, alternative city 
  name, year granted, name of the city cathedral.

@author: Clare Goodwin (14139478)
"""
""" 
PART A: Creating a table containing the information from UK_cities_list 
organise alphabetically by city name.

"""

infile = open("UK_cities_list.csv","r")
#opening the file for reading.

city_stuff = [] 
# creating a list to import the information in to for easy sorting.

for line in infile:
    one_set = line.strip().split(";")
    city_stuff.append(one_set)
#splitting the data in each line by the specified split between pieces of 
# information i.e ';'
    
header = city_stuff.pop(0)
# seperating the header (the information in the 1st line) from the rest of the 
# text so its not mistaken as data and be used in the formatting of my table.
city_stuff.sort()
# organising the lines into alphabetical order 
infile.close()
#closing the file for reading
outfile = open("Sorted UK Cities.txt","w")
#creating a new text file for writing to put the first table in
t_header = tuple(header)
# change header into a tuple so it cannot be edited 
outfile.write("%-19s %-20s %-20s %-55s %-30s %-20s %-10s\n" %t_header)
#formatting the lines of data in to a table. Negative numbers set to left align

for one_set in city_stuff:
    t_set = tuple(one_set)
    outfile.write(" %-19s %-20s %-20s %-55s %-30s %-20s %10s\n"%t_set)
#
    
outfile.close()
#closing file for writing.

"""
PART B: Creating a table containing the total population of the mentioned 
cities aroud the UK, split into England, Wales, Scotland and Ireland.

"""
cities = open("Sorted UK Cities.txt", "r")
# opeining first table for reading.
populationE = 0
populationNI = 0
populationW = 0
populationS = 0
# setting up empty variables to calculate the sum of the population for each 
#region of the UK requested

for one_set in city_stuff:
    if one_set[5] == "England":
        populationE = populationE +int(one_set[-1])
    elif one_set[5] =="Northern Ireland":
        populationNI = populationNI + int(one_set[-1])
    elif one_set[5] == "Wales":
        populationW = populationW +int(one_set[-1])
    else:
        populationS = populationS +int(one_set[-1])
#using a for loop to sum the populations listed in the 5th row according to the 
# regions listed in the 4th row.
        
infile.close()

outfile = open("City Population.txt", "w")
#writing second table into a new text file.
outfile.write("Welsh Cities        English Cities     Scottish Cities     Northern Irish Cities \n")
# END OF LINE MOVED TO NEXT LINE FOR PRINTING REASONS
outfile.write("%15d %15d %15d %15d \n" % (populationW, populationE, populationS, 
                                                                              populationNI))
# formatting a table to contain the new population data

outfile.close()

""" 
Part C: Creating a table sorted by city name containing data on city name, 
alternative city name, year granted, name of the city cathedral.

"""
infile = open("Sorted UK Cities.txt", "r").readlines()
#opening the first table and setting the program to read an entire line from the file
Header = infile.pop(0)
# seperating the header from the rest of the text
Names = {}
#creating a new dictionary

for one_set in city_stuff:
    if one_set[0]==one_set[1]:
        Names[one_set[0]]=' '
    else:
        Names[one_set[0]]=one_set[1]
#importing the city name and alternative name data into the dictionary, making 
# sure for those places where the city name and its alternative are the same 
# they print a blank space.

sorted_dict=Names.keys()
sorted_dict.sort()
#sorting my dictionary.

cathedral = {}
#creating a new dictionary for the cathedral name

for one_set in city_stuff:
    if one_set[3]=='*not applicable*':
        cathedral[one_set[3]]=' '
    else:
        cathedral[one_set[3]]=one_set[3]
# setting it so the cathedrals without names show a blank space rather than 
# '*not applicable*'

other_dict=cathedral.keys()
other_dict.sort()
#sorting the new dictionary
outfile = open("City Summary.txt", "w")
outfile.write("City Name            Alternative Name     Year Granted         Cathedral Name       \n")

for one_set in city_stuff:
    out= one_set[0], Names[one_set[0]], one_set[2], cathedral[one_set[3]]
    t_out = tuple(out)
    
    outfile.write("%-20s %-20s %-20s %-20s \n" % (t_out))
# creating a table for the city name, alt name, year granted and cathedral name.
    
outfile.close()
#closing the file for writing

print 'Your tables have been created.'
#used as a marker to show the program has finished running