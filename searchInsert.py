def searchInsert(nums, target):
    """Purpose: Returns the index if target is found.
    If not, returns the index where it would be if it were inserted in order.
    """
    if(nums == [] or nums == None):
        return
    if(target <= nums[0]):
        return 0
    if(target > nums[-1]):
        return len(nums)
        
    for i in range(len(nums)-1):
        if(nums[i] < target and nums[i+1] >= target):  
            return i+1
            
                
if __name__ == "__main__":
    a = [1,3,5,6]
    b = [0]
    
    assert(searchInsert(a,2) == 1), "Wrong answer"
    assert(searchInsert(a,3) == 2), "Wrong  answer"
    assert(searchInsert(a,6) == 4), "Wrong answer"
    assert(searchInsert(a, 10) == 4), "Wong answer"

    assert(searchInsert(b, 0) == 1), "Wrong"
    print("All tests passed!")