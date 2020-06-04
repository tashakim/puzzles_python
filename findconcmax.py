def findConsecutiveMax(arr):
  """Purpose:  returns character that occurs the greatest no. of consec times. 
  arr -> char
  """
  max_count = 1
  count = 1
  cur = arr[0]
  char = cur

  for i in range(1,len(arr)):
    if(arr[i] == cur):
      count +=1
      if(count > max_count):
        max_count = count
        char = arr[i]

    else:
      count = 1
    cur = arr[i]

  return char

if __name__ == "__main__":

  s=['c','c','a','b','e','e','e']
  print(findConsecutiveMax(s)) # 'e' occurs 3 times

  t= ['e','f','g','a','a','e','a','b','f']
  print(findConsecutiveMax(t)) # 'a' occurs 2 times