# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 20:27:57 2021

@author: Joela

This script is the dice simulator. The user will "roll" the dice and will be 
asked if they wish to roll again
"""

# initialize
error = False

# Import modules
from random import randint

# Main
while True:
    try:
        if error == False:
            print('You rolled: ' + str(randint(1,6)))
            answer = input('Do you want to roll again? \nUser Response [y/n]: ')    #Get user input as 'y' or 'n'
        elif error == True:
            answer = input('User Response [y/n]: ')
        
        error = False    #Reset error flag
        
        #If user input not 'y' or 'n', raise an exception
        if answer.casefold() not in ('y', 'n'):
            raise ValueError()
    
        #If user input is 'n', break
        if 'n' in answer.casefold():
            break            
    except ValueError:
        error = True    #Set error flag
        print('Please use "Y" or "N" to respond')



