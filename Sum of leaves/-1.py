class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def sumOfLeaves(root):
    if root is None:
        return 0

    queue = []
    rows = [] 
    queue.append(root)
 
    while(len(queue) > 0):
        sumrow = 0
        for i in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            sumrow += node.val
        rows.append(sumrow)

    return rows

head = TreeNode(3)
head.left = TreeNode(9)
head.left.right = TreeNode(4)
head.right = TreeNode(20)
head.right.left = TreeNode(15)
head.right.right = TreeNode(7)

print(sumOfLeaves(head))        