h = 3

for i in range(0, h+1):
	count = 0
	while list[0].depth == i:
		list.pop(0)
		count =+ 1
	k = 2**i - count

