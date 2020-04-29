_list = ["four", "fives", "eleven"]

def max_string_length(_list):
	return reduce(max, map(len, _list), 0)


# anonymous function that doubles a single number 
lambda x: 2*x
# anonymous function that doubles all elements in a list
map(lambda x: 2*x, myList)
# anonymous function that raises x to the nth power
lambda x, n: x**n
# eliminates duplicates in a list using 'reduce' function only
def compress(myList):
	return reduce(lambda: x, y: x + [y] if x[-1] is not y else x, myList, myList[:1])
#implement a map using reduce
def my_map(function, list):
	return reduce(lambda x,y: x + [function(y)], list, [])