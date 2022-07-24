#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    seqlist = [[] for i in range(n)]  # initialize sequence list 
    lastanswer = 0
    result = []
    for query,x,y in queries:
        if query == 1:   # for query 2
            indx = (x ^ lastanswer) % n
            seqlist[indx].append(y)    # append y to the sequence list
        else:
            if query == 2:
                indx = (x ^ lastanswer) % n
                val = y % len(seqlist[indx])   # assign this to the value
                lastanswer = seqlist[indx][val]   # and append to the lastanswer
                result.append(lastanswer)    # and finally append to the result
    return result
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
