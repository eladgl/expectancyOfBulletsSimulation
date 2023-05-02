# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 11:24:57 2023

@author: eladg
"""


"""
  
"""
class MachineError:
    """
    This class will allow us to create more generic simulations where we know 
    that the error is different then the ones stated at the story. 
    
    Attributes
    ----------
     __systematicErr : float
        systematic error all shots have
    __randomErr : float
        random error

    Methods
    -------
    getSystematicError : float
        Getter for systematicErr
    getRandomError : float
        Getter for ranErr
    """
    #constructor for MachineError
    def __init__(self, systematicErr, randomErr):
        """
        Constructor method for MachineError
        Parameters
        ----------
        systematicErr : float
            systematic error all shots have
        randomErr : float
            random error
        """
        self.__systematicErr = systematicErr
        self.__randomErr = randomErr
        
    def getSystematicError(self):
        """
        Getter for systematicErr. Returns float.
        """
        return self.__systematicErr
    
    def getRandomError(self):
        """
        Getter for sranErr. Returns float.
        """
        return self.__randomErr