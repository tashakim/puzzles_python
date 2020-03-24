def enqueue(list, value):
	list.append(value)
	return list

def dequeue(list):
	if list == [] or None:
		print("error")
		return
	list.remove(list[0])
	return list