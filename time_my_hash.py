import timeit


def s(data, n): # Complete!
  # Solution 2. Hash table
  # T.C: O(n), S.C: O(n)
  mydict = {}
  for x in data:
    if x in mydict: mydict[x] += 1
    else: mydict[x] = 1
  
  res = [x for x in data if mydict[x] <= n]
  if res == []: return None
  return res



def s1(data, n): # Complete!
  # Solution 2. Hash table
  # T.C: O(n), S.C: O(n)
  mydict = {}
  for x in data:
    if x in mydict:
      mydict[x] += 1
    else:
      mydict[x] = 1
  # can optimize hash table, by storing lists

  for k,v in mydict.items():
    if v > n:
      for i in range(v):
        data.remove(k)
  if data == []: return None
  return data


def test():
  assert(s([1,2,3], 0)) == None, "Wrong"
  assert(s([1,2,2,3,3,3,4,5,5],1)) == [1,4], "Wrong"
  assert(s([5,4,4,6,5,7,5,5], 3)) == [4,4,6,7], "Wrong"

  assert(s([-1, 9, -9, -9, 0, 0], 1)) == [-1, 9], "Wrong"
  assert(s([-1, 9, -9, -9, 0, 0], -1)) == None, "Wrong"
  assert(s([-1, 9, -9, -9, 0, 0], 2)) == [-1, 9, -9, -9, 0, 0], "Wrong"
  assert(s([-1, 9, -9, -9, 0, 0], 1.5)) == [-1, 9], "Wrong"

  assert(s([], 1)) == None, "Wrong"
  assert(s([1], 1)) == [1], "Wrong"
  assert(s([0,0,0,0,0,0,0,0,99], -10)) == None, "Wrong"
  assert(s([0,0,0,0,0,0,0,0,99], 10)) == [0,0,0,0,0,0,0,0,99], "Wrong"

def time():
  elapsed_time = timeit.timeit(code_to_test, number = 100)/100
  print(elapsed_time)

if __name__ == "__main__":
  #time()
  test()
  