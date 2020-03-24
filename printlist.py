string = "this is my list"
list = string.split(" ")
print(list)

#print the  string method1
for item in list:
	print(item, end = " ")
print()

#print the  string method2
for i in range(len(list)) :
	print(list[i], end = " ")
print()

#print the string method3
print(string)

