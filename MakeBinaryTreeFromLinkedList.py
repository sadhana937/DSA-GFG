def convert(head):
    n = 0
    arr = []
    while head:
        arr.append(head.data)
        head = head.next
        n += 1
        
    def recursion(index):
        if index >= n:
            return
    
        newNode = Tree(arr[index])
        left = recursion(2 * index + 1)
        right = recursion(2 * index + 2)
        newNode.left = left
        newNode.right = right
        return newNode
        
    root = recursion(0)
    return root
