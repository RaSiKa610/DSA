#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    common = 0    
    min_length = min(len(s), len(t))
    for i in range(min_length):
        if s[i] == t[i]:
            common += 1
        else:
            break
    min_op = (len(s) - common) + (len(t) - common)
    
    if k == min_op:
        return "Yes"
    elif k > min_op and (k - min_op) % 2 == 0:
        return "Yes"
    elif k >= len(s) + len(t):
        return "Yes"
    else:
        return "No"
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
