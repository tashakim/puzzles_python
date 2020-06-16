import sys
import math

n = int(input())  # the number of temperatures to analyse
min_n = float("inf")

if(n == 0): print(0)
else:
    for i in input().split():
        # t: a temperature expressed as an integer ranging from -273 to 5526
        t = int(i)
        if(abs(t) < abs(min_n)): min_n = t
        elif(abs(t) == abs(min_n) and t > min_n): min_n = t

    # To debug: print("Debug messages...", file=sys.stderr)
    print(min_n)
