#!/bin/python3

import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    pairs=0
    ar=sorted(ar)
    for some_val in range(0,n-1):
        if ar[some_val]==ar[some_val+1]:
            if ar[some_val+1]!=ar[some_val-1]:
                pairs+=1
            elif ar[some_val+1]==ar[some_val-2]:
                if ar[some_val+1]!=ar[some_val-3]:
                    pairs+=1
    return pairs
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
