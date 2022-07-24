#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. 2D_INTEGER_ARRAY queries
#

def solve(arr, queries):
    # Write your code here
    result = []    # create an empty list to store the resultant odd or even
    for i,j in queries:    # iterate through the given queries for the 2 numbers
        if(i==j):    # if two are equal
            if arr[i-1] % 2 == 0:    # check for even or not
                result.append("Even")   # append even
            else:
                result.append("Odd")   # else append odd
        elif arr[i] == 0:     # check for any element ia array is eqaul to 0
            result.append("Odd")
        elif arr[i-1] % 2 == 0:      # then again check for odd or even
            result.append("Even")
        else:
            result.append("Odd")
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = solve(arr, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
