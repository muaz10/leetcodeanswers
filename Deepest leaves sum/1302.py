# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deepestLeavesSum(root: Optional[TreeNode]) -> int:
    que = []
    que.append((root, 0))
    maxnodes = []
    maxlevel = 0
    
    while len(que)>0:
        node, level = que.pop(0)
        if node.left is None and node.right is None:
            if level >= maxlevel:
                maxlevel = level
                maxnodes.append((node, level))
        if node.left:
            que.append((node.left, level+1))
        if node.right:
            que.append((node.right, level+1))
            
    if maxlevel == 0:
        return root.val
            
    lastlevelnodes = 0
    
    while len(maxnodes) > 0:
        node, level = maxnodes.pop()
        if level == maxlevel:
            lastlevelnodes += node.val
        else:
            return lastlevelnodes
    
    return lastlevelnodes