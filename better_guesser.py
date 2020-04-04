class Guesser:
	def __init__(self, my_number, min = 0, max = 100):
		self.number = my_number
		self.guesses = 0
		self.min = min
		self.max = max

	def get_guess(self):
		guess = input("what is your guess? : ")
		if self.is_valid(guess):
			return int(guess)
		else:
			print("the number is invalid")
			return self.get_guess()


	def is_valid(self, input_number):
		try:
			number = int(input_number)
		except:
			return False
		return self.min <= number <= self.max


	def play(self):
		while(True):
			self.guesses +=1
			guess = self.get_guess()
			if (guess < self.number):
				print("guess higher!")
			elif (guess > self.number):
				print("guess lower!")
			else:
				break
		print(f"Correct! you have guessed it in {self.guesses} tries.")

if __name__ == "__main__":
	newgame = Guesser(10)
	newgame.play()