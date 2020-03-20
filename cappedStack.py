
class cappedStack:
  def __init__(self):
    stack = []*10
    count = 0

  def push(object):
    if count < 10:
      stack.append(object)
      count +=1
    else:
      print("stack is full. cannot push object.")
    return

  def push(object):
    if count == 0:
      print("stack is empty. cannot pop object.")
    else:
      stack.remove(stack[count])
      count -=1

  def isEmpty():
    return count == 0

  def size():
    return count
