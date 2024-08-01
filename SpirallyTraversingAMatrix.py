class Solution2:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix):
        # code here
        output = []
        m = len(matrix)
        n = len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        while left <= right and top <= bottom:
            
            # Traversing right
            for i in range(left, right + 1):
                output.append(matrix[top][i])
            top += 1
            
            # Traversing down
            for i in range(top, bottom + 1):
                output.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                # Traversing left
                for i in range(right, left - 1, -1):
                    output.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                # Traversing up
                for i in range(bottom, top - 1, -1):
                    output.append(matrix[i][left])
                left += 1            
        
        return output

class Solution1:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix):
        # code here
        m = len(matrix)
        n = len(matrix[0])
        output = []
        count = -1
        i, j = 0, 0
        visited = set()
        while m > 0 and n > 0:
          
            # Traverse left
            while j < n:
                if (i, j) in visited:
                    return output
                output.append(matrix[i][j])
                visited.add((i, j))
                j += 1
            i += 1
            j -= 1
          
            # Traverse down
            while i < m:
                if (i, j) in visited:
                    return output
                output.append(matrix[i][j])
                visited.add((i, j))                
                i += 1
            j -= 1
            i -= 1
          
            #Traverse right
            while j > count:
                if (i, j) in visited:
                    return output
                output.append(matrix[i][j])
                visited.add((i, j))                
                j -= 1
            j += 1
            i -= 1
          
            # Traverse up
            count += 1
            while i > count:
                if (i, j) in visited:
                    return output
                output.append(matrix[i][j])
                visited.add((i, j))                
                i -= 1
              
            m -= 1
            n -= 1
            i = count + 1
            j = count + 1
        
        return output
