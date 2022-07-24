#!/bin/python3

import math
import os
import random
import re
import sys
from collections import *

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    count = Counter(s)
    if len(set(count.values())) == 1:
        return "YES"   # if the values occurs single time 
    elif len(set(count.values())) > 2:
        return "NO"    # if the values occurs more than 2 times
    else:
        for i in count:
            count[i] -= 1
            temp = list(count.values())   # iterate the array for an element repeated 2 times
            try:
                temp.remove(0)    # remove
            except:
                pass
            if len(set(temp)) == 1:
                return "YES"
            else:
                count[i] += 1
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
