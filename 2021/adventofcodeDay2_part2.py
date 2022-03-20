#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 14:13:33 2021

@author: m3hd1.syed
"""

#Read and open file
with open('adventofcodeDay2_part1input.txt') as f:
    lines = f.readlines()
    
#Put values in list as [direction, value]
linesList = []
for line in lines:
    linesList.append(line.split())
    
depth = 0
horizontal = 0
aim = 0

for i in range(len(linesList)):
    if linesList[i][0] == 'forward':
        horizontal += int(linesList[i][1])
        depth += int(linesList[i][1])*aim
        
    elif linesList[i][0] == 'up':
        aim -= int(linesList[i][1])
        
    elif linesList[i][0] == 'down':
        aim += int(linesList[i][1])
        
print('Final depth: ', depth)
print('Horizontal: ', horizontal)

print(horizontal * depth)