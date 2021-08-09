class MRUQueue:
    """
    Purpose: Design a MRU (Most-Recently-Used) Queue.
    Brute force
    """

    def __init__(self, n: int):
        """
        Purpose: Constructs the MRUQueue with n elements: [1, 2, ..., n]
        """
        self.data = [x for x in range(1, n+1)]


    def fetch(self, k: int) -> int:
        """
        Purpose: Moves the k-th element (1-indexed) to the end of the queue,
        and returns it.
        """
        elm = self.data[k-1]
        self.data.pop(k-1)
        self.data.append(elm)

        return elm


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)