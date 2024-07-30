class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        # code here
        p = len(m)
        if m[0][0] == 0 or m[p - 1][p - 1] == 0:
            return []
        paths = []
        def recursion(i, j, path):
            if i < 0 or j < 0 or i >= p or j >= p or m[i][j] == 0:
                return False
            if i == p - 1 and j == p - 1:
                paths.append(path)
                return True
            m[i][j] = 0
            
            # Down
            recursion(i + 1, j, path + 'D')
            # Right
            recursion(i, j + 1, path + 'R')
            # Up
            recursion(i - 1, j, path + 'U')
            # Left
            recursion(i, j - 1, path + 'L')
            m[i][j] = 1
            return False
        recursion(0,0,'')
        return sorted(paths)
