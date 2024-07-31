class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        # Find minimum length
        pattern = arr[0]
        for i in arr:
            if len(i) < len(pattern):
                pattern = i
        flag = True
        output = ''
        for i in range(len(pattern)):
            for string in arr:
                if string[i] != pattern[i]:
                    flag = False
                    break
            if not flag:
                break
            else:
                output += pattern[i]
        
        if len(output) > 0:
            return output
        else:
            return -1
