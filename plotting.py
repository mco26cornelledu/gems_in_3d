# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 20:17:41 2015

@author: Pie
"""
import matplotlib.pyplot as p
from mpl_toolkits.mplot3d import Axes3D
from edge import *

class plotting(object):
    ax = None
    
    def plot_edge(self,e,color):
        p0 = e.getp0()
        p1 = e.getp1()
        
        x = [p0.getx(), p1.getx()]
        y = [p0.gety(), p1.gety()]
        z = [p0.getz(), p1.getz()]
       
        self.ax.plot(x,y,z,color)
     
    def plot_face(self,f):
        fig = p.figure()
        self.ax = fig.add_subplot(111,projection='3d')
        elist = f.getedge()
        for e in elist:
            self.plot_edge(e,'b')
        p.show()
        
