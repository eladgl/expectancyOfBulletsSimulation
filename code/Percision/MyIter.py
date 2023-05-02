# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 11:22:56 2023

@author: eladg
"""

# -*- coding: utf-8 -*-

class MyIter:
    """
    This is a My iterator class which will allow us to maintain an
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
    getStop() : int
        Returns stop value of iterator
    getBegin() : int
        Returns begin value of iterator
    getInterval() : int
        REturns interval value of iterator
    getList() : list(int)
        Returns the iterator as list, converts from generator to list
    __next__ : int
        Makes it subscriptable.
    __len__ : int
        Allows us to use len() on it.
    __iter__ : iter
        Returns us an iterator created from this object.
    """
    def __init__(self, minNum, maxNum, interval):
        """
        Constructor of RangeIter allows us to create object similar to:
        range(x), range(x,y), range(x,y,z) where x,y,z > 0, y>= x, z < y-x and 
        they are all integers
        
        Parameters
        ----------
        minNum : int
            Minimum number the iterator starts at
        maxNum : int
            (Maximum number - 1) the iterator ends at, depends on interval too.
        interval : int
            Jumps between consecutive nexts in iterator
        """
        if interval is None and maxNum is None:
            self._range = range(1, minNum)      #interval here is 1
            self.__current = 1
            self.__begin = 1
            self.__maxNum = minNum
            self.__interval = 1
        elif interval is None:
            self._range = range(minNum, maxNum) #interval here is 1
            self.__current = minNum
            self.__begin = minNum
            self.__maxNum = maxNum
            self.__interval = 1
        else:
            self._range = range(minNum, maxNum, interval)
            self.__current = minNum
            self.__begin = minNum
            self.__maxNum = maxNum
            self.__interval = interval
                
        self._iter = iter(self._range)
    
    def __iter__(self):
        """
        Returns iter object
        """
        return self
    
    def __next__(self):
        """
        Returns next element, int.
        """
        return next(self._iter)
    
    def hasNext(self):
        """
        Finds if there is a next element.
        """
        if self.__current + self.__interval < self.__maxNum:
            return True
        return False
    
    def next(self):
        """
        Returns next element
        """
        if not self.hasNext():
            raise StopIteration
        
        self.__current = self.__next__()
        return self.__current 
    
    def __len__(self):
        """
        Returns size of iter object, Returns int value.
        """
        return len(self._range)
    def getCurrent(self):
        return self.__current
    def getBegin(self):
        """
        Return begin value of iterator. Returns int value.
        """
        return self.__begin
    
    def getStop(self):
        """
        Return stop value of iterator. Returns int value.
        """
        return self.__maxNum
    
    def getInterval(self):
        """
        Return interval value of iterator. Returns int value.
        """
        return self.__interval
    
    def getList(self):
        """
        Returns the iterator as list with all the values in it. return List(int) value
        """
        return list(self._range)