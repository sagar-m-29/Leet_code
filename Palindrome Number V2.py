#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 12:09:10 2024

@author: Sagar
"""

def isPalindrome(x):
    x = str(x)
    i, j = 0, len(x) - 1
    
    def isPalindrome_recursion(i, j):
        if i >= j:
            return True
        
        if x[i] != x[j]:
            return False
        
        else:
            return isPalindrome_recursion(i + 1, j - 1)

    
    return isPalindrome_recursion(i, j)

x = 1432341
print(isPalindrome(x))
