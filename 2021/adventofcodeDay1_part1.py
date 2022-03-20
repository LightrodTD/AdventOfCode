#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 00:38:43 2021

@author: m3hd1.syed
"""

#Read and open file
with open('adventofcodeDay1_part1input.txt') as f:
    lines = f.readlines()

#Put numbers in list as integers
list_of_lines = []
for line in lines:
    list_of_lines.append(int(line[:-1]))
 
#Increase, decrease, and same number counter    
increaseCounter = 0
decreaseCounter = 0
sameCounter = 0

for i in range(1,len(list_of_lines)):
    if list_of_lines[i] > list_of_lines[i-1]:
        increaseCounter += 1
    elif list_of_lines[i] < list_of_lines[i-1]:
        decreaseCounter += 1
    elif list_of_lines[i] == list_of_lines[i-1]:
        sameCounter += 1
        
print(increaseCounter, decreaseCounter, sameCounter)

print(lines)