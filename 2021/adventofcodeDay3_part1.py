#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 14:37:41 2021

@author: m3hd1.syed
"""

#Read and open file
with open('adventofcodeDay3_part1input.txt') as f:
    lines = f.readlines()
    
#Put values in list as [direction, value]
linesList = []
for line in lines:
    linesList.append(list(line[:-1]))
    
#Gamma Rate 
gammaRate = []
for j in range(12):
    ones = 0
    zeroes = 0
    for i in range(len(linesList)):
        if linesList[i][j] == '0':
            zeroes += 1
        else:
            ones += 1        
    if zeroes > ones:
        gammaRate.append('0')
    else:
        gammaRate.append('1')

gammaNum = ''.join(gammaRate)
print('Therefore, the gamma rate is: ', gammaNum)

#Epsilon Rate
epsilonRate = []

for char in gammaRate:
    if char == '0':
        epsilonRate.append('1')
    else:
        epsilonRate.append('0')
epsilonNum = ''.join(epsilonRate)

print('Therefore, the epsilon rate is: ', epsilonNum)

#Power Conmuption Calculation
powerConsumption = (int(gammaNum,2))*(int(epsilonNum,2))
print('Therefore, the power consumption is: ', powerConsumption)