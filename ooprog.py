#Object oriented programming

class Person:

	def __init__(self, name):
		self._name = name

	def name(self):
		return self._name

class Student(Person):

	def __init__(self, name, ID, concentration, year):
		self._name = name
		self._ID = ID
		self._concentration = concentration
		self._year = year

	def declare(self,concentration):
		self._concentration = concentration

	def printInfo(self):
		print("Name : ", self._name)
		print("ID : ", self._ID)
		print("Concentration : ", self._concentration)
		print("Graduation year : ", self._year,"\n")


if __name__ == "__main__":
	ayrith = Student("ayrith", 1, "undeclared", 2022)
	ayrith.declare("mathematics")

	ayrith.details()

	print( Person.name(ayrith))