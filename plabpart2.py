class Student:
  def __init__(self, c):
    self.name = "Tasha"
    self.concentration = c
    self.year = 2021

  def set_concentration(self, c):
    self.concentration = c

  def print_student(self):
    print(self.name)
    print(self.concentration)
    print(self.year)

class Animal():
  def __init__(self, kg, breed):
    self.weight = kg
    self.breed = breed
  
  def call(self, name):
    self.name = name

  def print_infor(self):
    print(self.name)
    print(self.weight)
    print(self.breed)


if __name__ == "__main__":
  tasha = Student("Math")
  tasha.set_concentration("CS")
  tasha.print_student()

  dog = Animal(6, "poodle")
  dog.call("Kamie")
  dog.print_infor()