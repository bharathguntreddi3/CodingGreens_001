#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER n
#  2. INTEGER m
#

def solve(n, m):
    # Write your code here
    a_mod_m = 1
    i = 1
    mod_power = 10
    while 2*i<=n:
        a_mod_m = (((mod_power+1)%m)*a_mod_m)%m
        i *= 2
        mod_power = mod_power*mod_power%m
    if i!=n:
        a_mod_m = (a_mod_m+(mod_power*solve(n-i,m)))%m
    return a_mod_m

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = solve(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
