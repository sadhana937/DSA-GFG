class Solution:
    def ExtractNumber(self,sentence):
        #code here
        sentence = sentence.split()
        numbers = []
        for i in sentence:
            if i.isdigit() and '9' not in i:
                    numbers.append(int(i))
        return max(numbers, default = -1)
