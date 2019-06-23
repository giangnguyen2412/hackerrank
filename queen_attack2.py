#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    main_diagonal_obs = list()
    sub_diagonal_obs = list()
    col_obs = list()
    row_obs = list()

    for obs in obstacles:
        if (obs[0] == r_q):
            row_obs.append(obs[1])
            continue
        elif (obs[1] == c_q):
            col_obs.append(obs[0])
            continue
        elif ((obs[0] - r_q) == (obs[1] - c_q)):
            sub_diagonal_obs.append(obs[0])
            continue
        elif ((obs[0] + obs[1]) == (c_q + r_q)):
            main_diagonal_obs.append(obs[0])
            continue

    squares = 0
    len_row_obs = len(row_obs)
    if (len_row_obs):
        subtract_row_obs = [c_q - r_obs for r_obs in row_obs]
        pos = [sign_obs for sign_obs in subtract_row_obs if sign_obs > 0]
        neg = [sign_obs for sign_obs in subtract_row_obs if sign_obs < 0]
        if (len(pos)):
            min_pos = min(pos)
            left_pos = row_obs[subtract_row_obs.index(min_pos)]
        else:
            left_pos = 0 # If no obs on the left

        if (len(neg)):
            max_neg = max(neg)
            right_pos = row_obs[subtract_row_obs.index(max_neg)]
        else:
            right_pos = n + 1 # If no obs on the right

        if (left_pos == 0):
            squares += (r_q - 1) # no obs on the left
        else:
            squares += (r_q - left_pos - 1) # have at least 1 obs

        if (right_pos == n + 1):
            squares += (n - r_q)
        else:
            squares += (right_pos - r_q - 1)
    else:
        squares += n - 1 # No obs at all in the row
    print(squares)

    len_col_obs = len(col_obs)
    if (len_col_obs):
        subtract_col_obs = [r_q - c_obs for c_obs in col_obs]
        pos = [sign_obs for sign_obs in subtract_col_obs if sign_obs > 0]
        neg = [sign_obs for sign_obs in subtract_col_obs if sign_obs < 0]
        if (len(pos)):
            min_pos = min(pos)
            down_pos = col_obs[subtract_col_obs.index(min_pos)]
        else:
            down_pos = 0 # If no obs on the left

        if (len(neg)):
            max_neg = max(neg)
            up_pos = col_obs[subtract_col_obs.index(max_neg)]
        else:
            up_pos = n + 1 # If no obs on the right

        if (down_pos == 0):
            squares += (c_q - 1) # no obs on the left
        else:
            squares += (c_q - down_pos - 1) # have at least 1 obs

        if (up_pos == n + 1):
            squares += (n - c_q)
        else:
            squares += (up_pos - c_q - 1)
    else:
        squares += n - 1 # No obs at all in the row
    print(squares)

    len_sub_diagonal_obs = len(sub_diagonal_obs)
    if (len_sub_diagonal_obs):
        subtract_sub_diagonal_obs = [r_q - sd_obs for sd_obs in sub_diagonal_obs]
        pos = [sign_obs for sign_obs in subtract_sub_diagonal_obs if sign_obs > 0]
        neg = [sign_obs for sign_obs in subtract_sub_diagonal_obs if sign_obs < 0]
        if (len(pos)):
            min_pos = min(pos)
            left_pos = sub_diagonal_obs[subtract_sub_diagonal_obs.index(min_pos)]
        else:
            left_pos = 0 # If no obs on the left

        if (len(neg)):
            max_neg = max(neg)
            right_pos = sub_diagonal_obs[subtract_sub_diagonal_obs.index(max_neg)]
        else:
            right_pos = n + 1 # If no obs on the right

        if (left_pos == 0):
            #squares += (r_q - 1) # no obs on the left
            squares += min(r_q, c_q) - 1
        else:
            squares += (r_q - left_pos - 1) # have at least 1 obs

        if (right_pos == n + 1):
            #squares += (n - r_q)
            squares += n - max(r_q, c_q)  
        else:
            squares += (right_pos - r_q - 1)
    else:
        squares += min(r_q, c_q) - 1 + n - max(r_q, c_q)        
    print(squares)

    len_main_diagonal_obs = len(main_diagonal_obs)
    if (len_main_diagonal_obs):
        subtract_main_diagonal_obs = [r_q - md_obs for md_obs in main_diagonal_obs]
        pos = [sign_obs for sign_obs in subtract_main_diagonal_obs if sign_obs > 0]
        neg = [sign_obs for sign_obs in subtract_main_diagonal_obs if sign_obs < 0]
        if (len(pos)):
            min_pos = min(pos)
            down_pos = main_diagonal_obs[subtract_main_diagonal_obs.index(min_pos)]
        else:
            down_pos = 0 # If no obs on the left

        if (len(neg)):
            max_neg = max(neg)
            up_pos = main_diagonal_obs[subtract_main_diagonal_obs.index(max_neg)]
        else:
            up_pos = n + 1 # If no obs on the right

        if (down_pos == 0):
            #squares += (c_q - 1) # no obs on the left
            i = r_q - 1
            j = c_q + 1
            while (i <= n and j <= n and i > 0 and j > 0):
                squares += 1
                i -= 1
                j += 1 
        else:
            squares += (r_q - down_pos - 1) # have at least 1 obs

        if (up_pos == n + 1):
            #squares += (n - c_q)
            i = r_q + 1
            j = c_q - 1
            while (i <= n and j <= n and i > 0 and j > 0):
                squares += 1
                i += 1
                j -= 1 
        else:
            squares += (up_pos - r_q - 1)
    else:
        #squares += max(r_q, c_q) - 1 + n - max(r_q, c_q) # No obs at all in the row
        i = r_q + 1
        j = c_q - 1
        while (i <= n and j <= n and i > 0 and j > 0):
            squares += 1
            i += 1
            j -= 1 
        i = r_q - 1
        j = c_q + 1
        while (i <= n and j <= n and i > 0 and j > 0):
            squares += 1
            i -= 1
            j += 1 
    print(squares)

    print('row obs is {}'.format(row_obs))
    print('col obs is {}'.format(col_obs))
    print('sub_diagonal obs is {}'.format(sub_diagonal_obs))
    print('main_diagonal obs is {}'.format(main_diagonal_obs))
    return squares

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
