class Arithmetic:
	def __init__(self, a,b):
		self.param1 = a
		self.param2 = b

	def add(self):
		print(self.param1 + self.param2)
	

if __name__ == "__main__":
	arithmetic = Arithmetic(1,2)
	arithmetic.add()