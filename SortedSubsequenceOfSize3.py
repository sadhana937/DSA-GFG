# Time Complexity: O(n^3)
# Space Complexity: O(1)

class Solution:
    def find3Numbers(self, arr):
        # Code Here
        n = len(arr)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if arr[i] < arr[j] < arr[k]:
                        return [arr[i], arr[j], arr[k]]                   
        return []

# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def find3Numbers(self, arr):
        # Code Here
        n = len(arr)
        for i in range(1, n - 1):
            right = arr[i]
            for j in range(i + 1, n):
                right = max(right, arr[j])
            
            left = arr[i]
            for j in range(i):
                left = min(left, arr[j])
            
            if left < arr[i] < right:
                return [left, arr[i], right]
        
        return []

# Time Complexity: O(n)
# Space Complexity: O(2n)

class Solution:
    def find3Numbers(self, arr):
        # Code Here
        n = len(arr)
        left_min = [0] * n
        right_max = [0] * n
        
        left_min[0] = arr[0]
        for i in range(1, n):
            left_min[i] = min(left_min[i - 1], arr[i])
            
        right_max[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], arr[i])
            
        for i in range(1, n - 1):
            if left_min[i - 1] < arr[i] < right_max[i + 1]:
                return [left_min[i - 1], arr[i], right_max[i + 1]]
        return []

                
                

        
