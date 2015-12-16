#!/usr/bin/python

import math
from point import Point

class Line:
    '''Line class'''
    
    def __init__(self, start, end):
        '''Initialize Line'''
        self.start=start
        self.end=end

    def distance(self):
        '''Calculate distance between points'''
        return math.sqrt(
            (self.end.x - self.start.x)**2 +
            (self.end.y - self.start.y)**2)
