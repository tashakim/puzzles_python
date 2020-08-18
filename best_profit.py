class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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