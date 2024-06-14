#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 11:29:56 2024

@author: Sagar
"""

# hint: K_HOURS = [1, 2, 3, 4, 5, .... X]
# arr = [5, 1, 3, 10]
# Koko loves to eat bananas. There are N piles of bananas, the i-th pile has piles[i] bananas. The guards have gone and will come back in H hours.
#
# Koko can decide her bananas-per-hour eating speed of K. Each hour, she chooses some pile of bananas, and eats K bananas from that pile.
# If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.
#
# Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.
#
# Return the minimum integer K such that she can eat all the bananas within H hours.

# O(nlog(n))

print(range(10))

# WHY DO WE NEED K?
def koko(bananas, H):
    start = 1
    end = max(bananas)
    
    while start <= end:
        mid = (start + end) // 2
        
        total_hours = 0
        
        for i in bananas:
            
            total_hours += -(-i // mid)
            
            if total_hours <= H:
                
                end = mid-1
                
            else: 
                
                start = mid + 1
                
    return start

arr = [5, 1, 3, 10]

x = koko(arr, 10)
print(x)

y = koko(arr, 20)
print(y)



