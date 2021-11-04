# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

##
# Random walk by https://www.codespeedy.com/random-walk-program-in-python/
#


import numpy as np
import matplotlib.pyplot as plt

trigger = False


def Randomwalk1D(n): #n here is the no. of steps that we require
   global trigger
   x = 0
   y = 0
   xposition = [0] #starting from origin (0,0)
   yposition = [0] 
   for i in range (1,n+1):
       step = np.random.uniform(0,1)
       if step < 0.5: # if step is less than 0.5 we move up    
           x += 1
           y += 1  #moving up in u direction
       if step > 0.5: # if step is greater than 0.5 we move down  
           x += 1
           y += -1 #moving down in y direction
 
       xposition.append(x)
       yposition.append(y)
       if(y < 0):
           trigger = True
   return [xposition,yposition]

triggercounter = 0

for i in range (1,10000):
    trigger = False
    Randwalk = Randomwalk1D(100) #creating an object for the Randomwalk1D class and passing value of n as 100
    if(trigger):
       triggercounter += 1
    #print(triggercounter)
    ## DONT PRINT 10.000 PLOT WITH 100 STEPS EACH
    #plt.plot(Randwalk[0],Randwalk[1],'r-', label = "Randwalk1D") # 'r-' makes the color of the path red
    #plt.title("1-D Random Walks")
    #plt.show()
    
solution = triggercounter/10000
print(1-solution)
