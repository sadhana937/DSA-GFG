class Solution:
    def kPangram(self,string, k):
    # code here
        string = [i for i in string if i != " "]
        if len(string) >= 26:
            string = set(string)
            if len(string) + k >= 26:
                return True
            else:
                return False
        else:
            return False
