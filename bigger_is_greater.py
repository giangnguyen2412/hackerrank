#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations
from copy import deepcopy

def concatenate(w_list):
    permuted_word = ''

    for c in w_list:
        permuted_word += c

    return permuted_word

# Complete the biggerIsGreater function below.
def biggerIsGreater1(w):
    w_len = len(w)
    w_list = list()

    for i in range(w_len):
        w_list.append(w[i])

    w_permut = list(set(permutations(w_list)))
    w_permut_len = len(w_permut)
    w_permut.sort()

    if (w_permut[w_permut_len - 1] == tuple(w_list)):
        return 'no answer'

    w_index = w_permut.index(tuple(w_list))

    permuted_word = ''
    for c in w_permut[w_index + 1]:
        permuted_word += c

    return permuted_word  

def biggerIsGreater(w):
    w_len = len(w)
    w_letter_list = list(w)
    index = w_len - 1
    mark_index = -1
    swap_flag = False
    inner_break = False

    while (index > 0): # Except the first letter
        if (inner_break == True):
            break
        current_letter = w_letter_list[index]
        index_left = index - 1
        while (index_left >= 0):
            left_letter = w_letter_list[index_left]
            #print(current_letter, left_letter, index, index_left)
            if (current_letter > left_letter):  # Find a greater here
                swap_flag = True
                temp_letter = current_letter
                w_letter_list[index] = left_letter
                w_letter_list[index_left] = temp_letter
                mark_index = index_left
                inner_break = True
                break
            index_left -= 1
        index -= 1

    prefix = w_letter_list[:mark_index + 1]
    suffix = w_letter_list[mark_index + 1:]
    #print(prefix)
    suffix.sort()


    if (swap_flag == False): # Can not find any possible
        return 'no answer'
    else:
        solution = prefix + suffix
        return concatenate(solution)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
