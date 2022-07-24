#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def poisonousPlants(p):
    # Write your code here
    # Compare the current element with the left element takes O(n2)
    # store plants find the maximum day and give the last final plants
    stack = []
    maxday = 0
    for plant in p:
        day = 0
        while stack and stack[-1][0] >= plant:  # comparing the top of stack with the each element
            day = max(day, stack.pop()[1])
        if stack:
            day += 1
        else:
            day = 0
        maxday = max(maxday, day)
        stack.append([plant, day])
    return maxday
                
# initially stack - [6, 0] # popping out the stack and the stack remains empty 
# now append the next element i.e [5, 0], [8,1]
# now append [4,0] [7,1] [9,2]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()
