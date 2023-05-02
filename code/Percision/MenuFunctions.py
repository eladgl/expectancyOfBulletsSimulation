# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 12:21:59 2023

@author: eladg
"""
from MachineError import MachineError
from MyIter import MyIter
from RangeIter import RangeIter
from BurstIter import BurstIter
from Simulation import Simulation
from Target import Target
import Constants

class MenuFunctions:
    """
    This is an helper class. It holds different static method to be used
    in different calculations and building the other classes in the simulation 
    in an easier way.
    
    Attributes
    ----------
    
    menu : string
        A simple txt message to be prompted to the user. 
        
    Methods
    -------
    enterErrors : MachineError
        Asks user to enter errors. Returns MachineError object
    enterTry : int
        Checkes if the entered value is int, otherwise retun None
    enterRange : RangeIter
        Creates a range generator
    enterBurst : BurstIter
        Creates a burst generator
    enterTarget : Target
        Returns a new Target object
    CreateSiulation : Simulation
        Creates a simulation object from MachineError, Target, RangeIter, BurstIter 
        and returns it
    BuildIter : MyIter
        Creates a MyIter object and returns it
    """
    
    menu = ("Type 1 to edit errors in simulation\n"
        "Type 2 to edit target's dimension (default are 1m by 1 m)\n"
        "Type 3 to edit RangeIterator for the simulation\n"
        "Type 4 to edit BurstIterator for the simulation\n"
        "Type 5 to run simulation\n"
        "Type 6 to exit\n"
        "Your choice is: ")
    
    @staticmethod
    def enterErrors():
        """
        Asks user to enter errors. Returns MachineError object
        """
        try:
            sysErr = float(input("Please insert this experiment systematic error: "))
            ranErr = float(input("Please insert this experiment random error: "))
            if sysErr > 0 and ranErr > 0:
                return MachineError(sysErr * Constants.MILLI_CONSTANT, ranErr * Constants.MILLI_CONSTANT)
            else:
                print("Input Errors. They must be positive value\n")
        except ValueError or AttributeError:
            pass
    @staticmethod        
    def enterTry(msg):
        """
        Checkes if the entered value is int, otherwise retun None
        """
        try:
            return int(input(msg))
        except ValueError:
            pass
        return None   
    @staticmethod
    def enterRange():
        """
        Creates a range generator
        """
        minRange = MenuFunctions.enterTry("Plese input minimum range from target to begin plotting: ")
        maxRange = MenuFunctions.enterTry("Plese input maxmimum range from target to begin plotting: ")
        interval = MenuFunctions.enterTry("Please input intervals between experiments: ")
        rIter = MenuFunctions.BuildIter(minRange, maxRange, interval)
        return RangeIter(rIter.getBegin(), rIter.getStop(), rIter.getInterval())
    @staticmethod
    def enterBurst():
        """
        Creates a burst generator
        """
        minBurst = MenuFunctions.enterTry("Plese input minimum burst from target per simulation: ")
        maxBurst = MenuFunctions.enterTry("Plese input maxmimum burst from target per simulation: ")
        interval = MenuFunctions.enterTry("Please input intervals between bursts: ")
        bIter = MenuFunctions.BuildIter(minBurst, maxBurst, interval)
        return BurstIter(bIter.getBegin(), bIter.getStop(), bIter.getInterval())
    
    @staticmethod
    def enterTarget():
        """
        Returns a new Target object
        """
        try:
            width = float(input("Please insert the target's width: "))
            height = float(input("Please insert the target's height': "))
            if width> 0 and height > 0:
                return Target(height, width)
            else:
                print("Input Errors. They must be positive value\n")
        except ValueError:
            pass
        
        
    @staticmethod
    def BuildIter(begin, stop, interval):
        """
        Creates a simulation object from MachineError, Target, RangeIter, BurstIter 
        and returns it
        """
        helper = [begin, stop, interval]
        if None not in helper and stop > begin and interval < stop - begin:
            return MyIter(begin, stop, interval)
        if interval is None and stop is None:
            return MyIter(begin, None, None)
        elif interval is None:
            return MyIter(begin, stop, None)
        print("Wrong values were entered")
        
    @staticmethod
    def CreateSimulation(target, mErr, rIter, bIter):
        """
        Creates a MyIter object and returns it
        """
        return Simulation(target, mErr, rIter, bIter)
        
        