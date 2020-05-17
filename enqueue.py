# Simple python implementation of a queue
def enqueue(mylist, value) :
	mylist.append(value)
	return mylist

def dequeue(mylist) :
	if mylist == [] :
		print("list is empty")
		return mylist
	mylist.remove(mylist[0])
	return mylist


if __name__ == "__main__":
	mylist = [1,2,3]
	print(enqueue(mylist, 4))
	print(dequeue(mylist))

	assert dequeue([]) == [], "Error!"

	# Taking in user's input
	print("what number do you want to enqueue? : ")
	your_choice = input()
	enqueue(mylist, int(your_choice))

	# List with user's input enqueued.
	print(mylist)