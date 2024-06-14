#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:02:22 2024

@author: Sagar
"""

def find_target(nums, target):
    
    start = 0 
    end = len(nums) - 1
    
    while start <= end:
        
        mid = (start + end) // 2
        
        if nums[mid] > target:
            end = mid - 1
            
        elif nums[mid] < target:
            start = mid + 1
        
        else:
            return mid
    
    return start # could be end here as per my logic, as while loop wouldn't run when start > end

nums = [1,2,4,5,6]
target = 3
result = find_target(nums, target)
print(result)




[1,2,3,4,8,9,10,11]



target = 7


        