# change contents of myList
myList = ["python", "csharp", "howmanyletters"]

# uses map function to count letters of item in myList.
result = []
for item in map(len, myList):
	result.append(item)

# prints result of mapping
print(result)