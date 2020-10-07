from FixedSizeArray import FixedSizeArray
import pytest

# 4. Use Test-First Design  thinking to write test cases for each TODO item 
#    a. Work incrementally and start with methods that don’t depend on other methods
#    b. After you write your tests for a method, implement it, and run it
#    c. Debug failing tests and methods as you go
#
# __Tips:__
# - Create helper methods when necessary

class DynamicArray:
    """
    This DynamicArray class provides set, get, append, insert, pop methods.  Data is stored internally 
    using a `FixedSizeArray` which is resized as needed. 
    """
    def __init__(self):
        """
        Purpose: Initializes an empty DynamicArray.

        Time Complexity: Average O(1), Worst-case O(1)
        """
        self._capacity = 4
        self._fixed_array = FixedSizeArray(self._capacity) # create new fixed-size array
        self._length = 0
        self._head = 0
        
    def __len__(self):
        return self._length
    

    def capacity(self):
        """
        Purpose: Returns the current capacity of the array.

        Time Complexity: Average O(1), Worst-case O(1)
        """
        return self._capacity
    

    def get(self, p):
        """
        Purpose: Returns the element at position `p`. 
        Note: Raises IndexError when p is not in index range of array.

        Time Complexity: Average O(1), Worst-case O(1)
        """
        if p < 0 or p >= self._length:
            raise IndexError(
                'array index out of range, size is {} but tried to access '
                'index {}'.format(self._length, p))
        
        return self._fixed_array.get(p)


    def set(self, p, x):
        """
        Purpose: Sets the element at position 'p' to 'x'.
        Note: Raises IndexError when p is not in index range of array.

        Time Complexity: Average O(1), Worst-case O(1)
        """
        if p < 0 or p >= self._length:
            raise IndexError(
                'array index out of range, size is {} but tried to access '
                'index {}'.format(self._length, p))
        self._fixed_array.set(p, x)


    def append(self, x):
        """ 
        Purpose: Adds an item to the end of the current array. 
        Note: When append is called on a full-capacity array, resizes itself to 
        double capacity and adds item x.

        Time Complexity: Average O(1) / Worst-case: O(n), when array needs to be resized.
        """
        # If array is not full, simply append item
        if self._length < self._capacity:
            self._fixed_array.set(self._head, x)
            self._head += 1
            self._length += 1
        # If array is full, move items into a new FixedArray with double capacity.
        else:
            # First, create a new Fixed Array with double capacity
            self._capacity *= 2 # update capacity
            temp_array = FixedSizeArray(self._capacity)
            
            # Copy original elements into this array
            for i in range(self._length):
                temp_array.set(i, self._fixed_array.get(i))
            
            temp_array.set(self._head, x) # append x to the end
            self._head += 1
            self._length += 1

            self._fixed_array = temp_array


    def insert(self, i, x):
        """
        Purpose: Insert an item `x` before position `i` of self.   
        Note: Raises IndexError when NOT 0 <= i <= len(self).

        Time Complexity: Average O(n), Worst-case O(n), where n is the length of array.
        """
        insert_index = i
        if not 0 <= i or not i <= self._length:
            raise IndexError('Index is out of range')
        # If array is full, move items into a new FixedArray with double capacity.
        if self._length >= self._capacity:
            self._capacity *= 2
            temp_array = FixedSizeArray(self._capacity)

            for i in range(self._length):
                temp_array.set(i, self._fixed_array.get(i))
            self._fixed_array = temp_array

        for k in range(self._length, insert_index, -1):
            self._fixed_array.set(k, self._fixed_array.get(k-1))

        self._fixed_array.set(insert_index, x)
        self._head += 1
        self._length += 1


    def pop(self, i=float('inf')):
        """
        Remove the item at position `i` of self, and returns it. 
        Note: a.pop() removes and returns the last item in self. 
        Note: Raises IndexError if NOT 0 <= i < len(self).
        
        Time Complexity: 
        pop(): Average O(1), Worst-case O(n), where n is length of array.
        pop(i): Average O(n), Worst-case O(n), where n is length of array.
        """
        # If array is empty, raise error
        if self._length == 0:
            raise IndexError('Array is empty. Cannot pop from array.')
        
        if i == float('inf'):
            i = self._length -1

        popped = self._fixed_array.get(i)

        for k in range(i+1, self._length):
            self._fixed_array.set(k-1, self._fixed_array.get(k))
        
        self._length -= 1
        self._fixed_array.set(self._head-1, None)
        self._head -= 1

        # If length is less than capcity/4, resize array.
        if self._length < self._capacity/4:
            self._capacity //= 2
            temp_array = FixedSizeArray(self._capacity)

            for i in range(self._length):
                temp_array.set(i, self._fixed_array.get(i))
            self._fixed_array = temp_array

        return popped


    def reverse(self):
        """
        Reverse the elements of the self, in-place.

        Time Complexity: Average O(n), Worst-case O(n), where n is the length of the array.
        """
        pivot = self._length//2
        start, end = 0, self._length -1 
        while start <= end:
            temp = self._fixed_array.get(start)
            self._fixed_array.set(start, self._fixed_array.get(end))
            self._fixed_array.set(end, temp)
            start += 1
            end -= 1

        return self._fixed_array


    def __str__(self):
        return f'DynamicArray: capacity={len(self._fixed_array)}, length={self._length}; Internal {self._fixed_array}; '


################ Testing #################### 
def assert_dynamic_array_equal(a, b):
    """
    Purpose: Defines an assertion method for our DynamicArray object.
    """
    if isinstance(a, DynamicArray) and isinstance(b, list):
        for i in range(len(a)):
            assert a.get(i) == b[i], "Values are not equivalent"

    elif isinstance(a, DynamicArray) and isinstance(b, DynamicArray):
        assert a.capacity() == b.capacity(), "Arrays have different lengths"
        for i in range(len(a)):
            assert a.get(i) == b.get(i), "Values are not equivalent"

    elif isinstance(a, list) and isinstance(b, DynamicArray):
        assert len(a) == b.capacity(), "Arrays have different lengths"
        for i in range(len(b)):
            assert b.get(i) == a[i], "Values are not equivalent"



def test_init():
    """
    Purpose: Tests that DynamicArray is initialized properly.
    """
    dl = DynamicArray()
    assert_dynamic_array_equal(dl, [])
    # Example of Exception testing
    
    with pytest.raises(IndexError):
        dl.pop()
    with pytest.raises(IndexError):
        dl.get(0)
    

def test_append():
    """
    Purpose: Tests that DynamicArray's append() method works correctly,
    and resizes array as appropriate.
    """
    dl = DynamicArray()
    dl.append(1)
    dl.append(2)
    assert_dynamic_array_equal(dl, [1, 2])
    dl.append('test')
    assert_dynamic_array_equal(dl, [1, 2, 'test'])


def test_resize():
    """
    Purpose: Tests that our DynamicArray doubles capacity and shrinks 
    doubly when necessary.
    """
    arr = DynamicArray()
    for i in range(1,5):
        arr.append(i)
    
    assert_dynamic_array_equal(arr, [1,2,3,4])
    
    arr.append(5)
    assert_dynamic_array_equal(arr, [1,2,3,4,5, None, None, None])

    arr.append(6)
    arr.append(7)
    arr.append(8)
    assert_dynamic_array_equal(arr, [1,2,3,4,5,6,7,8,None, None, None, None, None, None, None, None])


def test_capacity():
    """
    Purpose: Tests the capacity method returns correct capacity of 
    DynamicArray instance.
    """
    arr = DynamicArray()
    for i in range(2):
        arr.append(i)
    assert arr.capacity() == 4, "Wrong capacity"

    for i in range(3):
        arr.append(i)
    assert arr.capacity() == 8, "Wrong capacity"

    for i in range(4):
        arr.pop()
    assert arr.capacity() == 4, "Wrong capacity"

    arr.pop()
    assert arr.capacity() == 2, "Wrong capacity"


def test_get():
    """
    Purpose: Tests the get method returns correct element at input index,
    and raises an IndexError when index is out of range.
    """
    arr = DynamicArray()
    for i in range(4):
        arr.append(0)
    assert arr.get(1) == 0, "Wrong value"

    with pytest.raises(IndexError):
        arr.get(5)

def test_set():
    """
    Purpose: Tests the set method correctly sets the element at input index
    with the input value, and raises an IndexError when index is out of range.
    """
    arr = DynamicArray()
    with pytest.raises(IndexError):
        arr.set(1, 1)
    arr.append(1)
    arr.append(1)
    arr.set(1, 99)
    assert arr.get(1) == 99, "Wrong value"

    arr.set(0, 0)
    arr.set(1, 1)
    assert_dynamic_array_equal(arr, [0, 1, None, 99]), "Wrong values"
    arr.insert(2, 2)
    assert_dynamic_array_equal([0, 1, 2, 99], arr), "Wrong values"

    with pytest.raises(IndexError):
        arr.set(5, 0)


def test_insert():
    """
    Purpose: Tests the insert method correctly places input value into 
    the input index position.
    Also checks that an IndexError is raised when index is out of range.
    """
    arr = DynamicArray()
    with pytest.raises(IndexError):
        arr.insert(100, 0)
    arr.insert(0, 9)
    assert len(arr) == 1, "Wrong length"
    assert_dynamic_array_equal(arr, [9, None, None, None])


def test_pop():
    """
    Purpose: Tests that the pop method correctly removes element from 
    DynamicArray, and shrinks the array doubly when length of array is 
    less than capacity/4.
    """
    arr = DynamicArray()
    arr2 = DynamicArray()
    for i in range(9):
        arr.append(i)
        arr2.append(i+1)

    arr.pop(0)
    arr2.pop()
    assert_dynamic_array_equal(arr, arr2)

    for i in range(7):
        arr.pop()
        arr2.pop()
    assert_dynamic_array_equal(arr, arr2)
    

def test_reverse():
    """
    Purpose: Tests the reverse function correctly reverses all items 
    in the DynamicArray, including the case when array is not full.
    """
    arr = DynamicArray()
    for i in range(4):
        arr.append(i*10)
    assert_dynamic_array_equal(arr, [0,10,20,30])
    arr.reverse()
    assert_dynamic_array_equal(arr, [30,20,10,0]) # Tests reversal for full DynamicArray
    arr.insert(2,2)
    # [30,20,2,10,0]
    arr.reverse()
    assert_dynamic_array_equal(arr, [0,10,2,20,30, None, None, None]) # Tests reversal for non-full DynamicArray
    for i in range(4):
        arr.pop()
    assert_dynamic_array_equal(arr, [0])


# TODO: add test cases for all of your methods here.

# Use the following command to test your code and 
# generate a coverage report and listing
# $ python3 -m pytest --cov-report term --cov-report=annotate DynamicArray.py --cov
#
# After it runs the file DynamicArray.py,cover contains the 
# code coverage listing.  Lines that begin with '!' are not 
# covered by your tests.  Try running this now on 
# and checking out the coverage report and listing.

if __name__ == "__main__":
    print("Running tests...\n")
    tests = [test_init(), test_append(), test_resize(), test_capacity(), test_get(), test_set(), test_insert(), test_pop(), test_reverse()]
    
    # Run all test functions
    for test in tests:
        test

    print("All tests passed!")