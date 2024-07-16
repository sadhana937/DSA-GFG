class Solution:
	def printString(self, s, ch, count):
		# code here
        mycount = 0
        string = ''
        for i in s:
            if mycount == count:
                string += i
            elif i == ch:
                mycount += 1
        return string
