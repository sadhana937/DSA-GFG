class Solution:
    def smallestNumber(self, s, d):
        # code here
        if s > d * 9:
            return -1
        result = ['0'] * d
        for i in range(d - 1, -1, -1):
            if s > 9:
                result[i] = '9'
                s -= 9
            else:
                if i == 0:
                    result[i] = str(s)
                else:
                    result[i] = str(s - 1)
                    result[0] = '1'
                    break
        return int("".join(result))
