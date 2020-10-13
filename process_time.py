
import time
import copy

t = time.process_time()

arr = [4,5,10, 1,2,3, 0,9]
new_arr = copy.deepcopy(arr)
new_arr.sort()
t2 = time.process_time()
print(t2 - t)
print(arr)
print(new_arr)

new_arr = copy.deepcopy(arr)
new_arr.sort()
t3 = time.process_time()
print(t3 - t2)
print(arr)
print(new_arr)

new_arr = copy.deepcopy(arr)
new_arr.sort()
t4 = time.process_time()
print(t4 - t3)
print(arr)
print(new_arr)

"""
new_arr = [x**x for x in arr]
t5 = time.process_time()
print(t5 - t4)
"""