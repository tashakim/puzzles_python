def makeArrayConsecutive2(statues):
    # [ 6, 2, 3, 8]
    # we need to add 4, 5, 7
    # start from min(statues), end at max(statues)
    start, end = min(statues), max(statues)
    # max-1  - min = x 
    slots = (end - 1) - start 
    # x - len(arr) - 2 = y
    res = slots - (len(statues) - 2)
    
    # return y
    return res
    
def adjacentElementsProduct(inputArray):
    # max_prod : keep track of max product
    max_prod = float('-inf')
    # cur_prod : keep track of current product
    cur_prod = float('-inf')
    
    # iterate through inputArray range(0, len(arr) - 1)
    for i in range(len(inputArray) - 1):
        # take product of arr[i] * arr[i+1]
        cur_prod = inputArray[i] * inputArray[i+1]
        # if current product > max product, update max.
        max_prod = max(cur_prod, max_prod)
        
    # return max product
    return max_prod
