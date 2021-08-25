# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 22:18:25 2021

@author: M10817021
"""

import numpy as np
s = [77,5,5,22,13,55,97,4,796,1,0,9]
ans = []

while(1):
    a = np.min(s)
    ar = np.argmin(s)
    ans.append(a)
    s.pop(ar)
    if s==[]:
        break
    