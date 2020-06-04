from datetime import date

class InvalidInputException:
  def __init__(self):
    return


def is_prime(n):
  """is_prime: int -> boolean
  Purpose: Test whether the given number is prime or not
  Example: is_prime(3) -> True
  """
  if(n<0):
    raise InvalidInputException("Input must be a positive number.")
  if(n<2):
    return False
  if(n == 2):
    return True
  else:
    for i in range(2, n//2):
      if(n%i == 0):
        print(n, "is not a prime number.")
        return False
  print(n, "is a prime number.")
  return True


def get_today():
  today = date.today()
  return today.day


def test_is_prime():
  assert is_prime(5) == True, "Test failed: 5 is prime"
  assert is_prime(11) == True, "Test failed: 11 is prime"
  assert is_prime(22) == False, "Test failed: 22 is not prime"
  print("All tests passed!\n")


if __name__ == "__main__":
  test_is_prime()
  is_prime(get_today())