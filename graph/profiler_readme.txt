These are the runtimes for the following algorithms:

QUICK SORT
	numlist1.txt time: 0.02399420738220215
	numlist2.txt time: 0.5084707736968994
MERGE SORT
	numlist1.txt time: 0.04488992691040039
	numlist2.txt time: 0.04131817817687988
RADIX SORT
	numlist1.txt time: 0.03035902976989746
	numlist2.txt time: 0.030843257904052734

We notice that for numlist1, quick sort algorithm runs the fastest. On the other hand, merge sort runs the slowest.

For numlist2, surprisingly, quick sort algorithm runs the 
slowest. On the other hand, radix sort and merge sort runs
faster. 

Quick sort:
-I think that "quick sort algorithm" runs faster on numbers that
have larger difference in values, hence much faster for 
numlist1.txt compared to numlist2.txt.
-The expected runtime of quick sort is O(n log(n)),
however as you can see from the time it took to run numlist2,
the worst case runtime of quick sort is much larger.

Merge sort:
-The "merge sort algorithm" had very similar runtime for the 
two lists, numlist1.txt and numlist2.txt. 

Radix sort:
-"Radix sort algorithm" ran similarly for both numlist1.txt and 
numlist2.txt, and this makes sense because the worst case 
runtime of radix sort depends on the number of digits in the 
largest number. Since both of numlist1.txt and numlist2.txt's
largest number has 5 digits, they run in similar time.