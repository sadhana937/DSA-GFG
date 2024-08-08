#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def is_sum_tree(self, node):
        # code here
        def recursion(root):
            if not root:
                return True
            if not root.left and not root.right:
                return True
            if root.left and root.right:
                if root.left.data + root.right.data != root.data:
                    return False
            if not root.right:
                if root.left.data != root.data:
                    return False
            if not root.left:
                if root.right.data != root.data:
                    return False
            left = right = True
            if root.left:
                left = recursion(root.left)
            if root.right:
                right = recursion(root.right)
            return left and right
        return recursion(root)
            
            
