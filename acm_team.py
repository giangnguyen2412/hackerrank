#!/bin/python3

import math
import os
import random
import re
import sys

# Perform or operation on two strings
def or_str(str1, str2):
    or_len = len(str1)
    ret_list = list()
    for i in range(or_len):
        if (str1[i] == '0' and str2[i] == '0'):
            ret_list.append(0)
        else:
            ret_list.append(1)
    return ret_list

# Complete the acmTeam function below.
def acmTeam(topic):
    topic_len = len(topic)
    or_list = list()
    for i in range(topic_len - 1):
        for j in range(i+1, topic_len):
            topic1 = int(topic[i], base = 2)
            topic2 = int(topic[j], base = 2)
            or_list.append(topic1 | topic2)

    or_list_len = len(or_list)
    count_tmp = 0
    count = 0
    for i in range(or_list_len):
        if (bin(or_list[i]).count('1') > count_tmp):
            count_tmp = bin(or_list[i]).count('1')
            count = 1
        elif (bin(or_list[i]).count('1') == count_tmp):
            count = count + 1

    return [count_tmp, count]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
