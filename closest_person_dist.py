class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:  
        max_distance = [0]*len(seats)

        for i in range(len(seats)):
            if seats[i] == 0:
                max_distance[i] = self.permanate(seats, i)
            else:
                max_distance[i] = 0
        return max(max_distance)
            
    def permanate(self, arr, i):
        k = 0
        if i == len(arr)-1:
            while i - k >= 0:
                if arr[i-k] ==0:
                    k+=1
                else: break
        elif i == 0:
            while i + k < len(arr):
                if arr[i+k] == 0:
                    k += 1
                else: break
        else:
            while i-k >= 0 and i+k < len(arr):
                if arr[i-k] == arr[i+k] == 0:
                    k += 1
                else: break
        return k