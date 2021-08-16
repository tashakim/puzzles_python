from itertools import permutations

def generatePermutations(self, arr, n):
    """
    Purpose: Implements permutation of k items out of n items, of array arr.
    Note: Utilizes backtracking, implemented using dfs.
    """
    def traverse(arr, k, depth, path, seen):
        if k == depth:
            self.res.append(path[:]) # deep copy
            return
        
        for i in range(len(arr)):
            if i not in seen:
                path.append(arr[i])
                seen.add(i)
                traverse(arr, k, depth+1, path, seen)

                path.pop()
                seen.remove(i)
        return

    self.res = []
    traverse(arr, k, 0, [], set())

    return self.res

def generatePermutations1(self, arr, n):
    """
    Purpose: Uses itertools.permutations to implement the above function.
    """
    p = permutations(arr)

    return [x for x in p]