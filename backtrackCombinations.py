class Solution:
    def genCombinations(arr, k):
        """
        Purpose: Generates all combinations of elements in `arr`, using backtracking.
        """
        def backtrack(arr, k, depth, path):
            if len(path) == k:
                self.res.append(path[:])
                return
            
            for i in range(depth, len(arr)):
                path.append(arr[i])
                backtrack(arr, k, depth+1, path)
                path.pop()

        self.res = []
        backtrack(arr, k, 0, [])
        
        return self.res


    def genPermutations(arr, k):
        """
        Purpose: Generates all permutations of elements in `arr` using backtracking.
        """
        def backtrack(arr, k, depth, path, seen):
            if depth == k:
                self.res.append(path[:])
                return

            for i in range(len(arr)):
                if i not in seen:
                    path.append(arr[i])
                    seen.add(i)
                    backtrack(arr, k, depth+1, path, seen)

                    path.pop()
                    seen.remove(i)
            return 

        self.res = []
        backtrack(arr, k, 0, [], set())

        return self.res