#!/bin/python3

import math
import os
import random
import re
import sys
import copy

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    arr_set = set(arr)
    arr_len = len(arr)
    count = 0

    #for counter, value in arr_enum:
        #print(counter, value)
    arr_enum = copy.deepcopy(list((enumerate(arr))))

    for i in range(arr_len):
        a_i = arr[i]
        a_j = a_i + d
        a_k = a_j + d
        if (a_j in arr and a_k in arr):
            a_j_idx = [m for m, x in arr_enum if x == a_j]
            a_k_idx = [n for n, x in arr_enum if x == a_k]

            count += len(a_j_idx)*len(a_k_idx)
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
