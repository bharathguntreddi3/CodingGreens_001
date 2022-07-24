#!/bin/python3

import sys

t=int(input().strip())
for i in range(t):
    n=int(input().strip())
    count=0
    ans=5*n
    val=n
    while val>0:
        count+=val
        if val<5:  
            if count==n:
                break
            elif count<n:
                ans=ans+5
                break
            else:
                ans=ans-5
                val=ans
                count=0
        elif count>=n:
                ans=ans-5
                val=ans
                count=0
        val=val//5
    print(ans)
    
'''Terminated Due to Timeout'''