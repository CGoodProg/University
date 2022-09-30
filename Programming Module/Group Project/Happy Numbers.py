# -*- coding: utf-8 -*-

"""
A Python Programme that tests all the numbers in a range to test if they are happy. 
It then creates a file of all the happy numbers. 
"""

##############################################################################

def happy(number):

    a=number%10
    b=((number-a)%100)/10
    c=((number-(a+b))%1000)/100
    d=((number-(a+b+c))%10000)/1000
    e=((number-(a+b+c+d))%100000)/10000
    f=((number-(a+b+c+d+e))%1000000)/100000
    g=((number-(a+b+c+d+e+f))%10000000)/1000000

    square=(a**2)+(b**2)+(c**2)+(d**2)+(e**2)+(f**2)+(g**2)
    return square

"""
The above function uses modulo to seperate the number into it's didgits and then 
sums the square of the digits.  
"""

##############################################################################

happy_set=[]
rnge=int(10e6)

for number in xrange(rnge):

    test=[]
    test.append(number)

    if number %1000==0:
        print number,'/10000000'

    while number!=1:
        number=happy(number)

        if number in happy_set: 
            for item in test:
              if item not in happy_set:
                  happy_set.append(item)
            break

        elif number in test:
            break

        else: 
            test.append(number)

    for item in test:
        if number==1 and item not in happy_set:
            happy_set.append(item)

                        
happy_set.sort()
print happy_set


length=len(happy_set)
length=length+1
print length


outfile=open("Happy_10e6.txt","w")

for item in happy_set:
    outfile.write(" %10d \n" %(item))

outfile.close()