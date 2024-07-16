class Solution:
    #Function to construct binary tree from parent array.
    def createTree(self,parent):
        nodes = [Node(i) for i in range(len(parent))]
        root = None
        
        for index, parent_index in enumerate(parent):
            cur = nodes[index]
            if parent_index == -1:
                root = cur
            else:
                parent_node = nodes[parent_index]
                if parent_node.left is None:
                    parent_node.left = cur
                else:
                    parent_node.right = cur
        
        return root
