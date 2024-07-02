'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
def compute(head): 
    #return True/False
    string = ''
    cur = head
    while cur:
        string += cur.data
        cur = cur.next
    
    i = 0
    j = len(string) - 1
    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True
