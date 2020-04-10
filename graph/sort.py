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
    checkValidInput(array)

    n = len(array)
    if n > 1:
        left = array[:n//2]
        right = array[n//2:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0       
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
        return array
    else:
        return array


def quick_sort(array):
    """quick_sort: int array -> int array
        Purpose: Sort the input array of integers in descending order using the quicksort algorithm
        Example: quick_sort([4,5,1,3,2]) -> [5,4,3,2,1]
        Throws: InvalidInputException if list is None
    """
    checkValidInput(array)

    # We define our 3 arrays
    smaller = []
    equal = []
    larger = []

    # if the length of our array is greater than 1
    # we perform a sort
    if len(array) > 1:
        # Select our pivot. This doesn't have to be
        # the first element of our array
        pivot = array[0]

        # recursively go through every element
        # of the array passed in and sort appropriately
        for number in array:
            if number < pivot:
                smaller.append(number)
            if number == pivot:
                equal.append(number)
            if number > pivot:
                larger.append(number)
        # recursively call quicksort on gradually smaller and smaller
        # arrays until we have a sorted list.
        return quick_sort(larger) + equal + quick_sort(smaller)
    else:
        return array



def radix_sort(array):
    """radix_sort: int array -> int array
        Purpose: Sort the input array of integers in descending order using the radixsort algorithm
        Example: radix_sort([4,5,1,3,2]) -> [5,4,3,2,1]
        Throws: InvalidInputException if list is None
    """
    checkValidInput(array)
    if len(array)<=1:
        return array

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

    for i in range(n):
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

    for i in range(n):
        array[i] = output[n-i-1]


def checkValidInput(array):
    if array is None:
        raise InvalidInputException('List cannot be empty')


if __name__ == "__main__":
    array = [4,5,1,3,2]
    print(merge_sort(array))
    print(quick_sort(array))
    print(radix_sort(array))    

