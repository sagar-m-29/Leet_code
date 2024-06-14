#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 15:39:31 2024

@author: Sagar
"""

def twoSum(nums, target):
    
    dictionary = {}
    
    for i in range(len(nums)):
        checker = target - nums[i]
        if checker in dictionary:
            return [dictionary[checker], i]
        else:
            dictionary[nums[i]] = i
      
        
nums = [3,2,4]
target = 6

twoSum(nums,target)


            
        