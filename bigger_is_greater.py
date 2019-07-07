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
def biggerIsGreater_bruteforce(w):
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

    index_left = index - 1
    # First exchange two consecutive elements to get the bigger one than the origi
    while (index > 0 and index_left >= 0): # Except the first letter
        current_letter = w_letter_list[index]
        left_letter = w_letter_list[index_left]
        if (current_letter > left_letter):  # Find a greater here
            swap_flag = True
            temp_letter = current_letter    # right letter
            w_letter_list[index] = left_letter
            w_letter_list[index_left] = temp_letter
            mark_index = index_left # point marking the left position where we exchanged
            break
        index_left -= 1
        index -= 1

    # Second, find the minimum permutation
    if (swap_flag == True):
        prefix = w_letter_list[:mark_index + 1] # split the orig to prefix and suffix
        suffix = w_letter_list[mark_index + 1:] # by the mark point
        suffix.sort()
        print(prefix, suffix)

        suffix_set = list(set(suffix))
        suffix_set.sort()
        suffix_set_len = len(suffix_set)

        # Now find the bigger closest to the right letter which already be xchanged
        if (left_letter != suffix_set[suffix_set_len - 1]):
            start_to_swap_letter_idx = suffix_set.index(left_letter)
            i = start_to_swap_letter_idx + 1
            to_swap_letter = suffix_set[i]
            if (to_swap_letter < current_letter):
                prefix[len(prefix) - 1] = to_swap_letter
                suffix[suffix.index(to_swap_letter)] = current_letter
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
