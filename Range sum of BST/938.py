class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def dfsrangeSumBST(self, root, L, R):
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    ans += node.val
                if L < node.val:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        return ans
        
def rangeSumBST(root: TreeNode, low: int, high: int) -> int:
    if root is None:
        return 0

    queue = []
    rangesum = 0
    queue.append(root)
 
    while(len(queue) > 0):
        sumrow = 0
        for i in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if low <= node.val and node.val <= high:
                rangesum += node.val

    return rangesum


head = TreeNode(10)
head.left = TreeNode(5)
head.left.right = TreeNode(7)
head.left.left = TreeNode(3)
head.right = TreeNode(15)
head.right.right = TreeNode(18)

high = 15
low = 7

print(rangeSumBST(head, low, high))
