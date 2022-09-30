# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 19:04:04 2016

Using the Monte Carlo simulation 100,000 times to calculate the probabilities 
of different outcomes of the playoffs such as:
    - the chances of the green boots to win the playoffs.
    - the probability of the playoff concluding after 4, 5, 6, or 7 matches.
    
@author: Clare Goodwin (14139478)
"""

import random

green = [0,0,0,0]
blue = [0,0,0,0]
subtotal = [0,0,0,0]
# creating for lists to track the number of times each team wins the playoffs
# after 4, 5, 6, and 7 games in total and subtotal to track the number of 
# times the playoffs is won by a team after 4, 5, 6, or 7 games.

alloutcomes = 0
# setting up all outcomes to use to sum all the possibilities of considered 
# eventualities. Should total to 100 at the end of the program.

bootswin = 0
faceswin = 0

# setting up the variables to track the total probability of either team 
# winning the playoffs.

for i in range (int(10e4)):
    green_boots = 0
    blue_faces = 0
    # tracking the number of times out of the run games either team wins.
    total = 0 
    while green_boots<4 and blue_faces<4: # while both green boots and blue 
    # faces have won less than 4 games. 
        rand = 1+random.randrange(100)
        # generating a random number between 0 and 100 so that each number has
        # a 1% chance of being produced and therefore can be used to 
        total = total+1
        if rand<=55: # <=55 to reflect the 55% chance of the grren boots 
        # winning the playoffs
            green_boots = green_boots +1
            # adding one to the count of how many times the green boots have 
            # won games
        else:
            blue_faces = blue_faces+1
             # adding one to the count of how many times the blue faces have 
             # won games. This is the only alternative as each game can only 
             # end in a win for one team, no draws are allowed
    total = total - 4 #setting total back to 0.
    if blue_faces == 4:
        blue[total]=blue[total]+1
    # adding a playoff win to the blue faces once they have won 4 games.
    else: 
        green[total]=green[total]+1
    # adding a playoff win to the green boots once they have won 4 games.

for i in range(4):
    alloutcomes = alloutcomes+green[i]+blue[i]
    # summing the outcomes of each team winning after 4, 5, 6, or 7 games.
    green[i] = 100*green[i]/float(10e4)
    blue[i] = 100*blue[i]/float(10e4)
    # turning the amount of games each team have won into a percentage of the
    #total games played.
    bootswin = bootswin+green[i]
    faceswin = faceswin+blue[i]
    #  summing the chances of either team winning after 4, 5, 6 or 7 games to 
    # get the total chance of either team winning the plyoffs overall.
    subtotal[i] = green[i]+blue[i]
    # summing the percentage chance of either team winning after 4, 5, 6 or 7 
    # games to get the percentage chance the ployoffs will end after any of 
    # these games.
alloutcomes = alloutcomes*100/float(10e4) 
# turning all outcomes into a percentage. Should total 100% to show my 
# calculations are correct and I have not missed any possible outcomes.
    
print "Percentage chance of the Green Boots winning the playoffs: ", bootswin
print "Percentage change of the playoffs ending after 4, 5, 6, and 7 games respectively: ", subtotal
#printing the required results from the question