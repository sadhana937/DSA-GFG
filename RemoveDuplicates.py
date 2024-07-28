class Solution:
	def removeDups(self, str):
		seen = set()
		output = []
		for i in str:
		    if i not in seen:
		        output.append(i)
		        seen.add(i)
		return "".join(output)
