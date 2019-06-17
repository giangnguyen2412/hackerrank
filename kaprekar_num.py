#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    ret_list = list()
    for value in range(p, q+1):
        value_str = str(value)
        value_len = len(value_str)

        value_sqr = value*value
        value_sqr_str = str(value_sqr)
        value_sqr_len = len(value_sqr_str)
        
        if ((int)(value_sqr/10**(value_len)) + \
            (int)(value_sqr%10**(value_len)) == value):
            ret_list.append(value)

    if (len(ret_list)):
        print(*ret_list, sep = ' ')
    else:
        print("INVALID RANGE")


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
