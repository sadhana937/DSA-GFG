# Needs optimisation

import math
class Solution:
    
    def gcd(self, a, b):
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a
        
    def ETF (self, N):
        # code here
        count = 0
        for i in range(1, N):
            if self.gcd(N,i) == 1:
                count += 1
        return count
