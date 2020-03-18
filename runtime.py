#Input: array.
#Write three functions that each have constant, linear, and quadratic running time.

def one(array) :
	return array[0]

def two(array) :
	my_list = []
	for i in range(0,len(array)-1):
		my_list.append(array[i])
	return my_list


def three(array) :
	my_list = []
	for i in range(0, len(array)-1):
		for j in range(0, len(array) -1):
			my_list.append(array[j]*array[i])
	return my_list


if __name__ == "__main__":
	array = [1,2,3,4,5]
	print(one(array))
	print("one() ran in constant running time!\n")

	print(two(array))
	print("two() ran in linear running time!\n")
	
	print(three(array))
	print("three() ran in quadratic running time!")