# change contents of myList
myList = ["python", "csharp", "howmanyletters"]

# uses map function to count letters of item in myList.
result = map(len, myList)

# prints result of mapping
for item in result:
	print(item, end = '\n')