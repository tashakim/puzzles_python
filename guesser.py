number_of_guesses = 1
correct_num = 10

while True:
	num = input("what is your number?: ")
	try:
		num = int(num)
	except:
		print("number must be an integer")
		continue

	if (num<correct_num):
		print("guess higher")
	elif (num > correct_num):
		print("guess lower")
	else:
		break
	number_of_guesses +=1

print("You guessed it correctly! number of guesses: ", number_of_guesses)
