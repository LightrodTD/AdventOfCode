#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 00:57:51 2021

@author: m3hd1.syed
"""
#Read and open file
with open('adventofcodeDay1_part1input.txt') as f:
    lines = f.readlines()

#Put numbers in list as integers
list_of_lines = []
for line in lines:
    list_of_lines.append(int(line[:-1]))
 
   
#Determine the exact number of lines that use the 3-measurement system
#For every i(determined before), it will add a sum of i, i+1, i+2 to letterSums
letterSums = []
for i in range(len(list_of_lines)-2):    
    total = 0
    for j in range(3):
        total += list_of_lines[i+j]
    letterSums.append(total)

#Same as part 1; increase, decrease, and same counter
increaseCounter = 0
decreaseCounter = 0
sameCounter = 0

for k in range(1,len(letterSums)):
    if letterSums[k] > letterSums[k-1]:
        increaseCounter += 1
    elif letterSums[k] < letterSums[k-1]:
        decreaseCounter += 1
    elif letterSums[k] == letterSums[k-1]:
        sameCounter += 1
        
print(increaseCounter, decreaseCounter, sameCounter)