class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        stack = []
        dictionary = {'[':']', '(':')', '{':'}'}
        for i in x:
            if i in dictionary.keys():
                stack.append(i)
            else:
                if stack and dictionary[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        else:
            return True
