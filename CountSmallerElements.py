from sortedcontainers import SortedList

class Solution1:

	def constructLowerArray(self,arr):
		# code here
		sorted_list = SortedList()
		ans = [0] * len(arr)
		for i in range(len(arr) - 1, -1, -1):
		    ans[i] = sorted_list.bisect_left(arr[i])
		    sorted_list.add(arr[i])
		return ans


#User function Template for python3
class Solution2:

    def constructLowerArray(self,arr):
        # code here
        sorted_arr = []
        ans = [0] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            count = 0
            for j in range(len(sorted_arr)):
                if arr[i] > sorted_arr[j]:
                    count += 1
                else:
                    break
            sorted_arr.append(arr[i])
            sorted_arr.sort()
            ans[i] = count
        
        return ans
                
                    
              
                
            
