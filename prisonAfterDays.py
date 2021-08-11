class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        """
        Purpose: There are 8 prison cells in a row and each cell is either occupied or vacant.
        Each day, the cell is 'occupied' or 'vacant' according to the following rules:

        -If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
        -Otherwise, it becomes vacant.

        Returns the state of the prison after n days.

        """
        self.cache = {}
        
        def prisonAfterOneDay(arr, k):
            """
            Purpose: Returns state of prison after 1 day.

            """
            res = [0] * len(arr)
            for i in range(1, len(arr)-1):
                if arr[i-1] == arr[i+1]: 
                    res[i] = 1
                else: 
                    res[i] = 0
                    
            if tuple(res) in self.cache.values(): # identifies loops, if exists.
                return [k for k,v in self.cache.items() if v == tuple(res)][0]
            
            self.cache[k] = tuple(res)
            return res
                    
        for i in range(n):
            cells = prisonAfterOneDay(cells, i)
            if isinstance(cells, int): 
                r = n % len(self.cache) - 1
                if r < 0:
                    r = len(self.cache) - 1

                return self.cache[r]
