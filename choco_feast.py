#!/bin/python3

import math
import os
import random
import re
import sys

def wrapping(wrapper, m):
    choco_num = 0
    while(wrapper >= m):
        choco_num += wrapper//m
        wrapper = wrapper//m + wrapper%m

    return choco_num

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    wrapper = 0
    choco_num = 0
    money = n

    buy_choco = (money//c)
    wrapper = buy_choco
    
    choco_num += buy_choco + wrapping(wrapper, m)

    return int(choco_num)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
