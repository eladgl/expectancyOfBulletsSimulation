# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 11:22:16 2023

@author: eladg
"""
from MyIter import MyIter

class BurstIter(MyIter):
    """
    A subclass of MyIter that inherits all of its behavior
    
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
    def __init__(self, begin,stop,interval):
        super().__init__(begin,stop,interval)