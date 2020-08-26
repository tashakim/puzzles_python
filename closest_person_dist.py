class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:  
        """Purpose: Returns the maximum possible distance to the closest 
        person, where people in a row of seats are represented as 1, 
        and empty seats as 0. 
        """
        max_distance = [0]*len(seats)

        for i in range(len(seats)):
            if seats[i] == 0:
                max_distance[i] = self.permanate(seats, i)
            else:
                max_distance[i] = 0
        return max(max_distance)
            
    def permanate(self, arr, i):
        k = 0
        if i == len(arr)-1: # edge case when position is left-most seat
            while i - k >= 0:
                if arr[i-k] ==0:
                    k+=1
                else: break
        elif i == 0:
            while i + k < len(arr): # edge case when position is right-most seat
                if arr[i+k] == 0:
                    k += 1
                else: break
        else:
            while i-k >= 0 and i+k < len(arr): # general case 
                if arr[i-k] == arr[i+k] == 0:
                    k += 1
                else: break
        return k


     def maxDistToClosest0(self, seats):
        """Purpose: Simplified version using helper methods within class.
        """
        dp = [0]*len(seats)
        for i in range(len(seats)):
        	if seats[i] == 0:
        		dp[i] = self.permenate(seats, i)
        return max(dp)
    
     def permanate(self, arr, i):
        left, right = 0, 0
        while i - left >= 0:
            if arr[i-left] != 1:
                left += 1
            else: break
        while i + right < len(arr):
   	        if arr[i+right] != 1:
                right += 1
            else: break

        if left == 0 or right == 0:
            return max(left, right)
        else:
            return min(left, right)

if __nam__ == "__main__":
	assert(maxDistToClosest([1,0,0,0,1,0,1]) == 2), "Wrong output"
	assert(maxDistToClosest([1,0,0,0]) == 3), "Wrong output"

	print("All tests passed!")