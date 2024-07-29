class Solution1:

	def rowWithMax1s(self,arr):
		# code here
		row, col = 0, len(arr[0]) - 1
		max_len = -1
		while col >= 0 and row < len(arr):
		    if arr[row][col] == 1:
		        max_len = row
		        col -= 1
		    else:
		        row += 1
	    return max_len

class Solution2:

    def rowWithMax1s(self,arr):
        # code here
        max_ones = 0
        index = -1
        for i in range(len(arr)):
            summ = sum(arr[i])
            if summ > max_ones:
                index = i
                max_ones = summ
        return index
