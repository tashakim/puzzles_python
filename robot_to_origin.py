class Solution:
    def judgeCircle(self, moves: str) -> bool:
    """Purpose: Returns whether a robot starting at the origin of a 2D plane
    returns to the origin after it completes its moves.

    Note: Hash set is used to keep track of number of moves in each direction.
    Time complexity: O(n), where n is number of characters in input string.
    Space complexity: O(1), since directions hash set is always constant size.
    """
        dir = {'U':0, 'D':0, 'L':0, 'R':0}
        for c in moves:
            dir[c] += 1
        if dir['U'] == dir['D'] and dir['L'] == dir['R']:
            return True
        return False

    def judgeCircle(self, moves: str) -> bool:
    """Purpose: Different way, counts only the absolute no. of steps in U or L direction.

    Time complexity & space complexity: same as above.
    """
        dir = {'U':0, 'L':0}
        for c in moves:
            if c in 'UL':
                dir[c] += 1
            elif c == 'D':
                dir['U'] -= 1
            elif c == 'R':
                dir['L'] -= 1
        if dir['U'] == 0 and dir['L'] == 0:
            return True
        return False