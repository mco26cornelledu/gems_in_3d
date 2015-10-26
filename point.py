# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:31:59 2015

@author: Pie
"""

class point(object):
    x = 0
    y = 0
    z = 0
    
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z
        
    def __repr__(self):
        return "(%.2f,%.2f,%.2f)" %(self.x,self.y,self.z)
        
    
    def setx(self,x):
        self.x=x
        
    def sety(self,y):
        self.y=y
        
    def setz(self,z):
        self.z=z
        
        
    def setall(self,x,y,z):
        self.setx(x)
        self.sety(y)
        self.setz(z)
        
    def getx(self):
        return self.x
        
    def gety(self):
        return self.y
        
    def getz(self):
        return self.z
        
    def getall(self):
        return [self.getx(), self.gety(), self.getz()]
        
#p0 = point()
#p1 = point(3,4,5)
#print p0
#print p1
#p0.setx(43)
#print p0
#print p0.getx()
#vals = p0.getall()
#print vals