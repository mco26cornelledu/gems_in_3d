# -*- coding: utf-8 -*-
"""
Created on Wed Oct 07 21:18:10 2015

@author: Pie
"""

x=2
y=4
string = "Hi."
print x
z=range(0,5,1)
print z
for index in range(11,13,1):
    print index

class Bob(object):
    name = "Bob"
    age = 17
    
    def __init__(self,age=17):
        self.age=age
    
    def __repr__(self):
        return "Name is " + self.name + ". Age is " + str(self.age) + "."
b = Bob(69)
print b
print b.name
b.age = 45
print b.age
print b
c = Bob()
print c