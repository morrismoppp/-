# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 22:33:00 2021

@author: M10817021
"""

def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    ans = nums[i] + nums[j]
                    if ans == target:
                        return i,j