def nestLists(name, score):
	"""Purpose: given a list of n items, store them 
	in a nested list, and print the name associated
	with the second-lowest grade.
	"""
	arr = []
	for i in range(len(name)):
		arr.append([name[i], score[i]])
	l = [x for x in score if x!= min(score)]

	result = []
	for item in arr:
		if(item[1] == min(l)):
			result.append(item[0]) # adds names of second-lowest scores
	result.sort() # sorts names alphabetically

	for i in result:
		print(i) # prints each name in list


if __name__ == "__main__":
	nestLists(['H', 'B', 'T', 'A', 'H'], [3,3,1,4,5])

	nestLists(['Tash', 'MJ', "Angie"], [0,1,2])
