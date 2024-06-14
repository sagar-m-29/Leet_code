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

# My solution:
def isValid(s):
    
    dictionary = {"(":0,
                  ")":0,
                  "{":0,
                  "}":0,
                  "[":0,
                  "]":0}
    
    
    for i in s:
        if i in dictionary:
            dictionary[i] = dictionary[i] + 1

    for i in range(len(s)-1):
        if s[i] == ")" and dictionary[")"] > dictionary["("] or s[i] == "}" and dictionary["}"] > dictionary["{"] or i == "]" and dictionary["]"] > dictionary["["]:
            return False
        elif s[i] == "(" and s[i+1] == "]" or s[i+1] == "}":
            return False
        elif s[i] == "[" and s[i+1] == "}" or s[i+1] == ")":
            return False
        elif s[i] == "{" and s[i+1] == ")" or s[i+1] == "]":
            return False
        else:
            return True

    
string = "{}[(])"
string2 = "({[]"
    
print(isValid(string2))


# # My initial solution, why doesn't it work?
# def isValid(s):
    
#     dictionary = {"(":0,
#                   ")":0,
#                   "{":0,
#                   "}":0,
#                   "[":0,
#                   "]":0}
    
    
#     for i in s:
#         if i in dictionary:
#             dictionary[i] = dictionary[i] + 1

#     for i in s:
#         if i == ")" and dictionary[")"] > dictionary["("] or i == "}" and dictionary["}"] > dictionary["{"] or i == "]" and dictionary["]"] > dictionary["["]:
#             return False
#         elif i == "(" and i+1 == "]" or i+1 == "}":
#             return False
#         elif i == "[" and i+1 == "}" or i+1 == ")":
#             return False
#         elif i == "{" and i+1 == ")" or i+1 == "]":
#             return False
#         else:
#             return True
            

    
# string = "{}[(])"
    
# isValid(string)


    
    
