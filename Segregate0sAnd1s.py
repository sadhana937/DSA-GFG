class Solution1:
    def segregate0and1(self, arr):
        # code here
        left = 0
        right = len(arr) - 1
        n = len(arr) - 1
        while left < right:
            while left < right and arr[left] == 0:
                left += 1
            while right > left and arr[right] == 1:
                right -= 1
            arr[left], arr[right] =arr[right], arr[left]


# Time limit exceeded
class Solution:
    def segregate0and1(self, arr):
        # code here
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] == 1:
                arr[right], arr[mid] = arr[mid], arr[right]
                right -= 1
            if arr[mid] == 0:
                arr[left], arr[mid] = arr[mid], arr[left]
                left += 1

                
            
