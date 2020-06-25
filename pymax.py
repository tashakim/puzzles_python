import time
"""Search through the haystack
"""

n = int(input("Number of elements: "))
haystack = [k for k in range(n)]

print("Searching for maximum value...")

ts = time.time()
max_val = max(haystack) 
elapsed = time.time() - ts # time elapsed to find 'max_val' in 'haystack'.

print("Maximum element = %d, Elapsed time = %.2f" % (max_val, elapsed))