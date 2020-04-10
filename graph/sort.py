#!/usr/bin/python3

class InvalidInputException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)


def merge_sort(array):
    """merge_sort: int array -> int array
        Purpose: Sort the input array of integers in descending order using the merge sort algorithm
        Example: merge_sort([4,5,1,3,2]) -> [5,4,3,2,1]
        Throws: InvalidInputException if list is None
    """
    checkValidity(array)

    if len(array)>1:
        mid = len(array)//2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] > righthalf[j]:
                array[k]=lefthalf[i]
                i=i+1
            else:
                array[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            array[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            array[k]=righthalf[j]
            j=j+1
            k=k+1
        return array


def quick_sort(array):
    """quick_sort: int array -> int array
        Purpose: Sort the input array of integers in descending order using the quicksort algorithm
        Example: quick_sort([4,5,1,3,2]) -> [5,4,3,2,1]
        Throws: InvalidInputException if list is None
    """
    checkValidity(array)

    # We define our 3 arrays
    less = []
    equal = []
    greater = []

    # if the length of our array is greater than 1
    # we perform a sort
    if len(array) > 1:
        # Select our pivot. This doesn't have to be
        # the first element of our array
        pivot = array[0]

        # recursively go through every element
        # of the array passed in and sort appropriately
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # recursively call quicksort on gradually smaller and smaller
        # arrays until we have a sorted list.
        return quick_sort(greater)+equal+quick_sort(less)
    else:
        return array



def radix_sort(array):
    """radix_sort: int array -> int array
        Purpose: Sort the input array of integers in descending order using the radixsort algorithm
        Example: radix_sort([4,5,1,3,2]) -> [5,4,3,2,1]
        Throws: InvalidInputException if list is None
    """
    checkValidity(array)

    max_element = max(array)
    digit = 1
    while max_element // digit > 0:
        radixSortHelper(array, digit)
        digit *= 10
    return array


def radixSortHelper(array, digit):
    n = len(array)
    output = [0] * n
    count = [0] * 10

    for i in range(0, n):
        index = array[i] // digit
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = array[i] // digit
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, n):
        array[i] = output[n-i-1]


def checkValidity(array):
    if array is None:
        raise InvalidInputException('List cannot be empty')


if __name__ == "__main__":
    array = [4,5,1,3,2]
    print(merge_sort(array))
    print(quick_sort(array))
    print(radix_sort(array))    

