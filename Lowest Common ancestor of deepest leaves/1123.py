# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lcaDeepestLeaves(root: Optional[TreeNode]) -> Optional[TreeNode]:
    parent = {}
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
            parent[node.left] = node
            que.append((node.left, level+1))
        if node.right:
            parent[node.right] = node
            que.append((node.right, level+1))
            
    if maxlevel == 0:
        return root
            
    lastlevelnodes = []
    
    while len(maxnodes) > 0:
        node, level = maxnodes.pop()
        if level == maxlevel:
            lastlevelnodes.append(node)
        else:
            break
    
    if len(lastlevelnodes) == 1:
        return lastlevelnodes[0]
    
    parents = []
    for node in lastlevelnodes:
        p = [node]
        while node in parent:
            p.append(parent[node])
            node = parent[node]
        parents.append(p[::-1])
    
    minl = min(len(i) for i in parents)
    prev = parents[0][0]
    for i in range(minl):
        val = parents[0][i]
        for j in parents:
            if val != j[i]:
                return prev
        prev = val
            
        
    return root
        
    
                
  