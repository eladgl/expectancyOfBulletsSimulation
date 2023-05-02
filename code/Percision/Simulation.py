# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 11:54:55 2023

@author: eladg
"""
import Constants
import random
import math
import matplotlib.pyplot as plt
from BurstIter import BurstIter
import numpy as np

class Simulation:    
    """
    This class takes care of the simulation. It is initialized with a Machine
    object and then runs according to Monte Carlo Simulation method that runs a constant amount of
    times which is defined as a Constant in our Constants.py file and can be changed to improve accuracy.
    The overall result of the simulation is the expected number of shots that hit the target.
    
    ...
    
    Attributes
    ----------
     __target : Target
        Target object that holds dimensions of the target
    __err : MachineError
        MachineError object holds systematic and random errors regarding the simulation
    __Range : RangeIter
        RangeIter object, it is an iterator. used in running the simulation many times
    __Burst : BurstIter
        BurstIter object, it is an iterator. 
    
    Methods
    -------
    __isInTarget(x,y) : numpy.array of boolean
        Returns whether a shot hit the target or not. Basically it is a private 
        filter function for numpy arrays. Returns numpy.array of boolean values
    __beginSimulation(fire_range) : float
        Runs a monte carlo based simulation and returns the expected number of shots
        that have hit the target
    plotSimulation() : void
        plots two sort of graphs, the amount of graphs depend on how many elemnts 
        Range attribute has in its iterator. The graphs are mean hits vs burst length
        and percentage vs burst length. Each graph is for another element in the 
        Range iterator attribute that was supplied to the class.
    """    
    def __init__(self, target, err, Range, Burst):
        """
        Constructor for Simulation object
        
        Parameters
        ----------
        target : Target
            Target object that holds dimensions of the target
        err : MachineError
            MachineError object holds systematic and random errors regarding the 
            simulation
        Range : RangeIter
            RangeIter object, it is an iterator. used in running the simulation many times
        """
        self.__target = target
        self.__err = err
        #init machine
        self.__Range = Range
        self.__Burst = Burst
        self.__burst = 0
    
    #filter funtion for numpy arrays
    def __isInTarget(self, x, y):
        """
        Returns whether a shot hit the target or not. Basically it is a private 
        filter function for numpy arrays. Returns numpy.array of boolean values
        
        Parameters
        ----------
        x : numpy.array 
            This is the x-coordinates of a numpy vector
        y : numpy.array
            This is the y-coordinates of a numpy vector    
        """
        width = self.__target.getWidth()
        height = self.__target.getHeight()
        return (-width/2 <= x) & (x <= width/2) & (-height/2 <= y) & (y <= height/2)
    
    
    #running the simulation according to monte carlo simulation
    def __beginSimulation(self, fire_range):
        """
        Runs a monte carlo based simulation and returns the expected number of shots
        that have hit the target. Returns float value
        
        Parameters
        ----------
        fire_range : double
            Given distance from target dimensions are meters
        """
        
        iterations = Constants.NUMBER_OF_SIMULATIONS
        r = random.Random()
        #calculate CEP
        sysCEP = math.tan(self.__err.getSystematicError()) * fire_range
        ranCEP = math.tan(self.__err.getRandomError()) * fire_range
        #calculate std
        sysStd = sysCEP / Constants.CONSTANT_FOR_CEP_CALC
        ranStd = ranCEP / Constants.CONSTANT_FOR_CEP_CALC
        #Get AverageHit vector many times 
        AverageHitVectorX = np.array([r.gauss(0, sysStd) for x in range(iterations)])
        AverageHitVectorY = np.array([r.gauss(0, sysStd) for x in range(iterations)])
        #get first hit
        burst = self.__burst
        expectancy = 0
        first = 0 #this is for the first bullet to be returned
        for i in range(iterations): #run many iterations as the Monte Carlo simulation method states
            actualHitPointsX = np.array([r.gauss(AverageHitVectorX[i], ranStd) for x in range(burst)])
            actualHitPointsY = np.array([r.gauss(AverageHitVectorY[i], ranStd) for x in range(burst)])
            result = self.__isInTarget(actualHitPointsX, actualHitPointsY)
            count = np.sum(result) #count those who have hit the target
            firstBullet = result.tolist()
            try:
                first += firstBullet.index(True)
            except ValueError: #in case there is no true value
                first += burst #assume we got it in the end
            
            expectancy += count
            if i == iterations - 1: #print to console every once in a while
                print("Burst = " + str(burst) + " expectancy = " + str(expectancy/(iterations)))
        return (expectancy / (iterations), first/iterations)  #This is the mean of all expectancy that were got. closest to the real value
    
    
    #plot the simulation for a set of ranges and a set of bursts
    def plotSimulation(self):
        """
        plots two sort of graphs, the amount of graphs depend on how many elemnts 
        Range attribute has in its iterator. The graphs are mean hits vs burst length
        and percentage vs burst length. Each graph is for another element in the 
        Range iterator attribute that was supplied to the class. Returns void
        """
        #burst_arr = list(range(10,201,10))    #Create a list of burst lengths that we will simulate their shooting
        mean_hits = [0] * len(self.__Burst)    #Initialization of the expectancy of how many shots did hit
        probability = [0] * len(self.__Burst)
        first_bullet = [0] * len(self.__Burst)
        #Init plotting
        fig, axs = plt.subplots(len(self.__Range), 1, figsize=(8, 5*len(self.__Range))) 
        fig2, axs2 = plt.subplots(len(self.__Range), 1, figsize=(8, 5*len(self.__Range))) 
        fig3, axs3 = plt.subplots(len(self.__Range), 1, figsize=(8, 5*len(self.__Range))) 
        
        for idx, fire_range in enumerate(self.__Range): #burst length increments
            print("Fire range changed to " + str(fire_range) + " km\n")
            bIter = BurstIter(self.__Burst.getBegin(),self.__Burst.getStop(),self.__Burst.getInterval())
            for k,burst in enumerate(bIter):            #increase range from target
                self.__burst = burst
                result = self.__beginSimulation(fire_range)    #find expectancy and first bullet
                mean_hits[k] = result[0]
                first_bullet[k] = result[1]
                probability[k] = mean_hits[k] / burst
                
            try:
                axs[idx].plot(self.__Burst.getList(), mean_hits)
                axs[idx].set_title("Meaan Hits For Fire Range: " + str(fire_range) + " meters")
                axs[idx].set_xlabel("Burst Length")
                axs[idx].set_ylabel("Mean Hits")
            
                axs2[idx].plot(self.__Burst.getList(), probability)
                axs2[idx].set_title("Probability For Fire Range: " + str(fire_range) + " meters")
                axs2[idx].set_xlabel("Burst Length")
                axs2[idx].set_ylabel("Probability")
                
                axs3[idx].bar(self.__Burst.getList(), first_bullet)
                axs3[idx].set_title("First Bullet that hit the target at range = : " + str(fire_range) + " meters")
                axs3[idx].set_xlabel("Burst Length")
                axs3[idx].set_ylabel("First bullet in to hit")
            except TypeError:  #use an except because if self.__Range had only 1 element in it, axs will not be subscriptable
                axs.plot(self.__Burst.getList(), mean_hits)
                axs.set_title("Meaan Hits For Fire Range: " + str(fire_range) + " meters")
                axs.set_xlabel("Burst Length")
                axs.set_ylabel("Mean Hits")
            
                axs2.plot(self.__Burst.getList(), probability)
                axs2.set_title("Probability For Fire Range: " + str(fire_range) + " meters")
                axs2.set_xlabel("Burst Length")
                axs2.set_ylabel("Probability")
                
                axs3.bar(self.__Burst.getList(), first_bullet)
                axs3.set_title("First Bullet that hit the target at range = : " + str(fire_range) + " meters")
                axs3.set_xlabel("Burst Length")
                axs3.set_ylabel("First bullet to hit")
        
        plt.tight_layout()
        plt.show()
        
        fig2.tight_layout()
        plt.show()
  
    
        
    
   
        