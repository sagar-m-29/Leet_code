#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 20:08:25 2024

@author: Sagar
"""

# My ATTEMPT
def peak_finding(arr):
    start = 0
    end = len(arr) - 1

    while start <= end: 
        mid = (start + end) // 2

        if (arr[mid] - arr[mid - 1]) > 0 and (mid == len(arr) - 1 or (arr[mid] - arr[mid + 1])) > 0: # Confused about this part. What if peak is the 1st element or last element.
            return mid
        
        elif arr[mid + 1] - arr[mid] > 0: # If next element is bigger than current mid element, take 2nd half
            start = mid + 1
            
        elif arr[mid - 1] - arr[mid] > 0:
            end = mid - 1 # If previous element is bigger than 
            
    return -1

print(peak_finding([2, 5, 7, 9, 15, 23, 8, 6]))  
print(peak_finding([73, 42, 13, 5, -17, -324]))  
print(peak_finding([100, 42, 17, 3, 8, 92, 234])) 



        
    