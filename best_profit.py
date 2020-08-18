class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Purpose: Returns the highest profit you can make 
        by buying and selling stock, at most once.

        Note: Scans graph from left to right, updating global max and min.
        
        """
        lowest = float('inf')
        highest = float('-inf')
        profit = 0
        for p in reversed(prices):
            if p > highest:
                highest = p
                lowest = float('inf')
                
            elif p <= highest:
                if p < lowest:
                    lowest = p
                    if highest - lowest > profit:
                        profit = highest - lowest
        return profit