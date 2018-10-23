#!/bin/python3

import math
import os
import random
import re
import sys


def jumpingOnClouds(c):
    count = 0
    l= len(c)
    c.append(1)
    c.append(1)
   
    for k in range (0,l+2):
        if c[k] == 0:
            if c[k+2] == 0:
                count += 1
            elif c[k+1]== 0 and c[k-1] != 0:
                count += 1
        
    return count 
    
            
            
            
    return i
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
