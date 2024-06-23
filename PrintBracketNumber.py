class Solution:
	def bracketNumbers(self, str):
		# code here
		stack = []
		count = 0
		output = []
		for i in str:
		    if i == '(':
		        count += 1
		        stack.append(count)
		        output.append(count)
		    elif i == ')':
		        output.append(stack.pop())
		return output
