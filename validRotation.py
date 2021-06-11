class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # Runtime 44ms, faster than 100.00% python3 online submissions
        def rotate(mat, target):
            mat.reverse()
            for i in range(len(mat)):
                for j in range(i, len(mat)):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            return mat == target

        if mat == target: 
            return True
        mat2 = rotate(mat, target)
        mat3 = rotate(mat2, target)
        mat4 = rotate(mat3, target)

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4): 
                if mat == target: return True
                mat = [list(x) for x in zip(*mat[::-1])]
            return False 

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(4):
            mat.reverse()
            for i in range(1, len(mat)):
                for j in range(i):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            if mat == target:
                return True
        return False

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        self.bool = False
        def rotate(mat, target):
            mat.reverse()
            for i in range(len(mat)):
                for j in range(i, len(mat)):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            if mat == target: self.bool = True
            return mat
            
        if mat == target: return True
        mat2 = rotate(mat, target)
        mat3 = rotate(mat2, target)
        mat4 = rotate(mat3, target)
        
        return self.bool