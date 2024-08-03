class Solution:
    def celebrity(self, mat):
        # code here
        n = len(mat)
        index = 0
        
        # A person who doesn't know others
        for i in mat:
            if sum(i) == 0:
                break
            index += 1
        
        if index >= n:
            return -1
            
        # Finding if the rest of others know this person
        for i in range(n):
            if i != index and mat[i][index] != 1:
                return -1
        
        return index
