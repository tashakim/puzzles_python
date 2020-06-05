import random

def prog1():
  """Purpose: Hash function that generates one random number to increment
  """
  arr = []
  for k in range(1,5):
    arr = [None]*(2**k)
    for i in range(2**k):
      arr[i] = i+1
    print("array is: ", arr)

    b = [0]*(2**k)
    for i in range(2**k):
      r=random.randrange(2**k)
      b[r]+=1
      print(b)

    print("n = ", 2**k)
    print("Maximum B[i]: ", max(b))
    print()


def prog2():
  """Purpose: Hash function that generates two random nums and increments the smaller B[i].
  """
  arr = []
  for k in range(1,5):
    arr = [None]*(2**k)
    for i in range(2**k):
      arr[i] = i+1
    print("array is: ", arr)

    b = [0]*(2**k)
    for i in range(2**k):
      i=random.randrange(2**k)
      j=random.randrange(2**k)
      r = min(b[i], b[j])
      b[r]+=1
      print(b)

    print("n = ", 2**k)
    print("Maximum B[i]: ", max(b))
    print()


if __name__ == "__main__":
  prog1()
  #prog2()