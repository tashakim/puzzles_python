class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int):
        """
        Purpose: Returns the maximum number of boxes that can be put on truck, where
        input array boxTypes[i] = number_of_boxes[i], number_of_units_per_box[i]]
        truckSize indicates the max no. of boxes that can be put on the truck.
        """
        def mysort(arr):
            return arr[1]

        tot = 0
        boxTypes = sorted(boxTypes, key=lambda x: mysort(x)) # O(n)
        
        while truckSize > 0: 
            if len(boxTypes) <= 0: # O(n)
                return tot
            truckSize -= 1
            tot += boxTypes[-1][1]
            
            boxTypes[-1][0] -= 1
            
            if boxTypes[-1][0] == 0:
                boxTypes.pop()
                
        return tot