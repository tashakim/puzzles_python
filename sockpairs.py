#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    mydict, count = {},0
    for x in ar:
        if x in mydict:
            mydict[x] += 1
        else:
            mydict[x] = 1
    for value in mydict.values():
        if value >= 2:
            count += math.floor(value//2)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
