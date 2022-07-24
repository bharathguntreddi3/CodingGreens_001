#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    # Write your code here
    s = list(s)   # convert string to list of characters
    mark = [0] * n  # mark the changed index

    # basic - numbeeing from 0-9 with 9 as maximum to be filled
    # change digits to palindrome
    l = 0  # index starting from left 
    r = n - 1  # right index
    while l <= r :  # check l and r for each iteration
        if s[l] != s[r]:   # check if left element is equal or not equal to right element
            if s[l] > s[r]:    # if left greater than right
                s[r] = s[l]    # initialize s[r] with s[l] element i.e the greater element 0-9
                mark[r] = 1    # mark the initialized element
            elif s[l] < s[r]:  # if left less than right
                s[l] = s[r]    # initialize s[l] with s[r] element i.e the greater element 0-9
                mark[l] = 1    # mark the initialized element
            k -= 1   # decrement k
        l += 1  # increment l next element
        r -= 1  # decrement r next element
    if k < 0:     # check whether we changed to palindrome with the above changes
        return "-1"   # return -1

    # maximizie the digits maximum value upto 9 i.e range 0-9 
    l = 0
    r = n - 1
    while l <= r:    # iterate for l <= r
        if l == r and k >= 1:     # middle index
            s[l] = '9'  # change middle index to 9
            break
        if s[l] < '9':  # check for value less than maximum value 9
            # no changes before
            if mark[l] == 0 and mark[r] == 0 and k >= 2:    # when there are no changes applied
                s[l] = s[r] = '9'   # if there are no changes before and k>=2 then put 9 to left and right
                k -= 2    # no changes before and change index to 9 
                # changed before
                if (mark[l] == 1 or mark[r] == 1) and k >= 1:   # when changes applied
                    s[l] = s[r] = '9'    # if there are changes applied and k>=2 then put 9 to left and right
                    k -= 1    # one change has  occured for next change decrement k
        l += 1    # again increment left to the next element
        l -= 1    # again decrement right to the next element
        # The loop continues to run untill we get the highest palindrome range 0-9 maxumum number 9
    return "".join(s)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
