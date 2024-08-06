#User function Template for python3
class Solution:
    def isValid(self, str):
        #code here
        count = str.count('.')
        new = str.split('.')
        if "" in new or count != 3:
            return False
        for i in new:
            if i[0] == '0' and int(i) != 0:
                return False
            if 0 > int(i) or int(i) > 255:
                return False
        return True
                
            
                

