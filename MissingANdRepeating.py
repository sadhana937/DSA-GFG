from collections import Counter
class Solution:
    def findTwoElement( self,arr): 
        # code here
        n = max(arr)
        missing = 0
        twice = 0
        count = set()
        for i in arr:
            if i in count:
                twice = i
                break
            count.add(i)
        arr = set(arr)
        for i in range(1, n + 2):
            if i not in arr:
                missing = i
                break
        
        return [twice, missing]
