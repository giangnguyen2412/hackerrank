#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    ret_list = list()
    count_zeros = 0
    if (arr.count(arr[0]) == len(arr)):
        ret_list.append(len(arr))
        return ret_list

    while (arr.count(arr[0]) != len(arr)):
        count_zeros = arr.count(0)
        ret_list.append(len(arr) - count_zeros)
        for i in range(count_zeros):
            arr.remove(0)
        min_val = min(arr)
        arr = [arr[i] - min_val for i in range(len(arr))]

    return ret_list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
