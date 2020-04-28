def string_length(listOfStrings):
	for item in map(len, listOfStrings): print(item, end = '\n')


if __name__ == "__main__":
	string_length(["cat", "a", "square"])