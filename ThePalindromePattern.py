class Solution1:
    def pattern(self, arr):
        n = len(arr)
        
        # Check for palindromic rows
        for i in range(n):
            if self.is_palindrome(arr[i]):
                return str(i) + " R"
        
        # Check for palindromic columns
        for i in range(n):
            column = [arr[j][i] for j in range(n)]
            if self.is_palindrome(column):
                return str(i) + " C"
        
        return -1
    
    def is_palindrome(self, lst):
        k = 0
        j = len(lst) - 1
        while k < j:
            if lst[k] != lst[j]:
                return False
            k += 1
            j -= 1
        return True

class Solution2:
    def pattern (self, arr):
        # code here
        n = len(arr)
        # for rows
        for i in range(n):
            k = 0
            j = n - 1
            flag = True
            while k < j:
                if arr[i][k] != arr[i][j]:
                    flag = False
                    break
                k += 1
                j -= 1
            if flag:
                return str(i) + " R"
                
        for i in range(n):
            k = 0
            j = n - 1
            flag = True
            while k < j:
                if arr[k][i] != arr[j][i]:
                    flag = False
                    break
                k += 1
                j -= 1
            if flag:
                return str(i) + " C"
        
        return -1
