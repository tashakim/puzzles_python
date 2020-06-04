def findConsecutiveMax(arr):
  """Purpose:  returns character that occurs the greatest no. of consec times. 
  arr -> char
  """
  max_count = 1
  count = 1
  cur = arr[0]

  for i in range(1,len(arr)):
    if(arr[i] == cur):
      count +=1
      if(count > max_count):
        max_count = count
    else:
      count = 1
    cur = arr[i]
  return max_count

if __name__ == "__main__":
  s=['c','c','a','b','e','e','e']
  print(findConsecutiveMax(s))
  t= ['e','f','g','a','a','e','a','b','f']
  print(findConsecutiveMax(t)) 