def string_length(listOfStrings):
	result = []
	for item in map(len, listOfStrings): result.append(item)
	print(max(result))



if __name__ == "__main__":
	string_length(["cat", "a", "square"])

