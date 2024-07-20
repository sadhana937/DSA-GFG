class Solution:
    def RemoveHalfNodes(self, node):
        #code here
        def recursion(root):
            if root is None:
                return 
            root.left = recursion(root.left)
            root.right = recursion(root.right)
            if root.left is None and root.right is None:
                return root
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            return root

        return recursion(node)
