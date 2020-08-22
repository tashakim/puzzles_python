class Bird:
	def intro(self):
		print("Hello I'm a bird")

	def fly(self):
		print("Bird flies")


class Albatross(Bird): # Inherits from Bird class
	def fly(self): # Polymorphism of Bird's method
		print("Albatross soars")

class Sparrow(Bird): # Inherits from Bird class
	def fly(self): # Polymorphism of Bird's method
		print("Sparrow flies")

class Penguin(Bird): # Inherits from Bird classvv
	def fly(self): # Polymorphism of Bird's method
		print("Penguin could not fly")


if __name__ == "__main__":
	bird = Bird()

	albatross = Albatross()
	sparrow = Sparrow()
	penguin = Penguin()
	my_birds = [albatross, sparrow, penguin] # Create collection of my birds

	bird.intro() # "Hello I'm a bird"
	bird.fly() # "Bird flies"

	for bird in my_birds:
		bird.intro()
		bird.fly() # Each bird flies its own way


