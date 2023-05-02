# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 16:39:20 2023

@author: eladg
"""

from MyIter import MyIter

class RangeIter(MyIter):
    """
    This is a Range iterator class which will allow us to maintain an
    easier iterating scheme in this task. It uses a composition of range 
    object
    
    Attributes
    ----------
    _range : range
        range object
    _iter : iter
        iter object

    Methods
    -------
    next : int
        Returns next number 
    hasNext() : boolean
        Returns if there is a next number
        
    __next__ : int
        <akes it subscriptable.
    __len__ : int
        Allows us to use len() on it.
    __iter__ : iter
        Returns us an iterator created from this object.
    """
    def __init__(self, begin,stop,interval): #constructor for Range, used in downcasting
        super().__init__(begin,stop,interval)