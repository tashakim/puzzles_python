
def divideBySixty(time):
	count = 0
	for i in range(len(time)):
		for j in range(i+1, len(time)):
			if (time[i] + time[j])%60 == 0:
				count += 1
	return count



if __name__ == "__main__":
	l = [30, 20, 100, 150, 40]
	print(divideBySixty(l))