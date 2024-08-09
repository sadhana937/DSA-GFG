
class Solution:
    def Maximize(self, a): 
        # Complete the function
        mod = 10 ** 9 + 7
        a.sort()
        summ = 0
        for i, val in enumerate(a):
            summ += i * val
        return summ % mod
