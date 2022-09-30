# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 13:34:12 2017

@author: cg14acu
"""

def digits(n):
    """
    The purpose of this function is to seperate the digits using integer division
    and add it to a list in order to calculate whether the number is happy or not.
    """
    if n==0: return [0] #the fuction will end when there are no more remainders
    seperation=[] #empty list to store the digits
    while n!=0: #value does not equal 0
        seperation.append(n%10) # appends the remainder to seperation list
        n//=10 # integer division to calculat the next digit
    return seperation #ends the function by returning all the digits of the number as a list of seperate entities


def happy_number(n):
    """
    the purpose of this function is to calculate whether or not a number is happy.
    we do this through the summation of each individual digit until we get a value of one.
    we store all the happy numbers in a dictionary
    
    """
    n_sequence={n:1} # a dictionary of all the tried happy numbers
    while n !=1: #loop continues while n does not equal to 1
        n=sum((x**2) for x in digits(n)) #defines n as the sum of the squares of the digit
        if n in n_sequence: return False# not equal to one and is therefore a sad number
        n_sequence[n]=1 # if n is in the dictionary of happy numbers then it is happy
    return True
        

    
upto=[x for x in xrange(1,10**7+1)if happy_number(x)] #list of all the happy numbers in the range we are testing
print upto # so we can check 
#calculates the total number of Happy Numbers we have found
length=len(upto)
print "total number of happy numbers:",length

outfile=open("Happy_Numbers.txt","w") # opens a file for us to write in
outfile.write("Happy Numbers\n") #title 
for h in [upto]:#for loop to write in all the calculated happy numbers
    outfile.write ("%-10s" %(h))#formatting the file to make it clear to understand
outfile.close()#closes the file

#####################################################################