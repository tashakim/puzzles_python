def fibonacci():
  i = 1
  j = 1
  print(i)
  print(j)
  for num in range(98):
    sum = i+j
    print(sum)
    i = j
    j = sum 
  return

def factorial(n):
  if(n == 0):
    return 1
  return n*factorial(n-1)



if __name__ == "__main__":
  fibonacci()

  assert(factorial(2) == 2), "should be 2"
  print(factorial(2))
  print(factorial(3))