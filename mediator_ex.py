class Colleague(object):
	def __init__(self, mediator, id):
		self._mediator = mediator
		self._id = id

	def getID(self):
		return self._id

	def send(self, msg):
		pass

	def receive(self, msg):
		pass

class ConcreteColleague(Colleague):
	def __init__(self, mediator, id):
		super().__init__(mediator, id)

	def send(self, msg):
		print("Message " + msg + " sent by " + str(self._id))
		self._mediator.distribute(self, msg)

	def receive(self, msg):
		print("Message " + msg + " received by " + str(self._id))

class Mediator:
	def add(self, colleague):

	def distribute(self, sender, msg):


class ConcreteMediator(Mediator):
	"""Inherits from Mediator class

	def __init__(self):
		Mediator.__init__(self):

	def add(self, colleague):

	def distribute(self, sender, msg):


def main():