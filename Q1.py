# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 21:31:25 2021

@author: M10817021
"""

class Transportation:
    def __init__(self):
        self.maxspeed = 100
        
    def info(self):
        print("label:",self.label)
        print("color:",self.color)
        print("maxspeed",self.maxspeed)

class car(Transportation):
    def __init__(self,label=None,color=None):
        super().__init__()
        self.label=label
        self.color=color
    
class motorcycle(Transportation):
    def __init__(self,label=None,color=None):
        super().__init__()
        self.label=label
        self.color=color


c = car('BMW','red')
m = motorcycle('sym','white')

