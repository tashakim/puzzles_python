class Queue():
  """Purpose: simple python implementation of a queue.
  """
  def __init__(self):
    self.queue = []
  
  def enqueue(self, el):
    self.queue.append(el)

  def dequeue(self):
    self.queue.pop(0)
    return self.queue[0]

  def print_queue(self):
    print(self.queue)


if __name__ == "__main__":

  q = Queue()
  q.enqueue('s')
  q.print_queue()

  q.enqueue('t')
  q.enqueue('e')
  q.print_queue()

  q.dequeue()
  q.print_queue()
  