# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 22:10:34 2021

@author: M10817021
"""

s=[0,1,2,3,4,5,6,7,8,9]
even=[]
odd=[]
for i in range(len(s)):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
ans = sum(odd)-sum(even)
      