class Solution:
    def delete_node(self, head, x):
        #code here
        if x == 1:
            head = head.next
            head.prev = None
            return head
        temp = head
        prev = None
        while x > 1:
            x -= 1
            prev = temp
            temp = temp.next
        
        prev.next = temp.next
        temp.prev = prev
        return head
