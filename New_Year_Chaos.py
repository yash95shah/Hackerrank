#!/bin/python3

import math
import os
import random
import re
import sys

def minimumBribes(q):
    length = len(q)
    arra=[]
    temp=[]
    bribes = 0
    for k in range(1,length+1):
        arra.append([k])
    for j in range(0,length):
        val = arra[j] - q[j]
        if abs(val)>2:
            print ("Too chaotic")
        else:
            if arra[j] not in temp :
                temp.append(arra [j])
            if q[j]  not in temp:
                temp.append(q[j])
                bribes += 1
    return  bribes  
     
            
    

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
