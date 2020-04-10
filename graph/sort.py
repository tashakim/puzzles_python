#!/usr/bin/python3


class InvalidInputException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)


def merge_sort(array):
    """merge_sort: int array -> int array
        Purpose: Sort the input array of integers in descending order 
        using the merge sort algorithm.
        Examples: merge_sort([4,5,1,3,2]) -> [5,4,3,2,1]
                merge_sort([1,2,4]) -> [4,2,1]
        Throws: InvalidInputException if list is None.
        This algorithm runs in worst case O(n log(n)) time.
    """
    checkValidInput(array)

    n = len(array)
    if n > 1:
        # divides array into left and right subarrays
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
   # if size of array is 1 or less, returns the input array.
    else:
        return array


def quick_sort(array):
    """quick_sort: int array -> int array
        Purpose: Sort the input array of integers in descending order 
        using the quicksort algorithm.
        Examples: quick_sort([4,5,1,3,2]) -> [5,4,3,2,1]
                quick_sort([1,2,4]) -> [4,2,1]
        Throws: InvalidInputException if list is None
        This algorithm runs in expected case O(n log(n)) time.
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
        Purpose: Sort the input array of integers in descending order 
        using the radixsort algorithm.
        Examples: radix_sort([4,5,1,3,2]) -> [5,4,3,2,1]
                radix_sort([1,2,4]) -> [4,2,1]
        Throws: InvalidInputException if list is None/
        This algorithm runs in worst case O(dn) time, where 
        d is the number of digits in the largest number.
    """
    checkValidInput(array)

    if len(array)<=1:
        return array

    positive_array = list(filter((0).__lt__, array))
    negative_array = list(filter((0).__gt__, array))
    negative_array = [-x for x in negative_array]
    arrs = [positive_array, negative_array]

    for x in arrs:
        if len(x) > 0:
            max_element = max(x)
            digit = 1
            while max_element // digit > 0:
                radixSortHelper(x, digit)
                digit *= 10

    negative_array = [-x for x in negative_array][::-1]

    if (0 in array):
        num = array.count(0)
        return positive_array + [0]*num + negative_array
  
    return positive_array + negative_array


def radixSortHelper(array, digit):
    """radixSortHalper: int array, int digit
    Purpose: A helper method that is called by radix_sort() 
    method.
    """
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
    """checkValidInput: int array
        Purpose: Throws InvalidInputException if the input
        list is None, otherwise, does nothing.
    """
    if array is None:
        raise InvalidInputException('List cannot be empty')
    return
