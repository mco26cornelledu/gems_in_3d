# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 20:39:28 2015

@author: Pie
"""
from point import * 

class edge(object):
    p0 = None
    p1 = None
    
    def __init__(self,p0,p1):
        self.p0=p0
        self.p1=p1
    
    def __repr__(self):
        return str(self.p0) + "--" + str(self.p1)        
        
    def setp1(self,p1):
        self.p1=p1       
        
    def setp0(self,p0):
        self.p0=p0

#p0 = point()
#p1 = point(4,5,6)
#
#e0 = edge(p0,p1)
#print p0
#print p1
#print e0