class Solution:
    
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self, arr):
        # Strictly increasing
        count = 0
        max_count = 0
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                count += 1
            else:
                count = 0
            max_count = max(count, max_count)
        return max_count
