#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    if (n == 1):
        return 1
    fact_num = n*extraLongFactorials(n-1)
    return fact_num

if __name__ == '__main__':
    n = int(input())

    fact_num = extraLongFactorials(n)
    print(fact_num)
