class Solution:
    def canWinNim(self, n: int) -> bool:
    """Purpose: Let's play a nim game with me. 
    I'll tell you if I can or cannot win.

    Example: 
        1 -> True
        2 -> True
        3 -> True
        
        4 -> False
        5 -> 1 / 2 3 4 / 5 -> True 
        6 -> 1 2 / 3 4 5 / 6 -> True
        
        7 -> 1 2 3 / 4 5 6 7  (4) strategy: make a 4,5,6 for opponent
        8 -> 1 2 / 3 4 5 6 7 8 (6)
        9 -> 1 2 3 / 4 5 6 7 8 9 (6) 9-3 = 6. I.e., there exist some x in [1,2,3] s.t
            # n - x is in [4,5,6]
        
        10 -> 1 2 3 4 5 6 7 8 9 10
    """
        if n % 4 ==  0:
            return False

        return True
        
        