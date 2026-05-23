#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    c_max = 0
    c_min = 0
    min_score = scores[0]
    max_score = scores[0]
    for i in scores[1:]:
        if i > max_score:
            max_score = i
            c_max += 1
        elif i < min_score:
            min_score = i
            c_min += 1
            
    return [c_max, c_min]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
