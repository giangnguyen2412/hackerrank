#!/bin/python3

import math
import os
import random
import re
import sys

def checkRedundance(redundance):
    if (redundance >= 0 and redundance%2 == 0):
        return 'Yes'
            
    return 'No'

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    if (s == t):
        return 'Yes'

    s_len = len(s)
    t_len = len(t)
    min_len = min(s_len, t_len)
    pos = -1 # The max index when s[:match_pos] = t[:match_pos]
    overlap_cnt = 0
    abs_len_diff = abs(s_len - t_len) # Abs diff len of 2 strings
    total_len = s_len + t_len # Total len of 2 strings

    for i in range(min_len):
        if (s[i] != t[i]):
            pos = i - 1
            break
        else:
            overlap_cnt = overlap_cnt + 1
    
    if(overlap_cnt == min_len):
        if (k >= abs_len_diff and k < total_len):
            if ((k - abs_len_diff)%2 == 0):
                return 'Yes'
            else:
                return 'No'

    if (k >= total_len):
        return 'Yes'

    if (pos == -1): # Two strings are different from the first character
        if (k < total_len): 
            return 'No'
    
    if (s_len < t_len):
        # pos + 1 convert idx to len
        redundance = k - 2*(s_len - (pos + 1)) - abs_len_diff

    if (s_len > t_len):
        redundance = k - (s_len - (pos + 1) + t_len - (pos + 1))

    if (s_len == t_len):
        redundance = k - 2*(s_len - (pos + 1))
        
    return checkRedundance(redundance)

    print("Sth wrong here! Redudant = {} with len_s is {} \
    and len_t is {}".format(redundance, s_len, t_len))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
