#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    count = 0
    digit = n

    while (digit/10):
        modulo = digit%10
        if (modulo == 0):
            digit = digit/10
            continue
        
        if (n%modulo == 0):
            count += 1
        digit = (int)(digit/10)

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
