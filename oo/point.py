#!/usr/bin/python

#http://www.tutorialspoint.com/python/python_classes_objects.htm

class Point:
    '''demo class for point'''
    
    def __init__( self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destroyed"
   
    def display(self):
        print "x : ", self.x,  ", y: ", self.y

    def length(self):
        return (self.x+self.y)*2
