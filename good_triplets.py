class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
    	"""
    	Purpose: Returns the no. of good triplets from input array.
    	"""
        count = 0
        for i in range(len(arr)-2):
            for j in range(i+1, len(arr)-1):
                for k in range(j+1, len(arr)):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1
        return count

if __name__ == "__main__":
	assert countGoodTriplets([3,0,1,1,9,7]) == 4, "Wrong answer"
	assert countGoodTriplets([1,1,2,2,3]) == 0, "Wrong answer"

	print("All tests passed!")