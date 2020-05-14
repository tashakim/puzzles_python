# Simple implementation of a queue

def enqueue(list, value) :
	list.append(value)
	return list

def dequeue(list) :
	if list == [] :
		print("list is empty")
		return list
	list.remove(list[0])
	return list


if __name__ == "__main__":
	list = [1,2,3]
	print(enqueue(list, 4))
	print(dequeue(list))

	assert dequeue([]) == [], "Error!"

	# Taking in user's input
	print("what number do you want to enqueue? : ")
	your_choice = input()
	enqueue(list, int(your_choice))

	# List with user's input enqueued.
	print(list)