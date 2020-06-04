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


class Stack():
  """Purpose: simple python implementation  of a stack.
  """
  def __init__(self):
    self.stack = []
    
  def push(self, el):
    self.stack.append(el)

  def pop(self):
    return self.stack.pop()

  def print_stack(self):
    print(self.stack)


if __name__ == "__main__":
  # testing queue
  print("let's test our queue:\n")
  q = Queue()
  q.enqueue('s')
  q.print_queue()

  q.enqueue('t')
  q.enqueue('e')
  q.print_queue()

  q.dequeue()
  q.print_queue()
  print("\n")

  # testing stack
  print("let's test our  stack:\n")
  s = Stack()
  s.push(1)
  s.push(0)
  s.print_stack()

  s.pop()
  s.print_stack()
  print("\n")

  