class ParkingSystem:

	def __init__(self, big: int, medium: int, small: int):
		self._slots = [big, medium, small]

	def addCar(self, carType: int) -> bool:
		self._slots[carType - 1] -= 1
		return self._slots[carType - 1] >= 0


class ParkingSystem2:

	def __init__(self, big: int, medium: int, small: int):
		self._big = big
		self._medium = medium
		self.small = small

	def addCar(self, carType: int) -> bool:
		if carType == 1 and self._big > 0:
			self._big -= 1
			return True

		elif carType == 2 and self._medium > 0:
			self._medium -= 1
			return True

		elif carType == 3 and self._small > 0:
			self._small -= 1
			return True

		return False
