def max_sequence(arr):
    # ... 
    if (len(arr) == 0):
        return 0
    sum = 0
    if (min(arr) >= 0):
        for item in arr:
            sum += item
        return sum
    if (max(arr) < 0):
        return 0
    
    temp = arr
    for i in range(1, len(arr)):
            if (temp[i] + temp[i-1] > temp[i]):
                temp[i] = temp[i] + temp[i-1]
    return max(temp)