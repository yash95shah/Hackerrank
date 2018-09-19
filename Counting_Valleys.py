#!/bin/python3

import math
import os
import random
import re
import sys
#Here the 'U' means upward direction and 'D' means downward direction
# Complete the countingValleys function below.
def countingValleys(n, s):
    levels=0
    valleys=0
    for k in range(0,n-1): 
        if s[k]=='U':
            levels+=1
        elif s[k]=='D':
            levels-=1
        if levels==0 and s[k]=='U':
            valleys+=1
    return valleys
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
