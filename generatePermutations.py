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

def generatePermutations2(self, arr: List[str], k):
    """
    Purpose: 
    Input: 
    ["a", "b", "c"], 1   ->    ['a', 'b', 'c']
    ["a", "b", "c"], 2   ->    ['aa', 'ba', 'ca', 'ab', 'bb', 'cb', 'ac', 'bc', 'cc']
    ["a", "b", "c"], 3   ->    ['aaa', 'baa', 'caa', 'aba', 'bba', 'cba', 'aca', 'bca', 'cca', 'aab', 'bab', 'cab', 'abb', 'bbb', 'cbb', 'acb', 'bcb', 'ccb', 'aac', 'bac', 'cac', 'abc', 'bbc', 'cbc', 'acc', 'bcc', 'ccc']
    """
    if k == 1: 
        return arr
    
    return [y + x for y in generatePermutations2(arr, 1) for x in generatePermutations2(arr, k-1)]
