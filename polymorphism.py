class Bird:
	def intro(self):
		print("Hello I'm a bird")

	def fly(self):
		print("Bird flies")

class Albatross(Bird):
	def fly(self):
		print("Albatross soars")

class Sparrow(Bird):
	def fly(self):
		print("Sparrow flies")

class Penguin(Bird):
	def fly(self):
		print("Penguin could not fly")

if __name__ == "__main__":
	bird = Bird()

	albatross = Albatross()
	sparrow = Sparrow()
	penguin = Penguin()
	my_birds = [albatross, sparrow, penguin]

	bird.intro()
	bird.fly()

	for bird in my_birds:
		bird.intro()
		bird.fly()

	
