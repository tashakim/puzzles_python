#Really cool minstack strategy

# Snapshots of min - stored as pair (val, min_at_val)
# Increasing min_at_vals stored in a separate stack


# Note: unsorted arrays...

	#Another cool third max strategy

	# Linear time complexity for finding maximum of array - looping though is 
	# faster than sorting - python uses timsort, an alternate to mergesort, hence
	# amortized average would be slower than stepping through each item of unsorted array.

	# Duplicate storing is where thought needs to be put:
		# Utilize hash set / table, or even a heap for constant space complexity

	#What about kth max?

	# Sort the array, then return kth item from the back.
	# Construct heap of size n - taking linear time, then pop n-k elements off this heap.
	# Wow: Restrict a min heap to size k, and store all elements in array

