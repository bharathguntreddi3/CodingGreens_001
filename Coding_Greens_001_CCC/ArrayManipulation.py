#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    arr = [0] * (n + 2)    # initialize array with zeros with n+2 starting with index 1, to avoid index out of bound error
    for a, b, k in queries:  # query operations
        arr[a] += k  # update first index
        arr[b+1] -= k  # for last index negate k which balances the array
        # print(arr)    # check the array output 

    temp = 0    # after sum of the array comparing with maxelement
    maxelement = temp   # store the maximum element
    for i in arr:
        temp += i
        maxelement = max(maxelement, temp)
    return maxelement

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
