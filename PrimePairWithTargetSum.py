class Solution:
    def getPrimes(self, n : int) -> List[int]:
        # code here
        def isPrime(num: int) -> bool:
            if num <= 1:
                return False
            if num <= 3:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6
            return True

        a = 2
        b = n - 2

        while a <= b:
            if isPrime(a) and isPrime(b) and (a + b) == n:
                return [a, b]
            a += 1
            b = n - a

        return [-1, -1]
        
