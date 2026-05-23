#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    d = 0
    
    if 1700 <= year <= 1917:
        if year % 4 == 0:
            d = 12
        else:
            d = 13
    
    elif year == 1918:
        d = 26
    elif 1919 <= year <=2700:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            d = 12
        else:
            d = 13
    return f"{d:02d}.09.{year}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
