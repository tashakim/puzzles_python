class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        """
        Purpose: Given input `logs` represented by a 2D integer array where 
        logs[i] = [ID_i, time_i], returns the user with ID_i performed an action at minute time_i.

        Note: Multiple users can perform actions simultaneously, and 
        a single user can perform multiple actions in the same minute.
        Also, a minute can only be counted once, even if multiple actions occur during it.
        
        Output: Calculates a 1-indexed array `answer` of size k such that, for each j (1<=j<=k), 
        answer[j] is the number of users whose UAM equals j.

        """
        d = {}
        
        for log in logs:
            user_id = log[0]
            minute = log[1]

            if user_id in d:
                if minute in d[user_id]: 
                    pass
                else: 
                    d[user_id].append(minute) 
            else: 
                d[user_id] = [minute]
        
        ans = [0] * k

        for k, v in d.items():
            ans[len(v)-1] += 1
            
        return ans