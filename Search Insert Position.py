#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:02:22 2024

@author: Sagar
"""

def find_target(nums, target):
    
    for i in range(len(nums)):
        
        if nums[i] == target:
            return i
        elif nums[i] >= target:
            return i
        elif target >= nums[i]:
            return len(nums)

nums = [2,3,5,6]
target = 8
result = find_target(nums, target)
print(result)


        








        