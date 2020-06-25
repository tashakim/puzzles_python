import time

n = int(input("Number of elements: "))
haystack = [k for k in range(n)]

print("Searching for maximum value...")

ts = time.time()
max_val = max(haystack)
elapsed = time.time() - ts

print("Maximum element = %d, Elapsed time = %.2f" % (max_val, elapsed))