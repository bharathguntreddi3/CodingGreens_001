#!/bin/python3

import math
import os
import random
import re
import sys
from fractions import *

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

def solve(n):
    # Write your code here
    divisors = [1]    # divisors are total outcomes 1 as the common divisor
    x = math.sqrt(n)
    for i in range(2, int(x)+1):
        if n%i == 0:
            divisors.append(i)
            if(n//i != i):
                divisors.append(n//i)
    divisors.sort()
    temp = 0    # temp for counting the total number of favourable outcomes
    for i in divisors:
        x = math.sqrt(i)
        if i%2 == 0 and int(x+0.5)**2 == i:
            temp = temp + 1
    if temp == 0:
        return "0"
    else:
        return str(Fraction(temp,len(divisors)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()