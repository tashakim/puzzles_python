import time

n = int(input("Input your number: "))
haystack = [k for k in range(n)]

t = time.time()
needle = max(haystack)
elapsed = time.time() - t
print("Elapsed time to find needle in haystack: %.2f\n" % elapsed)
