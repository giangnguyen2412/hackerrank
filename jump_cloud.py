#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e = 100
    num_cloud = len(c)
    thunder = [i for i in range(num_cloud) if c[i] == 1]

    print(thunder)
    
    '''
    If start is thunder, decrease 2
    Decrease 2 more for the next while loop if start is thunder
    '''
    if (c[0] == 1):
        e = e - 4

    pos = (0+k)%num_cloud   # Jump from 1 first
    jump_times = 1  # First jump
    while(pos > 0):
        if (pos in thunder): # If lands to a thunder
            e = e - 2
        pos = (pos+k)%num_cloud # Jump
        print(pos)
        jump_times = jump_times + 1

    print(e-jump_times)

    return e-jump_times


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
