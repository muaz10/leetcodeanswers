class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(root: TreeNode) -> int:
    result = 0
    stack = []
    
    while(root or stack):
        if root:
            stack.append(root)
            root = root.right
            if root and root.left is None and root.right is None:
                result += root.val
        else:
            root = stack.pop()
            root = root.left
    
    return result

head = TreeNode(3)
head.left = TreeNode(9)
head.left.right = TreeNode(4)
head.right = TreeNode(20)
head.right.left = TreeNode(15)
head.right.right = TreeNode(7)

print(sumOfLeftLeaves(head))
