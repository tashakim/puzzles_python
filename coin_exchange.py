class Solution:
    def coinChange(self, coins: List[int], n: int) -> int:
    """Purpose: Returns the fewest number of coins that you need to reach an amount 'n'.
    Note: If the amount cannot be made up by any combination of coins, return -1.
    """
        dp =[0] + [float('inf')]*n
        
        for coin in coins:
            for i in range(coin, n+1):
                dp[i] = min(dp[i-coin] + 1, dp[i])
        if dp[n] == float('inf'):
            return -1
        
        return dp[n] 