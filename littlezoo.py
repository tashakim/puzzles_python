class Zoo:
	def __init__(self, number, animal1, animal2, animal3):
		self.number = number
		self.animal1 = animal1
		self.animal2 = animal2
		self.animal3 = animal3
		print("\nCreated a new zoo with", self.number, "animals!")

	def rename(self, animal1, newName):
		self.animal1 = newName
		print(self.animal1, "is now", newName)

	def brush(self, animal):
		print("Brushed", animal)

	def feed(self, animal):
		print("Fed", animal)

if __name__ == "__main__":
	zoo = Zoo(3, "zebra", "giraffe", "panther")
	print(zoo.animal1)

	zoo.rename("zebra", "my zebra")
	zoo.brush(zoo.animal1)
	zoo.feed(zoo.animal2)


	newzoo = Zoo(0, None, None, None)
