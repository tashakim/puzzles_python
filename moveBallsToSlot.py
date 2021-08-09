class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        Purpose: Returns an array with length of boxes, where answer[i] is the 
        minimum no. of operations needed to move all balls to the i-th box.

        Note: boxes[i] is '0' if box is empty, '1' if it contains one ball.

        """
        def getSum(i):
            """
            Purpose: Returns min. no. of operations to move all balls to i-th position.
            """
            tot_sum = 0
            for j in range(len(boxes)):
                if j != i and boxes[j] == '1':
                    tot_sum += abs(i-j)
            return tot_sum
        
        cur_idx = 0
        res = []

        while cur_idx < len(boxes):
            res.append(getSum(cur_idx))
            cur_idx += 1
        """
        res = [0] * len(boxes)
        while cur_idx < len(boxes):
            res[cur_idx] += getSum(cur_idx)
            cur_idx += 1
        """        
        return res
