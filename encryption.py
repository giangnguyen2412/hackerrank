#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    print(s)
    len_s = len(s)
    print(len_s)
    len_sqrt = math.sqrt(len_s)
    row = math.floor(len_sqrt)
    col = math.ceil(len_sqrt)

    if (row*col < len_s):
        row = row + 1

    last_row_len = len_s - (row - 1)*col

    last_row_chars = s[len_s - last_row_len:]

    char_num = 0 # Start with the first character
    
    row_char_list = list()
    for i in range(row - 1):
        row_chars = s[i*col:(i+1)*col]
        row_char_list.append(row_chars)

    row_char_list.append(last_row_chars)

    print(row_char_list)

    col_char_list = list()

    for c in range(col):
        col_char = ''
        for r in range(row - 1):
            col_char += row_char_list[r][c]
        col_char_list.append(col_char)

    for c in range(last_row_len):
        col_char_list[c] += last_row_chars[c]

    ret_str = ''

    for col_char in col_char_list:
        ret_str += col_char + ' '

    return ret_str


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
