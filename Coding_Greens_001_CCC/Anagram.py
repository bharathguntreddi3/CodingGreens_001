from collections import *

def anagram(st):
    if len(st)%2: 
        return -1    # odd strings cannot be broken into two equal substrings
    l = len(st)//2
    b1 = Counter(st[:l])    # form dictionary array with the l as last index
    b2 = Counter(st[l:])    # form dictionary array with the l as first index
    return l-sum((b1 & b2).values())    

n = int(input())
for i in range(n):
    print(anagram(input()))