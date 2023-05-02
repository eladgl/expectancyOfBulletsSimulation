# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 11:15:21 2023

@author: eladg
"""

class Target:
    """
    Representative target object with height and width dimensions are meters
    
    Attributes
    ----------
    __height : float
        Target's height. Dimensions are meters
    __width : float
        Target's width. Dimensions are meters

    Methods
    -------
    getSystematicError : float
        Getter for systematicErr
    getRandomError : float
        Getter for ranErr
    """

    def __init__(self, height = 1, width = 1):
        """
        Constructor for Target object
        
        Parameters
        ----------
        height : float
            Target's height. Dimensions are meters. Default value is 1
        width : float
            Target's width. Dimensions are meters. Default value is 1
        """
        self.__height = height
        self.__width = width
    
    
    def getHeight(self):
        """
        Getter for height. Returns float.
        """
        return self.__height

    def getWidth(self):
        """
        Getter for width. Returns float.
        """
        return self.__width