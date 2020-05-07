class Zoo:
	def __init__(self, number, animal1, animal2, animal3):
		self.number = number
		self.animal1 = animal1
		self.animal2 = animal2
		self.animal3 = animal3

	def rename(self, animal1, newName):
		self.animal1 = newName

if __name__ == "__main__":
	zoo = Zoo(3, "zebra", "giraffe", "panther")
	print(zoo.animal1)

	zoo.rename("zebra", "kkamie")
	print(zoo.animal1)