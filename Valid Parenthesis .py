#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 09:27:10 2024

@author: Sagar
"""

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

#Handle case where closing brakcet apperars before opening bracket

def isValid(s):
    empty_array = []
    dictionary = {"(":")", 
                  "{":"}", 
                  "[":"]"}
    
    for i in s:
        if i in dictionary.keys():
            empty_array.append(i)
        elif i in dictionary.values():
            if dictionary[empty_array[-1]] == i:
                empty_array.pop()
        else:
            return False
    
    return len(empty_array) == 0

print(isValid("{}[(])"))
print(isValid("{[()]}"))
print(isValid("({[]"))
