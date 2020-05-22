def initialize():
	"""Purpose:
	"""
	mylist = []
	myqueue = []

	return [mylist, myqueue]

def add_to_structure(l,q,x):
	l.append(x)
	q.append(x)

	print("mylist: ", l, ", myqueue: ", q)

def remove_from_structure(l,q):
	l.pop()
	q.pop(0)
	print("mylist: ", l, ", myqueue: ", q)


if __name__ == "__main__":
	l = initialize()[0]
	q = initialize()[1]
	add_to_structure(l, q, 1)
	add_to_structure(l, q, 2)
	remove_from_structure(l, q)
