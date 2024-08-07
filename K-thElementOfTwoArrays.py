#User function Template for python3

class Solution:
    def kthElement(self, k, arr1, arr2):
        i, j = 0, 0
        count = 0
        while i < len(arr1) and j < len(arr2):
            count += 1
            if count == k:
                return min(arr1[i], arr2[j])
            if arr1[i] < arr2[j]:
                i += 1
            else:
                j += 1
        
        if i + (k - count) - 1 < len(arr1):
            return arr1[i + (k - count) - 1]

        if j + (k - count) - 1 < len(arr2):
            return arr2[j + (k - count) - 1]
        
        
        
