from matplotlib import pyplot as plt
import hybrid_sorting
import time
import numpy as np
import copy

def get_random_list(n):
	return np.random.randint(np.iinfo(np.int).min, np.iinfo(np.int).max, 2**n).tolist()

def find_threshold(n):
	num_samples = 50
	np.random.seed(0)
	unsorted = [get_random_list(n) for i in range(num_samples)]
	thresholds = range(1, n+1)

	# threshold testing hybrid sorting algorithm
	avg_times = []
	for threshold in thresholds:
		times = []
		for this_list in unsorted:
			copy_list = copy.deepcopy(this_list)

			t0 = time.process_time()
			hybrid_sorting.hybrid_sort(copy_list, threshold)
			t1 = time.process_time()

			times.append(t1-t0)
		avg_time = sum(times)/len(times)
		avg_times.append(avg_time)
		#print(avg_time)
	plt.plot(range(1, n+1), avg_times)
	plt.show()


"""
t = time.process_time()

arr = [4,5,10, 1,2,3, 0,9]
new_arr = copy.deepcopy(arr)
new_arr.sort()
t2 = time.process_time()
print(t2 - t)
print(arr)
print(new_arr, end = "\n\n")

new_arr = copy.deepcopy(arr)
new_arr.sort()
t3 = time.process_time()
print(t3 - t2)
print(arr)
print(new_arr, end = "\n\n")

new_arr = copy.deepcopy(arr)
new_arr.sort()
t4 = time.process_time()
print(t4 - t3)
print(arr)
print(new_arr, end = "\n\n")

"""
"""
new_arr = [x**x for x in arr]
t5 = time.process_time()
print(t5 - t4)
"""
print("############# Hybrid sort ##############")
arr = [4,5,10, 1,2,3, 0,9]
res = []
for threshold in range(1, 120):
	t = time.process_time()
	new_arr = copy.deepcopy(arr)
	hybrid_sorting.hybrid_sort(new_arr, threshold)
	t2 = time.process_time()
	res.append(t2-t)
#print(res)

#plt.plot(range(1, 120), res)
#plt.show()

print("############# Hybrid sort thresholds testing ##############")
find_threshold(10)

