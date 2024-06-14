#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 15:39:31 2024

@author: Sagar
"""

#Struggling here

def threeSum(nums):
    
    empty_array = []
    
    for i in range(len(nums)):
        for j in range(len(nums)-2):
            if nums[i] + nums[j+1] + nums[j+2] == 0 and nums[i] != nums[j+1] != nums[j+2]:
                empty_array.append([nums[i], nums[j+1], nums[j+2]])
                
    return empty_array

nums = [-1,0,2,1,-1,4]
threeSum(nums)

#######

# def threeSum(nums):
    
#     diction={}
    
#     for i in range(len(nums)):
#         if nums[i] = nums[i+1] + nums[i+2]:
#             return diction[nums[i]] = i

                
#     return empty_array

# nums = [-1,0,2,1,-1,4]
# threeSum(nums)

#######

def twoSum(nums, target):
    
    dictionary = {}
    
    for i in range(len(nums)):
        checker = target - nums[i]
        if checker in dictionary:
            return [dictionary[checker], i]
        else:
            dictionary[nums[i]] = i
      
        
nums = [2,4,3]
target = 6

twoSum(nums,target)


            
        