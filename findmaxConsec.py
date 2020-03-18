# Instead of counting the number of consecutive characters,
#we will return the character that occurs most frequently.

def findmaxConsec(array) :
	count = 1
	newcount = 1
	prev = None
	char = None

	if array == [] or array == None:
		return ""

	for element in array:
		if element == prev: 
			newcount+=1
			if newcount > count:
				count = newcount
				char = element
		else:
			newcount = 1
		prev = element
	return char

if __name__ == "__main__":
	array = [1,2,2,3,4]
	array2 = ['a','b','c','c','c','d']

	print(findmaxConsec(array))
	print(findmaxConsec(array2))

	findmaxConsec(['m','m','m','n','m','n','n']) == 'm', "Error!"
	findmaxConsec(['s','t','s','t','s']) == 's', "Error!"