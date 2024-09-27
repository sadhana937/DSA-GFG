class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,k,arr):
        
        #code here
        cur_max = max(arr[0: k])
        output = []
        for i in range(len(arr) - k + 1):
            if arr[i - 1] == cur_max:
                cur_max = max(arr[i:i+k])
            if arr[i + k - 1] > cur_max:
                cur_max = arr[i + k - 1]
            output.append(cur_max)
        
        return output
