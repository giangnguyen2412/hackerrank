#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    '''
    s is the amount of money
    p start
    d gap
    m lower bound
    '''

    game_num = 0
    current_price = p
    money = s

    while (money >= current_price):
        current_price = p - game_num*d
        if (current_price <= m):
            current_price = m

        money -= current_price
        game_num += 1

    return game_num
        
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
