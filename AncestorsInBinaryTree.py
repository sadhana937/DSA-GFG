class Solution:

    def Ancestors(self, root, target):
        '''
        :param root: root of the given tree.
        :return: None, print the space separated post ancestors of given target., don't print new line
        '''
        #code here
        def dfs(root, path):
            if root is None:
                return False
            if root.data == target:
                return True
            path.append(root.data)
            if dfs(root.left, path) or dfs(root.right, path):
                return True
            path.pop()
            return False
            
        path = []   
        dfs(root, path)
        path.reverse()
        return path
