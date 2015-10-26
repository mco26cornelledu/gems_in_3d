# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 21:18:55 2015

@author: Pie
"""
#from point import *
from edge import *

class face(object):
    elist = None
    
    def __init__(self):
        self.elist=[]
    
    def __repr__(self):
        to_write = ""
        for e in self.elist:
            to_write = to_write + "\n" + str(e)
        return to_write  
    
    def addedge(self,newedge):
        self.elist.append(newedge)
        
    def getedge(self):
        return self.elist

#f0 = face()
#f0.addedge(edge(point(1,2,3),point(2,3,4)))
#f0.addedge(edge(point(4,5,6),point(7,8,9)))
#print f0