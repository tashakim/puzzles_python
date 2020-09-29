# ## Support Code
# You will use the `FixedSizeArray` class below
# to implement `DynamicArray`. 
#
# You do __not__ need to modify anything FixedSizeArry
# but it will be helpful to read through the comments and 
# code to understand what this class does. 

class FixedSizeArray:
    """
    Fixed-size array class. 
    
    Use this as the data storage container when you implement DynamicArray. 
    DO NOT MODIFY.
    """
    # _access_count is a class variable that tracks how many times
    # `get`/`set` been called
    _access_count = 0

    def __init__(self, n):
        """
        Initializes `FixedSizeArray` of size `n` with all elements set to `None`.
        """
        if n <= 0:
            raise ValueError(
                "Tried to initialize `FixedSizeArray` with non-positive length")
        self._length = n
        self._internal_storage = [None] * n

    def __len__(self):
        return self._length

    def set(self, p, x):
        """
        Sets the element at position `p` to `x`. `p` should be in range [0,len(self)].
        """
        if p < 0 or p >= self._length:
            raise IndexError(
                "array index out of range, length is {} but tried to access "
                "index {}".format(self._length, p))
        FixedSizeArray._access_count += 1
        self._internal_storage[p] = x

    def get(self, p):
        """
        Returns the element at position `p`. `p` should be in range [0,len(self)).
        """
        if p < 0 or p >= self._length:
            raise IndexError(
                f"array index out of range, length is {self._length} but tried to "
                "access index {p}")
        FixedSizeArray._access_count += 1
        return self._internal_storage[p]

    def __str__(self):
        """
        Returns a printable string of the array content
        """
        return 'FixedSizeArray: ' + str(self._internal_storage)

    @classmethod
    def get_access_count(cls):
        """
        Returns the total number of times set() and get() have been called.
        """
        return cls._access_count
