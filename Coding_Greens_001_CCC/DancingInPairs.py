#!/bin/python3

import math
import os
import random
import re
import sys

t = int(input())
x = []
for i in range(t):
    inn = int(input())
    x.append(inn)
for i in x:
    d = 4*(i+1)   # days
    n = math.ceil((math.sqrt(d)-2)/2)  # number of students attending the class
    # for suppose the square root of first 3 days is 1, square root of next 5 days is 2 and the square root of next 7 days is 3
    if n%2 == 0:
        print("even")
    else:
        print("odd")
#     n = int(math.sqrt(i))
#     if n%2 == 0:
#         print("even")
#     else:
#         print("odd")

# same above logic implies here but fails some test cases