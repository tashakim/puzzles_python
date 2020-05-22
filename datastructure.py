def initialize():
	"""Purpose:
	"""
	mylist = []
	myqueue = []

def add_to_structure(x):
	mylist.append(x)
	myqueue.append(x)

def remove_from_structure():
	mylist.pop()
	myqueue.pop(0)


if __name__ == "__main__":
	initialize()

	add_to_structure(1)
	remove_from_structure()