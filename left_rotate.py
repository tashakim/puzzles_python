#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
""" Time constraint exceeded:
def rotLeft(a, d):
    # Time complexity: O(n*d), n = len(a)
    for i in range(d):
        helper(a)
    return a

def helper(a):
    # Time complexity: O(n), n = len(a)
    i = 0
    while i < len(a)-1:
        a[i], a[i+1] = a[i+1], a[i]
        i += 1
    return a
"""
def rotLeft(a,d):
    # Time complexity: O(n), n = len(a)
    # Space complexity: O(n), n = len(a)
    temp = a[d:] + a[:d]
    for i in range(len(a)):
        a[i] = temp[i]
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))
    result = rotLeft(a, d)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()