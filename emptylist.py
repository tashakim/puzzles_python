empty_list = [(), '',[],{}, 2,3,4]

for item in empty_list:
	if not item:
		print('something is wrong. List contains ', item)

