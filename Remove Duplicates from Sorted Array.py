#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 11:25:44 2024

@author: Sagar
"""

array = [1,1,1,2,2,3,3,3,3,4,4]

current_number = []

for i in range(len(array)-1):
    current = array[i+1]
    if array[i] != current:
        current_number.append(array[i])

#########

array = [1,1,1,2,2,3,3,3,3,4,4]

current_number_v2 = []

ran = False

for i in range(len(array)-1):
    current = array[-(i+2)]
    if array[-(i+1)] != current and not ran:
        current_number_v2.append(array[-i])
        ran = True
    
answer = current_number + current_number_v2

print(answer)

##########

## WHY DOES THIS TAKE SO LONG?
# array = [1,1,1,2,2,3,3,3,3,4,4]

# current_number_v2 = []

# while len(current_number_v2) <= 1:
#     for i in range(len(array)-1):
#         current = array[-(i+2)]
#         if array[-(i+1)] != current:
#             current_number_v2.append(array[-(i)])

# print(current_number_v2)

##########

### WHY DID THIS NOT WORK?
# array = [1,1,1,2,2,3,3,3,3,4,4]

# current_number_v2 = []

# for i in range(len(array)-1):
#     current = array[-(i+1)]
#     if array[-i] != current:
#         current_number.append(array[i])
#     if len(current_number_v2) <= 1:
#         break
    
# print(current_number_v2)






