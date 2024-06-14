#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 12:09:10 2024

@author: Sagar
"""

def isPalindrome(x):
    
    x=str(x)
    
    y = x[::-1]
    
    return x==y

    
    
x = 121
y = -121
print(isPalindrome(x))
print(isPalindrome(y))
