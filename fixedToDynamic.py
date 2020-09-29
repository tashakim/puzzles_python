from FixedSizeArray import FixedSizeArray
import pytest

# 3. Review DynamicArray so that you understand how it should operate, add docstrings to each pre-coded method
# 4. Use Test-First Design  thinking to write test cases for each TODO item 
#    a. Work incrementally and start with methods that don’t depend on other methods
#    b. After you write your tests for a method, implement it, and run it
#    c. Debug failing tests and methods as you go
#
# __Tips:__
# - Remember to adjust the array length and 
# capacity as needed. 
# - Create helper methods when necessary (there is 
# at least one obvious one if you utilize 
# the DRY Principle; see 
# https://en.wikipedia.org/wiki/Don%27t_repeat_yourself

class DynamicArray:
    """
    This DynamicArray class provides set, get, append, insert, pop methods.  Data is stored internally 
    using a `FixedSizeArray` which is resized as needed. 

    TODO: Implement the requested methods and design tests for each.  Use the `FixedSizeArray` class 
    to allocate the necessary memory.
    
    HINT: Do not inherit 'FixedSizeArray'. 
    """
    MIN_CAPACITY = 4

    def __init__(self):
        """
        Returns an empty DynamicArray.
        """
        self._fixed_array = FixedSizeArray(self.MIN_CAPACITY)
        self._length = 0
        
    def __len__(self):
        return self._length
    
    def capacity(self):
        """
        Purpose: Returns the current capacity of the array
        Time Complexity: O(n)
        """
        return len(self._fixed_array)
    
    def get(self, p):
        """
        Purpose: Returns the element at position `p`. `p` should be in range [0,len(self)]

        Time Complexity: 
        """
        if p < 0 or p >= self._length:
            raise IndexError(
                'array index out of range, size is {} but tried to access '
                'index {}'.format(self._length, p))
        
        return self._fixed_array.get(p)

    def set(self, p, x):
        """
        Purpose: 

        Time Complexity: O(1)
        """
        if p < 0 or p >= self._length:
            raise IndexError(
                'array index out of range, size is {} but tried to access '
                'index {}'.format(self._length, p))
        self._fixed_array.set(p, x)

    def append(self, x):
        """ 
        Purpose: Adds an item to the end of the current array. 
        """
        # TODO: Implement me! Remember to update length and capacity as needed.
        if self.capacity() > self._length:
            self.set(self._length-1, x)
            self._length += 1
        else:
            new_array = FixedSizeArray(self._length*2)
            self._length = 0
            for i in range(self._length):
                new_array[i] = self._fixed_array[i]
                self._length += 1
            new_array[self._length] = x
            self._fixed_array = new_array
        return 

    def insert(self, i, x):
        """
        Insert an item `x` before position `i` of self.   
        Requires 0 <= i <= len(self), otherwise, `IndexError` is raised.
        """
        # TODO: Implement me! Remember to update length and capacity as needed.
        pass

    def pop(self, i=None):
        """
        Remove the item at position `i` of self, and return
        it. a.pop() removes and returns the last item in self. 
        Requires 0 <= i < len(self), otherwise, `IndexError` is raised.
        """
        # TODO: Implement me! Remember to update length and capacity as needed.
        

    def reverse(self):
        """
        Reverse the elements of the self, in place.
        Time Complexity: O(n)
        """
        return self._fixed_array.reverse()

    def __str__(self):
        return f'DynamicArray: capacity={len(self._fixed_array)}, length={self._length}; Internal {self._fixed_array}; '



## Testing 
# Below are three example test cases

def assert_dynamic_array_equal(a, b):
    assert len(a) == len(b)
    for i in range(len(b)):
        assert a.get(i) == b[i]


def test_init():
    dl = DynamicArray()
    assert_dynamic_array_equal(dl, [])
    # Example of Exception testing
    """
    with pytest.raises(IndexError):
        dl.pop()
    with pytest.raises(IndexError):
        dl.get(0)
    """

def test_append():
    dl = DynamicArray()
    dl.append(1)
    dl.append(2)
    assert_dynamic_array_equal(dl, [1, 2])
    dl.append('test')
    assert_dynamic_array_equal(dl, [1, 2, 'test'])

# TODO: add test cases for all of your methods here.

# Use the following command to test your code and 
# generate a coverage report and listing
# $ python3 -m pytest --cov-report term --cov-report=annotate DynamicArray.py --cov
#
# After it runs the file DynamicArray.py,cover contains the 
# code coverage listing.  Lines that begin with '!' are not 
# covered by your tests.  Try running this now on 
# and checking out the coverage report and listing.

# Please refer to the README and handout for full guidance 
# and remember to answer the questions for your project in 
# report.md!

if __name__ == "__main__":
    # **Examples**
    arr = DynamicArray()
    print('Length:', len(arr))
    arr.append(3)
    arr.append(4)
    print('The first element is:', arr.get(0))
    print(arr)
    # arr.set(5, 7) # No error when your DynamicArray is finished!
