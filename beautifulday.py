#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    beauty_days = 0
    for i in range(i, j+1):
        subtractor = i
        reverse = 0
        while(i > 0):   # This loop is to find the reverse number
            last_digit = i%10
            reverse = reverse*10 + last_digit
            i = int(i/10)
        if((abs(subtractor - reverse))%k == 0):    # divisible
            beauty_days += 1 
    return beauty_days

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
