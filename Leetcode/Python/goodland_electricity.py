#!/bin/python3

import math
import os
import random
import re
import sys

#had to refer to hackerrank discussions
def pylons(k, arr):
    # Write your code here
    if len(arr) == 1:
        if arr[0] == 0:
            return -1
        else:
            return 1
    lastPlant, lastChosenPlant = -k, -2*k
    n = 0
    for s in range(len(arr)):
        if s - lastPlant > 2 * k:
            return -1
        if arr[s] == 1:
            if s - lastChosenPlant > 2*k:
                lastChosenPlant = lastPlant
                n += 1
            
            lastPlant = s
    return n
        
        
            
        

f = open('/Users/mtg-11/Documents/Competitive Programming/Leetcode/Python/ge.txt', 'r')
n, k = map(int, f.readline().split())


arr = list(map(int, f.readline().split()))

result = pylons(k, arr)
print(result)
