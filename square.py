# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 20:29:42 2015

@author: Pie
"""
from point import *

from edge import *

from face import *

from plotting import *

p1 = point(0,0,0)
p2 = point(2,0,0)
p3 = point(2,2,0)
p4 = point(0,2,0)

#print p1
#print p2
#print p3
#print p4

e1 = edge(p1,p2)
e2 = edge(p2,p3)
e3 = edge(p3,p4)
e4 = edge(p4,p1)

#print e1
#print e2
#print e3
#print e4

f0 = face()
f0.addedge(e1)
f0.addedge(e2)
f0.addedge(e3)
f0.addedge(e4)

print f0

plot = plotting()
plot.plot_face(f0)
