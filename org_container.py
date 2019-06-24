#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    container_len = len(container)
    type_len = container_len

    container_load_list = [sum(container_ele) for container_ele in container]
    
    type_load= list()
    for i in range(container_len):
        type_load.append([ele[i] for ele in container])

    print(type_load)

    type_load_list = [sum(ball_type) for ball_type in type_load]

    count = 0

    for container_load  in container_load_list:
        if (container_load in type_load_list):
            count += 1
            type_load_list.remove(container_load)

    if (count == container_len):
        return('Possible')
    else:
        return('Impossible')
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
