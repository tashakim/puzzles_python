class Solution:
    def minEatingSpeed(self, piles, h):
        """
        Purpose: Returns the minimum integer `k` where you can eat all bananas in `h` hours.

        Rules: There are `n` piles of bananas, 
        the i-th pile has piles[i] bananas.
        You must finish eating after `h` hours.
        Each hour, you can choose any pile of bananas and eat `k` bananas from the pile.
        Note: If the pile has less than `k` bananas, you eat them all, then wait until the hour ends.

        """
        def possibleToEat(k):
            tot = 0
            for bananas in piles:
                tot += math.ceil(bananas/k)
            return tot <= k

        low, high = 1, max(piles)
        while low < high:
            mid = (low+high)//2
            if possibleToEat(mid):
                high = mid
            else:
                low = mid + 1

        return low