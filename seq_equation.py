#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    ret = list()
    arr_len = len(p)
    for i in range(1, arr_len+1):
        outter_index = p.index(i) + 1
        inner_index = p.index(outter_index) + 1
        ret.append(inner_index)

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
