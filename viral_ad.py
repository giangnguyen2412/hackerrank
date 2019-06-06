#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising1(n):
    acc = 0
    rec_num = 5
    for i in range(n):
        likes = int(rec_num/2)
        rec_num = likes*3
        acc += likes
    
    return acc

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
