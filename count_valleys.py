#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level, vall = 0,0
    for c in s:
        if level == 0 and c == "D":
            vall += 1

        if c == "U":
            level += 1
        else: #(c == "D")
            level -= 1
    return vall
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    fptr.write(str(result) + '\n')
    fptr.close()
