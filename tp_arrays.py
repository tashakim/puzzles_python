from array import *

# list vs. array

array1 = array('i', [10,20,30,40,50])
array2 = array('l', [10,20,30,40,50])
array3 = array('d', [0.1,0.2,0.3,0.4,0.5])

for x in array1:
	print(x, end = " ")
for y in array2:
	print(y)
for i in range(5):
	print(array3[i], end = " ") # print on same line

list1 = [10,20,30,40,50]

for x in list1:
	print(x) 