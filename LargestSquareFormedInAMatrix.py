class Solution:
    def maxSquare(self, n: int, m: int, mat: List[List[int]]) -> int:
        if n == 0 or m == 0:
            return 0

        max_square = 0
        
        # Initialize the first row and first column
        for i in range(n):
            if mat[i][0] == 1:
                max_square = 1
        for j in range(m):
            if mat[0][j] == 1:
                max_square = 1
        
        # Iterate from the second row and second column
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][j] == 1:
                    mat[i][j] = min(mat[i-1][j], mat[i][j-1], mat[i-1][j-1]) + 1
                    max_square = max(max_square, mat[i][j])
        
        return max_square
