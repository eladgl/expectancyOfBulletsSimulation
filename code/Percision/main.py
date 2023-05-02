# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 11:58:30 2023

@author: eladg
"""
from MenuFunctions import MenuFunctions  
import Constants
from MachineError import MachineError
from RangeIter import RangeIter
from BurstIter import BurstIter
from Target import Target
import sys


def main():
    #define errors
    menu = MenuFunctions().menu
    #init
    mErr = MachineError(0.1 * Constants.MILLI_CONSTANT,0.2 * Constants.MILLI_CONSTANT)
    target = Target(1,1)
    rIter = RangeIter(1000,3001,1000)
    bIter = BurstIter(10,201,5)
    while(True):
        try:
            choice = int(input(menu))
        
            if choice == 1:
                mErr = MenuFunctions.enterErrors()
            elif choice == 2:
                target = MenuFunctions.enterTarget()
            elif choice == 3:
                rIter = MenuFunctions.enterRange()
            elif choice == 4:
                bIter = MenuFunctions.enterBurst()
            elif choice == 5:
                sim = MenuFunctions.CreateSimulation(target, mErr, rIter, bIter)
                sim.plotSimulation()
            elif choice == 6:
                sys.exit(0)
            else:
                 print("Choose only number from the list, 1-6")
        except ValueError:
            print("Only enter numbers")
        finally:
            print("\n")

if __name__ == '__main__':
    main()